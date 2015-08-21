#xarequest.py
import os
import threading
import time
import win32com.client

from .abstract_component import AbstractQueryProviderComponent
from .abstract_component import AbstractSubscriptionProviderComponent

class XAQueryEvents:
	def __init__(self):
		self._event_object_connector = XAQueryEvents.event_object_connector

	def OnReceiveData(self, szTrCode):
		try:
			self._event_object_connector.logger.debug("OnReceiveData("+str(szTrCode)+")")
			self._event_object_connector.on_receive_data_arg = szTrCode
			#원래는 outblock 접근코드가 이 쓰레드에 있어야하지만 전체 query코드가 블럭이므로
			#query 자체가 나가지 않으므로 이 쓰레드에서 다른 쓰레드로 나가더라도 안전함
			#하지만 subscribe의 경우 다름
		except Exception as ex:
			self._event_object_connector.logger.warn("OnReceiveData error: %s", ex)
			self._event_object_connector.logger.debug(ex, exc_info=True)
			return None
		finally:
			#? tr_code 검사가 필요한가?
			self._event_object_connector.on_receive_data_event.set()

	def OnReceiveMessage(self, bIsSystemError, szMessageCode, szMessage):
		try:
			self._event_object_connector.logger.debug("OnReceiveMessage("+", ".join([str(bIsSystemError), str(szMessageCode), str(szMessage)])+")")
			self._event_object_connector.on_receive_message_arg = (bIsSystemError, szMessageCode, szMessage)
		except Exception as ex:
			self._event_object_connector.logger.warn("OnReceiveMessage error: %s", ex)
			self._event_object_connector.logger.debug(ex, exc_info=True)
			return None
		finally:
			self._event_object_connector.on_receive_message_event.set()

class XARealEvents:
	def __init__(self):
		self._event_object_connector = XARealEvents.event_object_connector

	def OnReceiveRealData(self, *args):
		start_time = time.time()
		try:
			self._event_object_connector.logger.debug("OnReceiveRealData("+str(args)+")")
			outblock = self._read_outblocks(self._event_object_connector.res_blocks)
			self._event_object_connector.logger.debug(str(outblock))
			self._event_object_connector.queue.put(outblock)
		except Exception as ex:
			self._event_object_connector.logger.warn("OnReceiveRealData error: %s", ex)
			self._event_object_connector.logger.debug(ex, exc_info=True)
			return None
		finally:
			self._event_object_connector.logger.debug('[It took %fs]', time.time() - start_time)
			pass
	def _read_outblocks(self, res_blocks, comp_yn_flag = False):
		outblocks = filter(lambda b:not b['is_input'], res_blocks)
		ret = dict()
		for block in outblocks:
			if not block['is_occurs']:
				sub_ret = dict()
				for arg in block['args']:
					sub_ret[arg['code']] = self._event_object_connector.xaquery_xareal.GetFieldData(block['bname'], arg['code'])
			else:
				sub_ret = list()
				block_count = 0
				if comp_yn_flag: # if compressed?
					decompressed_size = self._event_object_connector.xaquery_xareal.Decompress(block['bname'])
					if decompressed_size > 0:
						block_count = self._event_object_connector.xaquery_xareal.GetBlockCount(block['bname'])
				else:
					block_count = self._event_object_connector.xaquery_xareal.GetBlockCount(block['bname'])
				for occur in range(block_count):
					sub_sub_ret = dict()
					for arg in block['args']:
						sub_sub_ret[arg['code']] = self._event_object_connector.xaquery_xareal.GetFieldData(block['bname'], arg['code'])
					sub_ret.append(sub_sub_ret)
			ret[block['bname']] = sub_ret
		return ret

class EventObjectConnector:
	logger = None

class XARequest(AbstractQueryProviderComponent, AbstractSubscriptionProviderComponent):
	def __init__(self, xasession, res_info, query_block_timeout):
		self._res_info = res_info
		self._xasession = xasession
		self.query_block_timeout = float(query_block_timeout)

	def init(self):
		self.logger.info("Initializing XARequest_" + self._res_info['header']['tr_code'])

		self.event_object_connector = EventObjectConnector()
		self.event_object_connector.logger = self.logger.getChild(self._res_info['header']['tr_code'] + "_events")
		
		if self._res_info['header']['is_query']:
			self._init_xaquery()
		else:
			self._init_xareal()

		self.logger.debug('self.xaquery_xareal.GetTrCode():%s', self.xaquery_xareal.GetTrCode())

	def getAvailableQueryCodeSet(self):
		if self._res_info['header']['is_query']:
			return {'xing.'+self._res_info['header']['tr_code']}
		else:
			return {}
	def getAvailableSubscriptionCodeSet(self):
		if not self._res_info['header']['is_query']:
			return {'xing.'+self._res_info['header']['tr_code']}
		else:
			return {}
	def query(self, query_code, arg_set):
		try:
			if not self._res_info['header']['is_query']:
				return None
			if query_code.startswith('xing.'):
				query_code = query_code.split('.')[1]
			else:
				return None
			self.logger.info("query has been received(%s)", query_code)
			self._verify_arguments(query_code, arg_set)
			#self.logger.debug("argumentd verified")
			# 실제 inblock 처리
			comp_yn_flag = self._write_inblocks(arg_set)

			self.event_object_connector.on_receive_message_event.clear()

			self.event_object_connector.on_receive_data_event.clear()
			continu_query = True if arg_set.get('continue_query') else False

			#2015-05-07 period limit를 먼저 체크하고 그 후에 초당 콜 제한을 체크
			if self.limit_period != 0:
				current_time = time.time()
				#원방법은 list에 요청된 tr요청 시간을 모두 기록해 두고 정확하게 10분이 초과된 요청만 리스트에서 제거해가면서 요청 수 초과를 확인
				#self.last_calls = list(filter(lambda x:x>=(current_time-self.limit_period), self.last_calls))
				#2015-05-26 xingAPI의 period limit 체크 방법이 예상보다 단순하여 제한회피 조건을 이에 맞춰서 다시 구현(원 방법은 바로 위 라인)
				#eBEST 문의결과 최초 tr요청 시 시간을 기록하고 10분안에 200회를 초과한 요청이 들어오는지 확인, 10분이 지나게 되면 다시 이후의 최초 tr요청을 기준으로 반복
				if len(self.last_calls) > 0 and current_time - self.last_calls[0] > self.limit_period:
					self.last_calls = []
				if len(self.last_calls) >= self.limit_call_count:
					#제한에 걸림, 얼마나 sleep해야하는지 확인
					tmp_sleep_time = self.last_calls[0] + self.limit_period - current_time
					self.last_calls = []
					if tmp_sleep_time > 0:
						self.logger.debug('sleep for period limit:'+str(tmp_sleep_time))
						time.sleep(tmp_sleep_time)

			# 초당 요청제한 준수
			tmp_sleep_time = self.last_call + self.minimum_interval_between_calls - time.time()
			if tmp_sleep_time > 0: # 0.01초 루프를 여러번 보는것 보다 sleep타임 계산하는것이 적절 - 2015-05-07
				self.logger.debug('sleep:'+str(tmp_sleep_time))
				time.sleep(tmp_sleep_time)
			#while time.time() - self.last_call < self.minimum_interval_between_calls:
				#self.logger.debug('sleep:'+str(0.01))
				#time.sleep(0.01)

			request_ret = self.xaquery_xareal.Request(continu_query)
			# 리턴값 기반 에러처리
			while request_ret < 0:
				if request_ret in [-21,-15,-16,-17]:
					#될때까지 재시도 해야하는 에러
					self.logger.warn("Warnning request_ret:"+str(request_ret))
					time.sleep(self.minimum_interval_between_calls + 0.01)
					request_ret = self.xaquery_xareal.Request(continu_query)
				elif request_ret in [-1,-2,-3,-4,-7,-13,-14,-15]:
					#xasession을 다시 시작해야하는 에러
					self.logger.error("Error request_ret:"+str(request_ret))
					self._xasession.reconnect()
					break
				elif request_ret in [-5,-6,-8,-9,-10,-11,-12,-18,-19,-20,-22,-23,-24,-25]:
					#구제 불능 에러, 이메일로 알려야함
					self.logger.critical("Critical request_ret:"+str(request_ret))
					#TODO shutdown 코드 추가
					# exit()
					#우선은 재접속 시도
					self.logger.error("Error request_ret:"+str(request_ret))
					self._xasession.reconnect()
					break

			self.logger.debug("request_ret:"+str(request_ret))
			#TODO 에러처리 필수!
			if request_ret < 0:
				self.logger.warn("Request return:"+str(request_ret))
				return None
			else:
				if not self.event_object_connector.on_receive_message_event.wait(self.query_block_timeout):
					#timeout
					self._xasession.reconnect()
					return None
				self.last_call = time.time()
				#2015-05-07 호출 시간 수집
				if self.limit_period != 0:
					self.last_calls.append(time.time())

				#self.event_object_connector.on_receive_message_arg = (bIsSystemError, szMessageCode, szMessage)
				if not self.event_object_connector.on_receive_data_event.wait(self.query_block_timeout):
					#timeout
					self._xasession.reconnect()
					return None

				return self._read_outblocks(self._res_info['block'], comp_yn_flag)

		except Exception as ex:
			self.logger.warn("XARequest_" + self._res_info['header']['tr_code'] + " query error: %s", ex)
			self.logger.debug(ex, exc_info=True)
			return None
		finally:
			pass

	def subscribe(self, subscribe_code, arg_set, queue):
		try:
			if self._res_info['header']['is_query']:
				return None
			if subscribe_code.startswith('xing.'):
				subscribe_code = subscribe_code.split('.')[1]
			else:
				return None
			self.logger.info("subscribe has been received(%s)", subscribe_code)
			self._verify_arguments(subscribe_code, arg_set)
			#self.logger.debug("arguments verified")

			if self._subscribe_key_code is not None:
				key = list(arg_set.values())[0][self._subscribe_key_code]
				if self.event_object_connector.queue.register(queue, key):
					self._write_inblocks_for_subscription(arg_set)
					self.xaquery_xareal.AdviseRealData()
					self.logger.debug("Actual AdviseRealData called(key=%s)", key)
				else:
					self.logger.debug("Subscription add to existing queue(key=%s)", key)
			else:
				if self.event_object_connector.queue.register(queue):
					self._write_inblocks_for_subscription(arg_set)
					self.xaquery_xareal.AdviseRealData()
					self.logger.debug("Actual AdviseRealData called(no key)")
				else:
					self.logger.debug("Subscription add to existing queue(no key)")
			return True

		except Exception as ex:
			self.logger.warn("XARequest_" + self._res_info['header']['tr_code'] + " subscribe error: %s", ex)
			self.logger.debug(ex, exc_info=True)
			return None
		finally:
			pass

	def unsubscribe(self, subscribe_code, arg_set, queue):
		try:
			if self._res_info['header']['is_query']:
				return None
			if subscribe_code.startswith('xing.'):
				subscribe_code = subscribe_code.split('.')[1]
			else:
				return None
			self.logger.info("unsubscribe has been received(%s)", subscribe_code)
			self._verify_arguments(subscribe_code, arg_set)
			#self.logger.debug("arguments verified")

			if self._subscribe_key_code is not None:
				self.logger.debug("%s has a key", subscribe_code)
				key = list(arg_set.values())[0][self._subscribe_key_code]
				self.logger.debug("unregister from queue")
				if self.event_object_connector.queue.unregister(queue, key):
					self.logger.debug("call UnadviseRealDataWithKey(%s)", key)
					self.xaquery_xareal.UnadviseRealDataWithKey(key)
			else:
				self.logger.debug("%s has no key", subscribe_code)
				if self.event_object_connector.queue.unregister(queue):
					self.xaquery_xareal.AdviseRealData()
			#self.logger.debug("unsubscribe finished")
			return True
		except Exception as ex:
			self.logger.warn("XARequest_" + self._res_info['header']['tr_code'] + " unsubscribe error: %s", ex)
			self.logger.warn(ex, exc_info=True)
			return None
		finally:
			pass

	# internal methods
	def _write_inblocks(self, arg_set):
		comp_yn_flag = False
		for block_name in arg_set.keys():
			if block_name == 'continue_query':
				continue # it's not real inblock
			if isinstance(arg_set[block_name], dict): # non=occurs
				for arg_code in arg_set[block_name].keys():
					if arg_set[block_name][arg_code] is not None:
						self.xaquery_xareal.SetFieldData(block_name, arg_code, 0, arg_set[block_name][arg_code])
						if (not comp_yn_flag) and arg_code.lower() == 'comp_yn' and str(arg_set[block_name][arg_code]) == 'Y':
							comp_yn_flag = True # compress
			else: # occurs
				block_count = len(arg_set[block_name])
				self.xaquery_xareal.SetBlockCount(block_name, block_count)
				for i, arg_set1 in enumerate(arg_set[block_name]):
					for arg_code in arg_set1.keys():
						self.xaquery_xareal.SetFieldData(block_name, arg_code, i, arg_set1[arg_code])
		return comp_yn_flag

	def _read_outblocks(self, res_blocks, comp_yn_flag = False):
		outblocks = filter(lambda b:not b['is_input'], res_blocks)
		ret = dict()
		for block in outblocks:
			if not block['is_occurs']:
				sub_ret = dict()
				for arg in block['args']:
					sub_ret[arg['code']] = self.xaquery_xareal.GetFieldData(block['bname'], arg['code'], 0)
			else:
				sub_ret = list()
				block_count = 0

				if comp_yn_flag: # if compressed?
					decompressed_size = self.xaquery_xareal.Decompress(block['bname'])
					if decompressed_size > 0:
						block_count = self.xaquery_xareal.GetBlockCount(block['bname'])
				else:
					block_count = self.xaquery_xareal.GetBlockCount(block['bname'])
				for occur in range(block_count):
					sub_sub_ret = dict()
					for arg in block['args']:
						sub_sub_ret[arg['code']] = self.xaquery_xareal.GetFieldData(block['bname'], arg['code'], occur)
					sub_ret.append(sub_sub_ret)

			ret[block['bname']] = sub_ret
		return ret

	def _verify_arguments(self, tr_code, arg_set):
		# 전달받은 arg_set 검사 시작
		if self._res_info['header']['tr_code'] != tr_code:
			raise Exception('Wrong tr-code has been received (%s)', tr_code)
		inblocks = list(filter(lambda b:b['is_input'], self._res_info['block']))
		arg_set_key_set = set(arg_set.keys())
		inblocks_bname_set = set(map(lambda b:b['bname'], inblocks))

		if arg_set_key_set-inblocks_bname_set-{'continue_query'}:
			raise Exception('Unsupported inblock name has been  received (%s)', arg_set_key_set-inblocks_bname_set)

		for block_name in arg_set.keys():
			if block_name == 'continue_query':
				continue
			inblock = list(filter(lambda bn:bn['bname']==block_name, inblocks))[0]
			
			if inblock['is_occurs'] and isinstance(arg_set[block_name], dict):
				raise Exception("Unexpected dict('{}') for occurs found, list('[]]') should be here instead")
			if not inblock['is_occurs'] and isinstance(arg_set[block_name], list):
				raise Exception("Unexpected list('[]') for non-occurs found, dict('{}') should be here instead")

			if isinstance(arg_set[block_name], dict):
				arg_set_keys = set(arg_set[block_name].keys())
			else:
				arg_set_keys = set()
				for a in arg_set[block_name]:
					arg_set_keys.update(set(a.keys()))

			arg_code_set = set(map(lambda b:b['code'], inblock['args']))
			if arg_set_keys-arg_code_set:
				raise Exception('Unsupported argument code has been received (%s)', str(arg_set_keys-arg_code_set))
		# 전달받은 arg_set 검사 끝
	def _init_xaquery(self):
		self.event_object_connector.on_receive_data_event = threading.Event()
		self.event_object_connector.on_receive_message_event = threading.Event()

		XAQueryEvents.event_object_connector = self.event_object_connector
		self.xaquery_xareal = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",XAQueryEvents)
		self.xaquery_xareal.LoadFromResFile(os.path.join(self._xasession.res_dir_path, self._res_info['header']['tr_code']+'.res'))
		#print(dir(self.xaquery_xareal.GetTRCountPerSec.__self__))
		count_per_sec_limit = self.xaquery_xareal.GetTRCountPerSec(self._res_info['header']['tr_code'])
		self.logger.debug("self.xaquery_xareal.GetTRCountPerSec(%s)", self._res_info['header']['tr_code'])
		self.logger.debug('count_per_sec_limit(%s):%s', self._res_info['header']['tr_code'], str(count_per_sec_limit))
		
		#2015-05-26 신규 추가된 GetTRCountBaseSec api를 이용한 요청 제한 추가
		count_per_sec_base = self.xaquery_xareal.GetTRCountBaseSec(self._res_info['header']['tr_code'])
		self.logger.debug("self.xaquery_xareal.GetTRCountBaseSec(%s)", self._res_info['header']['tr_code'])
		self.logger.debug('count_per_sec_base(%s):%s', self._res_info['header']['tr_code'], str(count_per_sec_base))
		if count_per_sec_limit:
			self.minimum_interval_between_calls = count_per_sec_base / count_per_sec_limit
		else:
			self.minimum_interval_between_calls = 0
		self.logger.debug('self.minimum_interval_between_calls:%s', str(self.minimum_interval_between_calls))
		self.last_call = 0

		#2015-05-07 period limit을 위한 변수 설정
		self.limit_call_count, self.limit_period = self._getTrCountPerPeriod(self._res_info['header']['tr_code'])
		#self.limit_period 기간 안에 self.limit_call_count 횟수 이상의 콜은 금지(가능하지만 페널티(추가 딜레이)가 주어짐)
		self.last_calls = []

	def _init_xareal(self):
		XARealEvents.event_object_connector = self.event_object_connector
		self.xaquery_xareal = win32com.client.DispatchWithEvents("XA_DataSet.XAReal",XARealEvents)
		self.xaquery_xareal.LoadFromResFile(os.path.join(self._xasession.res_dir_path, self._res_info['header']['tr_code']+'.res'))

		self.event_object_connector.res_blocks = self._res_info['block']
		self.event_object_connector.xaquery_xareal = self.xaquery_xareal

		#subscribe의 inblock은 1개밖에 없음
		args = list(filter(lambda b:b['is_input'], self.event_object_connector.res_blocks))[0]['args']
		if len(args) > 0:
			#key 있음
			self._subscribe_key_code = args[0]['code']
			self.event_object_connector.queue = QueueConnectAndDispatcher(self._subscribe_key_code)
		else:
			#key 없음
			self._subscribe_key_code = None
			self.event_object_connector.queue = QueueConnectAndDispatcherWithoutKey()
	# internal methods
	def _write_inblocks_for_subscription(self, arg_set):
		for block_name in arg_set.keys():
			for arg_code in arg_set[block_name].keys():
				if arg_set[block_name][arg_code] is not None:
					self.xaquery_xareal.SetFieldData(block_name, arg_code, arg_set[block_name][arg_code])

	def finalize_com_object(self):
		if hasattr(self, 'xaquery_xareal'):
			del(self.xaquery_xareal)
		if hasattr(self.event_object_connector, 'xaquery_xareal'):
			del(self.event_object_connector.xaquery_xareal)

	#우선은 홈페이지에 공지된 trcode 리스트로 period 제한을 두는 코드를 구분
	#차후에는 api등을 통해 얻어 올 수 있도록 해야할 것(제공한다면) - 2015-05-07
	_tmp_periodLimitedTrCodes=["CCEAQ01100",
	"CCEAQ06000",
	"CCEAQ10100",
	"CCEAQ50600",
	"CCEBQ10500",
	"CDPCQ04700",
	"CDPCQ13900",
	"CDPCQ14400",
	"CEXAQ21100",
	"CEXAQ21200",
	"CEXAQ31100",
	"CEXAQ31200",
	"CEXAQ44200",
	"CFOAQ00600",
	"CFOAQ10100",
	"CFOAQ50400",
	"CFOBQ10300",
	"CFOBQ10500",
	"CFOBQ10800",
	"CFOEQ11100",
	"CFOEQ82600",
	"CFOEQ82700",
	"CFOFQ02400",
	"CFXBQ03700",
	"CFXBQ03900",
	"CFXBQ07000",
	"CFXBQ08400",
	"CFXBQ08600",
	"CFXBQ08700",
	"CFXBQ08800",
	"CFXBT03600",
	"ChartExcel",
	"ChartIndex",
	"CIDBQ01400",
	"CIDBQ01500",
	"CIDBQ01800",
	"CIDBQ02400",
	"CIDBQ03000",
	"CIDBQ05300",
	"CIDEQ00800",
	"CLNAQ00100",
	"CSPAQ00600",
	"CSPAQ02200",
	"CSPAQ02300",
	"CSPAQ03700",
	"CSPAQ12200",
	"CSPAQ12300",
	"CSPAQ13700",
	"CSPBQ00200",
	"CSPBQ01300",
	"f8301",
	"f8307",
	"f8309",
	"f8311",
	"FOCCQ33600",
	"FOCCQ33700",
	"MMDAQ91200",
	"o3101",
	"o3103",
	"o3104",
	"o3105",
	"o3106",
	"o3107",
	"o3116",
	"o3117",
	"t1302",
	"t1305",
	"t1308",
	"t1404",
	"t1405",
	"t1449",
	"t1471",
	"t1475",
	"t1485",
	"t1514",
	"t1516",
	"t1532",
	"t1537",
	"t1602",
	"t1603",
	"t1615",
	"t1617",
	"t1621",
	"t1631",
	"t1632",
	"t1633",
	"t1640",
	"t1662",
	"t1664",
	"t1665",
	"t1701",
	"t1702",
	"t1717",
	"t1752",
	"t1764",
	"t1771",
	"t1809",
	"t1825",
	"t1826",
	"t1833",
	"t1901",
	"t1902",
	"t1903",
	"t1904",
	"t1921",
	"t1926",
	"t1927",
	"t1941",
	"t1954",
	"t2106",
	"t2203",
	"t2209",
	"t2405",
	"t2421",
	"t2541",
	"t2545",
	"t2805",
	"t2813",
	"t2814",
	"t2816",
	"t2833",
	"t3102",
	"t3202",
	"t3320",
	"t3325",
	"t3341",
	"t3401",
	"t3518",
	"t3521",
	"t4201",
	"t8405",
	"t8406",
	"t8408",
	"t8409",
	"t8411",
	"t8412",
	"t8413",
	"t8414",
	"t8415",
	"t8416",
	"t8417",
	"t8418",
	"t8419",
	"t8424",
	"t8427",
	"t8428",
	"t8429",]

	def _getTrCountPerPeriod(self, trcode):
		if trcode in self._tmp_periodLimitedTrCodes:
			return 200, 600 #600초당 200회 까지 조회 가능
			#return 5, 10 #테스트코드 - 10초당 5회 까지 조회 가능
		else:
			return 0, 0

class QueueConnectAndDispatcher:
	def __init__(self, key_code):
		self._key_code = key_code
		self._queues = dict()
		self._lock = threading.Lock()
		self._queue_count = 0

	def register(self, queue, key):
		new_key = False
		with self._lock:
			queue_set = self._queues.get(key)
			if queue_set:
				queue_set.add(queue)
			else:
				queue_set = {queue}
				self._queues[key] = queue_set
				new_key = True
			self._queue_count += 1
			return new_key
	def unregister(self, queue, key):
		with self._lock:
			remove_key = False
			queue_set = self._queues.get(key)
			queue_set.remove(queue)
			if len(queue_set) == 0:
				self._queues.pop(key)
				remove_key = True
			self._queue_count -= 1
			return remove_key
	def getRegisteredQueuesCount():
		with self._lock:
			return self._queue_count
	#queue part
	def task_done(self):
		"""지원안함"""
		raise NotImplementedError('This should not be called')
	def join(self):
		with self._lock:
			for queue in self._queues.values():
				queue.join()
	def qsize(self):
		return 0
	def empty(self):
		return True
	def full(self):
		return False
	#def put(self, item, block=True, timeout=None):
	def put(self, item):
		#key 추출
		key = list(item.values())[0][self._key_code]
		with self._lock:
			queue_set = self._queues.get(key)
			if queue_set:
				for queue in queue_set:
					queue.put(item)
	def get(self, block=True, timeout=None):
		"""지원안함"""
		raise NotImplementedError('This should not be called')
	def put_nowait(self, item):
		"""지원안함"""
		raise NotImplementedError('This should not be called')
	def get_nowait(self):
		"""지원안함"""
		raise NotImplementedError('This should not be called')

class QueueConnectAndDispatcherWithoutKey:
	def __init__(self):
		self._queues = set()
		self._lock = threading.Lock()
	def register(self, queue):
		with self._lock:
			self._queues.add(queue)
			return len(self._queues)==1
	def unregister(self, queue):
		with self._lock:
			self._queues.remove(queue)
			return len(self._queues)==0
	def getRegisteredQueuesCount():
		with self._lock:
			return len(self._queues)
	#dummy queue part
	def task_done(self):
		"""지원안함"""
		raise NotImplementedError('This should not be called')
	def join(self):
		with self._lock:
			for queue in self._queues:
				queue.join()
	def qsize(self):
		return 0
	def empty(self):
		return True
	def full(self):
		return False
	#def put(self, item, block=True, timeout=None):
	def put(self, item):
		with self._lock:
			for queue in self._queues:
				queue.put(item)
		pass
	def get(self, block=True, timeout=None):
		"""지원안함"""
		raise NotImplementedError('This should not be called')
	def put_nowait(self, item):
		"""지원안함"""
		raise NotImplementedError('This should not be called')
	def get_nowait(self):
		"""지원안함"""
		raise NotImplementedError('This should not be called')