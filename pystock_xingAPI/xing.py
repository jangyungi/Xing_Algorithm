#xing.py
import threading
import logging
import sys

from .xasession import XASession
from .abstract_component import AbstractQueryProviderComponent
from .abstract_component import AbstractSubscriptionProviderComponent

class XingEnterExit:
	def __enter__(self):
		pass
	def __exit__(self, exc_type, exc_value, traceback):
		pass

class Xing:
	def __init__(self, server_address=None, port=None, server_type=None, showcerterror=None, user=None, password=None, cert_password=None, connect_retry_period=5, connect_max_retry=5, login_timeout=15, query_block_timeout=15, logger=None):
		self._server_address = server_address
		self._port = port
		self._server_type = server_type
		self._showcerterror = showcerterror
		self._user = user
		self._password = password
		self._cert_password = cert_password
		self._connect_retry_period = connect_retry_period
		self._connect_max_retry = connect_max_retry
		self._login_timeout = login_timeout
		self._query_block_timeout = query_block_timeout
		self._logger = logger

	def __enter__(self):
		if self._server_address is not None and self._port is not None and self._server_type is not None and self._showcerterror is not None and self._user is not None and self._password is not None and self._cert_password is not None and self._connect_retry_period is not None and self._login_timeout is not None and self._query_block_timeout is not None:
			#모두 입력됐다면
			if self.open(self._server_address, self._port, self._server_type, self._showcerterror, self._user, self._password, self._cert_password, self._connect_retry_period, self._connect_max_retry, self._login_timeout, self._query_block_timeout, self._logger):
				return self
			else:
				raise Exception('Login error')
		else:
			raise Exception('Arguments are needed for constructor')

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()

	def query(self, trcode, args=None):
		obj = self._query_dispatch_dict.get(trcode)
		if obj is None:
			raise Exception('There is no such trcode')
		with obj.lock:
			return obj.query(trcode, args)

	def subscribe(self, trcode, args, queue):
		obj = self._subscribe_dispatch_dict.get(trcode)
		if obj is None:
			raise Exception('There is no such trcode(%s)' % str(self._subscribe_dispatch_dict))
		with obj.lock:
			return obj.subscribe(trcode, args, queue)

	def unsubscribe(self, trcode, args, queue):
		obj = self._subscribe_dispatch_dict.get(trcode)
		if obj is None:
			raise Exception('There is no such trcode')
		with obj.lock:
			return obj.unsubscribe(trcode, args, queue)

	xasession = None
	def open(self, server_address, port, server_type, showcerterror, user, password, cert_password, connect_retry_period=5, connect_max_retry=5, login_timeout=15, query_block_timeout=15, logger=None):
		self.xasession = XASession(server_address, port, server_type, showcerterror, user, password, cert_password, connect_retry_period, connect_max_retry, login_timeout, query_block_timeout)
		if not logger:
			self.xasession.logger = logging.getLogger()
			#streamHandler = logging.StreamHandler(sys.stdout) # 표준출력용 핸들러 생성
			#self.xasession.logger.addHandler(streamHandler) # logger에 핸들러 추가
			#self.xasession.logger.setLevel(logging.DEBUG)
			#streamHandler.setLevel(logging.DEBUG)
		else:
			self.xasession.logger = logger
		self.xasession.xing = self
		self.xasession.thread = threading.Thread(target=self.xasession.run)
		self.xasession.thread.start()
		self.xasession.first_connection_event.wait()
		if self.xasession.is_connected():
			self._register(self.xasession, "XASession")
			return True
		else:
			self.xasession.thread.join()
			return False

	def close(self):
		if self.xasession is not None:
			self.xasession.stop()
			self.xasession.thread.join()
			self._unregister(self.xasession)


	_query_dispatch_dict = dict()
	_subscribe_dispatch_dict = dict()
	def _register(self, obj, name):
		obj.logger = self.xasession.logger.getChild(name)
		obj.init()

		if isinstance(obj, AbstractQueryProviderComponent):
			ret = obj.getAvailableQueryCodeSet()
			for q_name in ret:
				self._query_dispatch_dict[q_name] = obj
		if isinstance(obj, AbstractSubscriptionProviderComponent):
			ret = obj.getAvailableSubscriptionCodeSet()
			for q_name in ret:
				self._subscribe_dispatch_dict[q_name] = obj
		obj.lock = threading.Lock()
		return True

	def _unregister(self, obj):
		if isinstance(obj, AbstractQueryProviderComponent):
			ret = obj.getAvailableQueryCodeSet()
			for q_name in ret:
				self._query_dispatch_dict.pop(q_name)
		if isinstance(obj, AbstractSubscriptionProviderComponent):
			ret = obj.getAvailableSubscriptionCodeSet()
			for q_name in ret:
				self._subscribe_dispatch_dict.pop(q_name)