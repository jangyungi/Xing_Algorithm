#xasession.py
import os
import threading
import time
import win32com.client

from .xarequest import XARequest
from .res_parser import multi_res_parser

from .abstract_component import AbstractQueryProviderComponent

class XASessionEvents:
	def __init__(self):
		self._event_object_connector = XASessionEvents.event_object_connector

	def OnLogin(self, szCode, szMsg):
		try:
			self._event_object_connector.logger.debug("OnLogin("+", ".join([str(szCode), str(szMsg)])+")")
			self._event_object_connector.login_arg = (szCode, szMsg)
		except Exception as ex:
			self._event_object_connector.logger.warn("OnLogin error: %s", ex)
			self._event_object_connector.logger.debug(ex, exc_info=True)
			return None
		finally:
			self._event_object_connector.is_disconnected = False
			self._event_object_connector.event.set()

	def OnLogout(self):
		try:
			self._event_object_connector.logger.debug("OnLogout()")
		except Exception as ex:
			self._event_object_connector.logger.warn("OnLogout error: %s", ex)
			self._event_object_connector.logger.debug(ex, exc_info=True)
			return None
		finally:
			self._event_object_connector.event.set()

	def OnDisconnect(self):
		try:
			self._event_object_connector.logger.debug("OnDisconnect()")
		except Exception as ex:
			self._event_object_connector.logger.warn("OnDisconnect error: %s", ex)
			self._event_object_connector.logger.debug(ex, exc_info=True)
			return None
		finally:
			self._event_object_connector.is_disconnected = True

class EventObjectConnector:
	logger = None
	login_arg = None
	event = None
	is_disconnected = True

class XASession(AbstractQueryProviderComponent):
	def __init__(self, server_address, port, server_type, showcerterror, user, password, cert_password, connect_retry_period, connect_max_retry, login_timeout, query_block_timeout):
		self.conf_server_address = server_address
		self.conf_port = port
		self.conf_server_type = server_type
		self.conf_showcerterror = showcerterror
		self.conf_user = user
		self.conf_password = password
		self.conf_cert_password = cert_password
		self.conf_connect_retry_period = float(connect_retry_period)
		self.conf_connect_max_retry = float(connect_max_retry)
		self.conf_login_timeout = float(login_timeout)
		self.conf_query_block_timeout = float(query_block_timeout)
		self._just_connected_time_from_reconnect = 0
		self.xasession = None
		self.methods = {
			'xing.IsConnected':self.is_connected,
			'xing.GetAccountListCount':self._GetAccountListCount,
			'xing.GetAccountList':self._GetAccountList,
			'xing.GetAccountName':self._GetAccountName,
			'xing.GetAcctDetailName':self._GetAcctDetailName,
			'xing.GetAcctNickname':self._GetAcctNickname,
			'xing.GetServerName':self._GetServerName,
		}
		self.xa_objs = []
		self.first_connection_event = threading.Event()
		self.first_connection_event.clear()

	def reconnect(self):
		if time.time() - self._just_connected_time_from_reconnect > 5: #재접속 성공후 최소 5초는 지나야 다시 재접속 시도 가능(접속여부 상관없이)
			self.event_object_connector.is_disconnected = True

	def is_connected(self, arg_set=None):
		if not hasattr(self, 'xasession') or self.xasession is None:
			return False
			
		if self.xasession.IsConnected() and not self.event_object_connector.is_disconnected:
			return True
		else:
			return False

	def _GetAccountListCount(self, arg_set=None):
		return self.xasession.GetAccountListCount()

	def _GetAccountList(self, arg_set):
		return self.xasession.GetAccountList(arg_set)

	def _GetAccountName(self, arg_set):
		return self.xasession.GetAccountName(arg_set)

	def _GetAcctDetailName(self, arg_set):
		return self.xasession.GetAcctDetailName(arg_set)

	def _GetAcctNickname(self, arg_set):
		return self.xasession.GetAcctNickname(arg_set)

	def _GetServerName(self, arg_set=None):
		return self.xasession.GetServerName()

	def _load_query_and_subscription(self):
		res_files = list(map(lambda fn:os.path.join(self.res_dir_path,fn), [ f for f in os.listdir(self.res_dir_path) if os.path.isfile(os.path.join(self.res_dir_path,f)) ]))
		res_files = list(filter(lambda fn:not (fn.split('.')[0].endswith('_1') or fn.split('.')[0].endswith('_2')), res_files))
		res_ret = multi_res_parser(res_files)

		for res in res_ret:
			xa_obj = XARequest(self, res, self.conf_query_block_timeout)
			if xa_obj and self.xing._register(xa_obj, 'xarequest'+'_'+res['header']['tr_code']):
				self.xa_objs.append(xa_obj)

	def init_xasession(self):
		self.logger.debug('init_xasession')
		
		if self.xasession is None:
			self.event_object_connector = EventObjectConnector()
			self.event_object_connector.logger = self.logger.getChild("XASessionEvents")
			self.event_object_connector.event = threading.Event()
			XASessionEvents.event_object_connector = self.event_object_connector
			self.xasession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
			del(XASessionEvents.event_object_connector)
			self.res_dir_path = os.path.join(self.xasession.GetPath(), 'Res/')
			self.logger.debug('Res files path:%s', self.res_dir_path)
			#print(dir(self.xasession.IsConnected.__self__))

		ret = self.xasession.ConnectServer(self.conf_server_address, self.conf_port)

		if not ret:
			self.logger.error('ConnectServer Failed(address:%s, port:%d)', self.conf_server_address, self.conf_port)
			return False

		self.event_object_connector.event.clear()
		ret = self.xasession.Login(self.conf_user, self.conf_password, self.conf_cert_password, self.conf_server_type, self.conf_showcerterror)
		self.logger.debug('Login ret:'+str(ret))

		if ret != True:
			self.logger.error('Login Failed(user:%s, server_type:%s)', self.conf_user, self.conf_server_type)
			return False

		last_time = time.time()

		#need own message loop here
		while not self.event_object_connector.event.isSet():
			win32com.client.pythoncom.PumpWaitingMessages()
			time.sleep(0.1)
			if time.time() - last_time > self.conf_login_timeout: #시간내 로그인이 이루어지지 않으면 오류
				self.logger.error('Login Failed(timeout(%fsec))', self.conf_login_timeout)
				return False

		if self.event_object_connector.login_arg[0].strip() == '0000':
			self._just_connected_time_from_reconnect = time.time()
			self.event_object_connector.is_disconnected = False
			self.logger.debug('Login OK(szCode:%s, szMsg:%s)', self.event_object_connector.login_arg[0], self.event_object_connector.login_arg[1])
			return True
		elif self.event_object_connector.login_arg[0].strip() in ['8004','2004','2005']: # 8004:비빌번호 틀림,2005:공인인증서 비밀번호 틀림,2004:공인인증오류5회 등 진행되어서는 안되는 오류 발생
			self.logger.critical('Login process is stopped due to error occurs while trying to login, message:%s', self.event_object_connector.login_arg[1])
			raise Exception('Login process is stopped due to error occurs while trying to login, message:%s' % self.event_object_connector.login_arg[1])
		else:
			self.event_object_connector.is_disconnected = True
			self.logger.error('Login Failed(szCode:%s, szMsg:%s)', self.event_object_connector.login_arg[0], self.event_object_connector.login_arg[1])
			return False

	_is_stop = True
	_retry_count = 0
	def run(self):
		self._is_stop = False
		win32com.client.pythoncom.CoInitialize()
		try:
			try:
				while not self.init_xasession() and not self._is_stop:
					self._retry_count = self._retry_count+1
					if self._retry_count > self.conf_connect_max_retry:
						self.first_connection_event.set()
						self.logger.error("Failed login attempts exceed(%d)", self.conf_connect_max_retry)
						raise Exception('Failed login attempts exceed')
					self.logger.warn("Fail to init xasession, will try %f seconds later(%d/%d)", self.conf_connect_retry_period, self._retry_count, self.conf_connect_max_retry)
					time.sleep(self.conf_connect_retry_period)
				self._retry_count = 0

			except:
				del(self.xasession)
				self.first_connection_event.set()
				return

			if not self._is_stop:
				self._load_query_and_subscription()
			self.first_connection_event.set()

			while not self._is_stop:
				win32com.client.pythoncom.PumpWaitingMessages()
				time.sleep(0.001)
				if self.event_object_connector.is_disconnected:
					self.logger.warn("xasession disconnected somehow, init xasession again")
					while not self.init_xasession() and not self._is_stop:
						self._retry_count = self._retry_count+1
						if self._retry_count > self.conf_connect_max_retry:
							self.logger.error("Failed login attempts exceed(%d)", self.conf_connect_max_retry)
							raise Exception('Failed login attempts exceed')
						self.logger.warn("Fail to init xasession, will try %f seconds later(%d/%d)", self.conf_connect_retry_period, self._retry_count, self.conf_connect_max_retry)
						time.sleep(self.conf_connect_retry_period)
					self._retry_count = 0

			self.xasession.DisconnectServer()
			self.event_object_connector.is_disconnected = True

			for xa_obj in self.xa_objs:
				self.xing._unregister(xa_obj)
				if hasattr(xa_obj, 'finalize_com_object'):
					xa_obj.finalize_com_object()
			self.xa_objs.clear()

			del(self.xasession)
			if win32com.client.pythoncom._GetInterfaceCount() != 0:
				self.logger.warn("win32com.client.pythoncom._GetInterfaceCount():%d", win32com.client.pythoncom._GetInterfaceCount())
		finally:
			win32com.client.pythoncom.CoUninitialize()
		return False

	def stop(self):
		self._is_stop = True

	def getAvailableQueryCodeSet(self):
		return set(self.methods.keys())

	def query(self, query_code, arg_set):
		try:
			return self.methods[query_code](arg_set)
		except KeyError as ex:
			self.logger.warn("There is no such query: %s", ex)
		except Exception as ex:
			self.logger.warn(self.__class__.__name__ + " query error: %s", ex)
			self.logger.debug(ex, exc_info=True)
			return None
		finally:
			pass