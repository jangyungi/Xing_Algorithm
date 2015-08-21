from pystock_xingAPI import *
import sqlite3
import queue
import time
import threading

SERVER = "demo.ebestsec.co.kr"
ID = "kwtkwt"
PASS = "87102712"
ACCOUNT = "55501018061"
ACCOUNTPASS = "0000"

# 모든 주식 종목에 대한 데이터를 all_jongmok.db 에 저장함. 이 함수를 실행할 때마다 업데이트 됨.
def all_jongmok():
	#1. 우선 Xing 객체를 이용해서 주식 종목을 서버에서 가져 옵니다.
	# 주식종목조회(t8430)
	inblock_query_t8430 = {
		't8430InBlock' : {
			# 구분(0:전체1:코스피2:코스닥)
			'gubun' : 0
		}
	}
	ret = xing.query('xing.t8430', inblock_query_t8430)
			
	#2. sqlite3객체를 생성하고 DBUtil을 이용해서 주식 종목을 저장하기위한 테이블을 생성합니다.(이미 존재한다면 무시하도록 되어있습니다.)
	# db 생성
	conn = sqlite3.connect("all_jongmok.db")
	# SHCODES_TB라는 테이블 생성
	# tr code 't8430' 용 테이블로 생성
	# tr code 't8430'의 반환값 중 outblock 't8430OutBlock'을 위한 테이블임을 명시
	# ['shcode'] 는 옵셔널한 값으로 'shcode'를 테이블의 키로 쓰겠다는 뜻
	# 키나 인덱스를 지정하지 않아도 정상적으로 동작히자만 많은 데이터를 검색시에 느려집니다
	DBUtil.create_table_for_outblock(conn.cursor(), 'All_JONGMOK', 't8430', 't8430OutBlock', ['shcode'])
	#commit 잊지마세요
	conn.commit()

	#3. 이제 받은 데이터를 생성해 놓은 테이블에 집어 넣겠습니다
	#SHCODES_TB 테이블에 넣습니다
	#ret['t8430OutBlock'] : 반환받은 ret 중 아웃블럭 t8430OutBlock 를 넣습니다.(사실 예제의경우 아웃블럭이 1개밖에 없습니다 하지만 두개 이상인 tr code도 있습니다)
	#place_flag = True : 이미 있으면 교체하겠다는 뜻입니다 만약 False를 넣거나 아무것도 넣지 않으면 이미 있으면 무시합니다
	DBUtil.insert_for_outblock(conn.cursor(), 'All_JONGMOK', ret['t8430OutBlock'], place_flag = True)
	conn.commit()

def abstract(my_list):
	'''
		INPUT:
			(list):'shcode'를 키값으로 가지는 임의의 오브젝트 리스트
		OUTPUT:
			(list): 해당 'shcode'를 가지는 값에 대한 all_jongmok.db에 저장된 정보 튜플 리스트
	'''
	#1. all_jongmok.db를 이용하여 주어진 리스트에 관한 종목정보조회를 한 뒤 my_list_jungbo 리스트에 담기.
	my_list_jungbo=[]
	num = len(my_list)
	conn = sqlite3.connect("all_jongmok.db")
	for i in range(num):
		#gubun:1(코스피),2(코스닥)	expcode:확장코드	etfgubun:1(ETF),2(ETN)	uplmtprice:상한가	dnlmtprice:하한가
		#jnilclose:전일가	memedan:주문수량단위	recprice:기준가
		#my_list_jungbo 리스트에는 아래 정보들이 순서대로 튜플로서 들어감.
		ret = conn.cursor().execute("SELECT shcode, gubun, hname, expcode, etfgubun, uplmtprice, dnlmtprice, jnilclose, \
			memedan, recprice from All_JONGMOK where shcode=?;",(my_list[i]['shcode'],))
		my_list_jungbo.append(ret.fetchone())
		return my_list_jungbo


#현재까지 "거래량/현재가"" 상위 (num)개 출력
def my_volume(num = 5, gubun = '0', jnilgubun = '1', sdiff = -90, ediff = 90, jc_num = '-02063580288', sprice = 1000, eprice = 99999999, volume = 100000, idx = None):
	'''
	input:
		num : 출력할 종목 갯수
		gubun : 0(전체), 1(코스피), 2(코스닥)
		jnilgubun : 1(당일), 2(전일)
		sdiff : 검색시점 당시 등락율 검색 시작 지점
		ediff : 검색시점 당시 등락율 검색 종료 지점 (ex : 등락율 -50% 에서 50% 사이의 종목을 찾을 때 사용)
		jc_num : 관리종목, 시장경보, 투자유의 등 위험요소 모두 제거  *****str값 사용 가능한지 확인 필요!!!!*****
		sprice : 검색시점 당시 종목가격 시작 지점
		eprice : 검색시점 당시 종목가격 종료 지점 (ex : 1000원 에서 2000원 사이의 종목을 찾을 때 사용)
		volume : volume '이상'의 거래량 검색
		idx : 연속조회를 위한 플래그
	output:
		상위 num 개 종목튜플로 구성 된 리스트 
	'''

	# 거래량상위조회(t1452)
	inblock_query_t1452 = {
	't1452InBlock' : {
		# ±¸ºÐ
		'gubun' : gubun,
		# ÀüÀÏ±¸ºÐ
		'jnilgubun' : jnilgubun,
		# ½ÃÀÛµî¶ôÀ²
		'sdiff' : sdiff,
		# Á¾·áµî¶ôÀ²
		'ediff' : ediff,
		# ´ë»óÁ¦¿Ü
		'jc_num' : jc_num,
		# ½ÃÀÛ°¡°Ý
		'sprice' : sprice,
		# Á¾·á°¡°Ý
		'eprice' : eprice,
		# °Å·¡·®
		'volume' : volume,
		# IDX
		'idx' : idx
		},
		'continue_query':False
	}	

	my_list = []
	while True: #연속질의 루프
		ret = xing.query('xing.t1452', inblock_query_t1452)
		my_list.extend(ret['t1452OutBlock1'])
		
		if ret['t1452OutBlock']['idx'].strip() == '0':
			break	
		else:
		#여기까지 왔단말은 최소 1번 질의는 했단것이고 다음 질의를 위해 연속질의를 활성화시킵니다.
			inblock_query_t1452['continue_query'] = True
			inblock_query_t1452['t1452InBlock']['idx'] = ret['t1452OutBlock']['idx']
		#이제 다시 루프를 처음부터 돌 준비가 되었습니다.
		#for i in my_list:		확인차 출력하는부분
		#	print(i)
	#4. 이제 원하는 양 만큼 테이블에서 출력해보자.		
	for i in my_list:
		i['my_volume'] = int(i['volume'])/int(i['price'])
	my_list.sort(key=lambda k: k['my_volume'], reverse=True)
	return my_list[:num]	

global my_representative
my_representative=[]
def my_timing(jonmok, code):
	'''
	INPUT:
		(str)jonmok : 종목종류   ***종목종류 1(코스피), 2(코스닥)
		(str)code : 종목코드   ***종목코드 : shcode   
	OUTPUT:
		None *** 이 함수는 쓰레드(데몬) 용도이며 global변수 2개를 계속 변화시킨다.
	'''
	#2. 체결 inblock 생성 코스피(S3_), 코스닥(K3_) 및 큐를 만들고 구독신청!
	try:
		#먼저 큐를 만들자.
		q = queue.Queue()	

		if jonmok == '1':	#코스피 종목이라면!
			#구독 신청을 하기 위한 inblock 생성
			inblock_subscription_S3_ = {
				'InBlock' : {
					# 단축코드
					'shcode' : code
				}
			}
			# 구독 신청!
			xing.subscribe('xing.S3_', inblock_subscription_S3_, q)
		else:
			#코스닥 종목이라면!
			inblock_subscription_K3_ = {
				'InBlock' : {
					# 단축코드
					'shcode' : code
				}
			}
			# 구독 신청!
			xing.subscribe('xing.K3_', inblock_subscription_K3_, q)
	# 3. queue를 확인하여 수신된 데이터 출력
	# 여기서부터는 각각의 큐에 자동으로 데이터가 차곡차곡 쌓입니다.
	# 우리는 주기적으로(여기서는 1초마다) 큐에 뭔가 들어왔나? 보고
	# 들어왔으면 출력 해 주면 됩니다
		'''
		def inner_thread():
			global my_representative
			while True:
				while not q.empty():
					my_representative.append((q.get()['OutBlock']['price'],time.time()))
					print('global my_representative: ', my_representative)	#확인용		
		'''
		'''
		def inner_thread():
			global my_representative
			while True:
				for i in range(10):
					time.sleep(10)
					my_representative.append((q.get()['OutBlock']['price'],time.time()))
					if i>0:
						temp = ((int(my_representative[i][0])-int(my_representative[i-1][0])),(my_representative[i][1]-my_representative[i-1][1]))
						print('global my_representative: ', temp)	#확인용		


		th = threading.Thread(target=inner_thread)
		th.daemon = True
		th.start()
		
		while True:
			print ('wow')
			time.sleep(2)
			if len(my_representative) > 2:
				if int(my_representative[-1][0])-int(my_representative[-2][0]) == 0:
					return 'complete'
		'''
		while True:
			temp = q.get()['OutBlock']
			my_representative.append((temp['shcode'],temp['price'],time.time()))			

	except KeyboardInterrupt:
		print ('키보드 인터럽트 발생!!')  #
				

		# 이 예제에서는 while True: 로 무한루프를 돌고 있기 때문에 중단시키는 방법은 ctrl+c 를 눌러 종료할 수 밖에 없습니다;	
		# 4. 구독해제
		# 매매신호를 잡거나 ctrl+c 를 눌러서 키보드 인터럽트 예외가 발생하면 함수가 종료되는데
		# 종료하기전에 구독을 해제 시킵니다.
		# subscribe 중 unsubscribe를 하게되면 데이터 수신이 중단됩니다
	finally:
		if jonmok == '1':	#코스피 종목이라면!
			xing.unsubscribe('xing.S3_', inblock_subscription_S3_, q)
		else:
			xing.unsubscribe('xing.K3_', inblock_subscription_K3_, q)




'''
			#만약 매수 기준 알고리즘을 통과한다면 매수신호를 보낸다.
			for j in queue_list:
				if (float(queue_result_dic2[j]['OutBlock']['price'])-float(queue_result_dic1[j]['OutBlock']['price']))/float(queue_result_dic1[j]['OutBlock']['price'])*100 >= 0.02 :
					print('Value: ', (float(queue_result_dic2[j]['OutBlock']['price'])-float(queue_result_dic1[j]['OutBlock']['price']))/float(queue_result_dic1[j]['OutBlock']['price'])*100, flush=True)
					temp = queue_result_dic1[j]['OutBlock']['shcode']
					return (1, temp)
				else:
					print('Value: ', (float(queue_result_dic2[j]['OutBlock']['price'])-float(queue_result_dic1[j]['OutBlock']['price']))/float(queue_result_dic1[j]['OutBlock']['price'])*100, flush=True)
			#매수 기준 알고리즘을 통과하지 못한다면 계속 반복시킨다.
			for k in queue_list:
				queue_result_dic1[k] = queue_result_dic2[k]
			# 큐가 너무 차지 않도록 30초마다 비워준다.
			#for l in queue_list:
			#	l.__init__()
'''

def BuySell(shcode, volume, price, buyorsell, tradetype, account = ACCOUNT, passw = ACCOUNTPASS,\
	mgntrncode = "000", loandt = "", ordcnditpcode = "0"):
	'''
	INPUT:
		shcode(str) : 종목번호 (주식:종목코드, 모의투자:A+종목코드, ELW:J+종목코드)
		volume(long) : 주문수량
		price(double) : 주문가
		buyorsell(str) : 매매구분 (1:매도, 2:매수)
		tradetype(str) : 호가유형코드 (00:지정가, 03:시장가, 05:조건부지정가, 06:최유리지정가, 07:최우선지정가, 61:장개시전시간외종가)
		account(str) = ACCOUNT : 계좌번호
		passw(str) = ACCOUNTPASS : 입력비번
		mgntrncode(str) = "000" : 신용거래코드 (000:보통, 001:유통융자신규, 003:자기융자신규, 005:유통대주신규, 007:자기대주신규, 101:유통융자상환)
		loandt(str) = "" : 대출일
		ordcnditpcode(str) = "0" : 주문조건구분 (0:없음, 1:IOC, 2:FOK)
	OUTPUT:
	'''
	with Xing(SERVER, 20001, 1, 1, ID, PASS, "") as xing:

		# 현물정상주문(CSPAT00600)
		inblock_query_CSPAT00600 = {
		'CSPAT00600InBlock1' : {
		# 계좌변호
		'AcntNo' : account,
		# 입력비번
		'InptPwd' : passw,
		# 종목번호
		'IsuNo' : shcode,
		# 주문수량
		'OrdQty' : volume,
		# 주문가
		'OrdPrc' : price,
		# 매매구분
		'BnsTpCode' : buyorsell,
		# 호가유형코드
		'OrdprcPtnCode' : tradetype,
		# 신용거래코드
		'MgntrnCode' : mgntrncode,
		# 대출일
		'LoanDt' : loandt,
		# 주문조건구분
		'OrdCndiTpCode' : ordcnditpcode
			}
		}
		ret = xing.query('xing.CSPAT00600', inblock_query_CSPAT00600)

		print('test: ', ret['CSPAT00600OutBlock2']) #이게 찍히면 테스트는 성공
		return 'Trade Success!'


def test():
	while True:
		print('wow')
		time.sleep(2)

	#BuySell('A000150', 2, 0, '2', '03')





if __name__ == '__main__':
	test_list = [{'volume': '177367', 'change': '2500', 'price': '189000', 'jnilvolume': '291322', 'bef_diff': '60.88', 'sign': '5', 'diff': '-1.31', 'hname': 'POSCO', 'shcode': '005490', 'vol': '0.20'},
{'volume': '156533', 'change': '210', 'price': '5260', 'jnilvolume': '178659', 'bef_diff': '87.62', 'sign': '2', 'diff': '4.16', 'hname': 'DMS', 'shcode': '068790', 'vol': '0.79'},
{'volume': '143999', 'change': '400', 'price': '56500', 'jnilvolume': '241929', 'bef_diff': '59.52', 'sign': '2', 'diff': '0.71', 'hname': 'LG', 'shcode': '003550', 'vol': '0.08'},
{'volume': '143282', 'change': '2000', 'price': '120000', 'jnilvolume': '321173', 'bef_diff': '44.61', 'sign': '5', 'diff': '-1.64', 'hname': 'CJ CGV', 'shcode': '079160', 'vol': '0.68'}
]	#5개의 결과값이 들어있는 테스트 리스트
	with Xing(SERVER, 20001, 1, 1, ID, PASS, "") as xing:
		
		th = threading.Thread(target=my_timing, args=('2','044380'))
		th.daemon = True
		th.start()
		
		
		while True:
			print('wow')
			if len(my_representative)>1:
				print ('time_space : ',my_representative[-1][2]-my_representative[-2][2])
			time.sleep(2)
		
