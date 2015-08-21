#ex1_collect_shcodes.py

import sqlite3
from pystock_xingAPI import *
'''
def main():
	xing = Xing()
	if xing.open("demo.ebestsec.co.kr", 20001, 1, 1, "kwtkwt", "87102712", ""):

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
		conn = sqlite3.connect("test_db.db")
		# SHCODES_TB라는 테이블 생성
		# tr code 't8430' 용 테이블로 생성
		# tr code 't8430'의 반환값 중 outblock 't8430OutBlock'을 위한 테이블임을 명시
		# ['shcode'] 는 옵셔널한 값으로 'shcode'를 테이블의 키로 쓰겠다는 뜻
		# 키나 인덱스를 지정하지 않아도 정상적으로 동작히자만 많은 데이터를 검색시에 느려집니다
		DBUtil.create_table_for_outblock(conn.cursor(), 'SHCODES_TB', 't8430', 't8430OutBlock', ['shcode'])
		#commit 잊지마세요
		conn.commit()


		#3. 이제 받은 데이터를 생성해 놓은 테이블에 집어 넣겠습니다
		#SHCODES_TB 테이블에 넣습니다
		#ret['t8430OutBlock'] : 반환받은 ret 중 아웃블럭 t8430OutBlock 를 넣습니다.(사실 예제의경우 아웃블럭이 1개밖에 없습니다 하지만 두개 이상인 tr code도 있습니다)
		#place_flag = True : 이미 있으면 교체하겠다는 뜻입니다 만약 False를 넣거나 아무것도 넣지 않으면 이미 있으면 무시합니다
		DBUtil.insert_for_outblock(conn.cursor(), 'SHCODES_TB', ret['t8430OutBlock'], place_flag = True)
		conn.commit()
		
		xing.close()
'''


if __name__ == '__main__':
	conn = sqlite3.connect("all_jongmok.db")
	select_query = "SELECT shcode, gubun, hname, expcode, etfgubun, uplmtprice, dnlmtprice, jnilclose, memedan, recprice from All_JONGMOK where shcode='001040'"
	ret = conn.cursor().execute(select_query)
	print (ret.fetchone()[1])
