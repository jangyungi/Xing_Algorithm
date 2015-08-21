#ex2_collect_1d_data.py

import sqlite3
from pystock_xingAPI import *

def main():
	with Xing("demo.ebestsec.co.kr", 20001, 1, 1, "kwtkwt", "87102712", "") as xing:
		#1. 지난글에서 생성했던 db를 열어 주식 종목들을 가져옵니다.
		#테이블에서 가져오는 기능은 어떤걸 가져올지, 가져올 조건 등등에 따라 워낙 다양한 사용법이 있어
		#별도 모듈을 제공하지 않습니다. 정공법대로 가져옵니다.
		#하지만 주식 코드만을 가져오는것은 어렵지 않습니다
		conn = sqlite3.connect("test_db.db")
		select_query = "SELECT shcode from SHCODES_TB" # where문 없이 전체 종목코드 가져오기
		#select_query = "SELECT shcode from SHCODES_TB where gubun=1" # 코스피 종목만 가져오기
		#select_query = "SELECT shcode from SHCODES_TB where gubun=2" # 코스탁 종목만 가져오기
		ret = conn.cursor().execute(select_query)
		#여기까지하면 ret에 db에서 읽어온 shcode들이 들어있습니다.
		#아래 주석을 풀면 읽어온 종목코드를 출력합니다.
		# for row in ret:
		#	print(row[0])

		#2. 이제 db에서 읽은 종목코드를 이용하여 서버에서 데이터를 긁어옵시다
		# 긁어올 대상은 1980년 1월 1일 이후의 모든 데이터로 사실상 서버에 있는 모든 데이터를 대상으로 합니다.
		# 이렇게 하려면 연속 질의도 자동으로 사용해야 합니다.
		#우선 db에서 읽은 종목코드로 for을 돕니다
		#주의사항은 execut()의 반환값은 for문을 한밖에 못돕니다. 즉, 위 주석처리해 놓은 부분의 주석을 제거하면 아래 실제 루프는 무용지물이 되는거죠
		for row in ret:
			shcode = row[0]
			#2-1. db테이블 생성
			#종목 코드에 맞는 데이터를 가져오기 앞서 db에 저장하려면 알맞는 테이블을 생성해야겠죠
			#지난 글과 동일한 방법으로 테이블을 먼저 생성하겠습니다. 
			table_name = 'DATA_1D_'+shcode+'_TB'
			DBUtil.create_table_for_outblock(conn.cursor(), table_name, 't8413', 't8413OutBlock1', ['date'])
			#테이블 이름은 DATA_1D_종목코드_TB 로 하고
			#테이블 포맷은 t8413 trcode의 t8413OutBlock1를 저장할 수 있는 형태로 합니다.
			#키는 검색할때 가정 빈번히 사용되는 날짜로 하겠습니다.
			#테이블 생성뒤에 commit()으로 실제 db에 적용되도록 합니다.
			conn.commit()

			#2-2. 이제 실제 데이터를 긁어옵시다
			# trcode t8413번으로 데이터를 긁어오겠습니다. (늘 그렇든 pystock_xingAPI 모듈에 동봉된 inblock_template.py를 뒤져서 복사해서 쓰면 됩니다)
			# 주식챠트(일주월)(t8413)
			inblock_query_t8413 = {
				't8413InBlock' : {
					# 단축코드
					'shcode' : shcode, # shcode부분에 db에서 읽어온 shcode를 집어넣습니다
					# 주기구분(2:일3:주4:월)
					'gubun' : 2, # 일데이터를 가져오도록 설정합니다. (주데이터나 월데이터를 가져올려면 어떻게할지 보이시죠?)
					# 요청건수(최대-압축:2000비압축:500)
					'qrycnt' : None, # 우리는 시작일자, 종료일자로 제어할 것이기 때문에 이곳은 손대지 않아도 됩니다
					# 시작일자
					'sdate' : "19800101", # 1980년 1월 1일로 설정합니다. 
					# 종료일자
					'edate' : "99999999", # 99999999 로 입력하면 입력가능한 최고 큰 날짜인 오늘로 취급합니다
					# 연속일자
					'cts_date' : None, # 요부분은 연속 질의에 관련된 부분으로 나중에 사용합니다.
					# 압축여부(Y:압축N:비압축)
					'comp_yn' : 'Y' # pystock_xingAPI 모듈은 받은 데이터의 압축을 자동으로 풀어주므로 그냥 'Y'를 입력하면 됩니다. 대소문자 구분하는점에 주의
				},

				# 연속질의를 사용하려면 요부분이 중요합니다.
				# 모듈에서 제공하는 템플릿에는 없으므로 아래 라인을 추가 해 주세요
				# 사실 나중에 넣어도 되지만 알아보기 쉽게하기위해 우선 False로 넣어둡니다. 나중에 연속질의 즉, 두번째 이후의 질의에서는 이 값을 True로 바꿔야합니다
				'continue_query':False
			}
			# trcode의 사용법에대한 더 자세한 설명은 DevCenter나 이트레이드 홈페이지를 이용하세요

			#2-2-1. 연속질의 루프
			#연속질의의 시작입니다.
			#연속질의란 한번 질의로 원하는 모든데이터를 가져올 수 없을때
			#다음 데이터를 연속으로 이어서 받아오고자 할 때 사용합니다.(물론 해당 trcode에서 제공할때만요)
			#압축하면 t8413 질의의 경우 한번에 2000개 데이터를 가져오지만 일데잍를 가져와도
			#2000개로는 전체 데이터는 목가져오고(종목별로 상장된지 얼마안됐다면 이야기가 다르겠지만요) 여러번 데이터 요청을 해야합니다.
			while True: #연속질의 루프
				#데이터 요청
				data = xing.query('xing.t8413', inblock_query_t8413)
				#정상적으로 동작했다면 data에 요청한 데이터가 들어있겠죠
				#수신받은 데이터를 아까만든 테이블에 집어넣습니다.
				#여기서 주의할점
				#일데이터를 받을때 마지막의 오늘 데이터의경우 아직 장마감이 뒤지 않았다면
				#거래가 이루이지는 중이기 때문에 계속해서 변하게 됩니다.
				#즉 지급 받은데이터가 최종 데이터가 아니란건죠
				DBUtil.insert_for_outblock(conn.cursor(), table_name, data['t8413OutBlock1'], place_flag = False)

				if not data['t8413OutBlock']['cts_date'].strip():
					# cts_date 값이 비었단말은 더이상 연속질의할 내용이 없단 뜻입니다. 즉 commit하고 루프에서 빠져나가면 됩니다
					conn.commit()
					break

				#여기까지 왔단말은 최소 1번 질의는 했단것이고 다음 질의를 위해 연속질의를 활성화시킵니다.
				inblock_query_t8413['continue_query'] = True
				#연속질의를 위해서는 서버에 내가 어떤데이터를 받을차례라는 것을 알려야하는데 그것이 cts_date 입니다.
				# cts_XXXX 가 있으면 대부분 연속질의를 위한것 이라 보면됩니다.
				# 단, cts_XXXX 형태가 아닌 경우가 있으므로 새로운 tr code룰 사용할때는 DevCenter를 확인합시다
				# (이런이유로 이것은 모듈내에서 자동화가 불가능했죠;)
				inblock_query_t8413['t8413InBlock']['cts_date'] = data['t8413OutBlock']['cts_date']
				#이제 다시 루프를 처음부터 돌 준비가 되었습니다.

if __name__ == '__main__':
	main()
