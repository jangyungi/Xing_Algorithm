#ex5_xasession_api.py
#계좌정보 조회 api 테스트
from pystock_xingAPI import *

def main():
	with Xing("demo.ebestsec.co.kr", 20001, 1, 1, "kwtkwt", "87102712", "") as xing:

		print('IsConnected:'+str(xing.query('xing.IsConnected')))

		#계좌 개수 조회
		count = xing.query('xing.GetAccountListCount')
		print('AccountListCount:'+str(count))

		#모든 계좌정보 출력
		for i in range(count):
			#계좌번호 조회
			accountNumber = xing.query('xing.GetAccountList', i)
			print('AccountNumber:'+accountNumber)
			#계좌명 조회 및 출력
			print('AccountName:'+xing.query('xing.GetAccountName', accountNumber))
			#계좌세부명 조회 및 출력
			print('AcctDetailName:'+xing.query('xing.GetAcctDetailName', accountNumber))
			#계좌 별명 조회 및 출력
			print('AcctNickname:'+xing.query('xing.GetAcctNickname', accountNumber))
			print()

		#현재 접속중인 서버 명 조회 및 출력
		print('ServerName:'+xing.query('xing.GetServerName'))

if __name__ == '__main__':
	main()