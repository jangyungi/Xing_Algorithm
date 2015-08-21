#ex4_volume_data.py (변형)
#전일대비 거래량 증가 상위조회
import operator
from pystock_xingAPI import *

def main():
	with Xing("demo.ebestsec.co.kr", 20001, 1, 0, "kwtkwt", "87102712", "") as xing:
		# 거래량상위(t1452)
		inblock_query_t1452 = {
			't1452InBlock' : {
				# 구분
				'gubun' : 2,
				# 전일구분
				'jnilgubun' : 1, # 1:당일기준, 2:전일기준
				# 시작등락율
				'sdiff' : -90,
				# 종료등락율
				'ediff' : 90,
				# 대상제외
				'jc_num' : None,
				# 시작가격
				'sprice' : None,
				# 종료가격
				# 거래량
				'volume' : None,
				# IDX
				'idx' : None
			}
			,'continue_query':False
		}

		# 빈 리스트를 준비합니다
		vol_list = list()
		while True:
			data = xing.query('xing.t1452', inblock_query_t1452)

			# 조회 결과를 출력하지않고 리스트에 모두 넣습니다
			# 리스트에서 리스트로 내용을 모두 추가할때는 extend를 이용합니다
			# 리스트에 append로 리스트를 넣게되면 리스트 자체가 들어가므로 주의
			vol_list.extend(data['t1452OutBlock1'])

			# 이 예제에서 특이한부분은 이곳하나인데, t1452 tr은 연속조회를 위한 참조값이 idx이고
			# idx가 '0'이면 연속조회가 종료된 것 입니다
			if data['t1452OutBlock']['idx'].strip() == '0':
				break
			else:
				inblock_query_t1452['t1452InBlock']['idx'] = data['t1452OutBlock']['idx']
				inblock_query_t1452['continue_query'] = True

		# 받은 전체리스트를 루프돌면서
		# dict 객체에  vol_diff를 새로 만들어 전일대비 당일 거래량 차이값을 저장합니다
		#for row in vol_list:
		#	row['vol_diff'] = int(row['volume']) - int(row['jnilvolume'])

		# 리스트를 위에서만든 vol_diff기준으로 정렬합니다
		# 리스트에 dict객체가 들어있을때에는 "key=operator.itemgetter('vol_diff')" 를 인자로 주어
		# 원하는 키에 대해 정렬이 가능합니다
		# 기본은 오름차순 정렬이므로, reverse=True를 인자로 주어 내림차순으로 정렬합니다
		# vol_list.sort(key=operator.itemgetter('vol_diff'), reverse=True)
		# vol_list.sort(key=lambda k: int(k['volume']) - int(k['jnilvolume']), reverse=True)
		
		# 루프돌면서 모두 출력
		index = 1
		for row in vol_list:
			print('%4d. %6s %12d (%12d) - %s' % (index, row['shcode'], int(row['volume']), int(row['jnilvolume']), row['hname']))
			index += 1

if __name__ == '__main__':
	main()