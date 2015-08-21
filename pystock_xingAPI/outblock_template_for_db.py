# ETF호가잔량(B7)
db_outblock_subscription_B7_ = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# LP매도호가수량1
		'lp_offerho1' : 'long',
		# LP매수호가수량1
		'lp_bidho1' : 'long',
		# LP매도호가수량2
		'lp_offerho2' : 'long',
		# LP매수호가수량2
		'lp_bidho2' : 'long',
		# LP매도호가수량3
		'lp_offerho3' : 'long',
		# LP매수호가수량3
		'lp_bidho3' : 'long',
		# LP매도호가수량4
		'lp_offerho4' : 'long',
		# LP매수호가수량4
		'lp_bidho4' : 'long',
		# LP매도호가수량5
		'lp_offerho5' : 'long',
		# LP매수호가수량5
		'lp_bidho5' : 'long',
		# LP매도호가수량6
		'lp_offerho6' : 'long',
		# LP매수호가수량6
		'lp_bidho6' : 'long',
		# LP매도호가수량7
		'lp_offerho7' : 'long',
		# LP매수호가수량7
		'lp_bidho7' : 'long',
		# LP매도호가수량8
		'lp_offerho8' : 'long',
		# LP매수호가수량8
		'lp_bidho8' : 'long',
		# LP매도호가수량9
		'lp_offerho9' : 'long',
		# LP매수호가수량9
		'lp_bidho9' : 'long',
		# LP매도호가수량10
		'lp_offerho10' : 'long',
		# LP매수호가수량10
		'lp_bidho10' : 'long',
		# 단축코드
		'shcode' : 'char',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가잔량1
		'offerrem1' : 'long',
		# 매수호가잔량1
		'bidrem1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가잔량2
		'offerrem2' : 'long',
		# 매수호가잔량2
		'bidrem2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가잔량3
		'offerrem3' : 'long',
		# 매수호가잔량3
		'bidrem3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가잔량4
		'offerrem4' : 'long',
		# 매수호가잔량4
		'bidrem4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가잔량5
		'offerrem5' : 'long',
		# 매수호가잔량5
		'bidrem5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가잔량6
		'offerrem6' : 'long',
		# 매수호가잔량6
		'bidrem6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가잔량7
		'offerrem7' : 'long',
		# 매수호가잔량7
		'bidrem7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가잔량8
		'offerrem8' : 'long',
		# 매수호가잔량8
		'bidrem8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가잔량9
		'offerrem9' : 'long',
		# 매수호가잔량9
		'bidrem9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가잔량10
		'offerrem10' : 'long',
		# 매수호가잔량10
		'bidrem10' : 'long',
		# 총매도호가잔량
		'totofferrem' : 'long',
		# 총매수호가잔량
		'totbidrem' : 'long',
		# 동시호가구분
		'donsigubun' : 'char',
		# 배분적용구분
		'alloc_gubun' : 'char'
	}
}

# 시간대별투자자매매추이(BMT)
db_outblock_subscription_BMT = {
	'OutBlock' : {
		# 수신시간
		'tjjtime' : 'char',
		# 투자자코드1(개인)
		'tjjcode1' : 'char',
		# 매수 거래량1
		'msvolume1' : 'long',
		# 매도 거래량1
		'mdvolume1' : 'long',
		# 거래량 순매수1
		'msvol1' : 'long',
		# 매수 거래대금1
		'msvalue1' : 'long',
		# 매도 거래대금1
		'mdvalue1' : 'long',
		# 거래대금 순매수1
		'msval1' : 'long',
		# 투자자코드2(외국인)
		'tjjcode2' : 'char',
		# 매수 거래량2
		'msvolume2' : 'long',
		# 매도 거래량2
		'mdvolume2' : 'long',
		# 거래량 순매수2
		'msvol2' : 'long',
		# 매수 거래대금2
		'msvalue2' : 'long',
		# 매도 거래대금2
		'mdvalue2' : 'long',
		# 거래대금 순매수2
		'msval2' : 'long',
		# 투자자코드3(기관계)
		'tjjcode3' : 'char',
		# 매수 거래량3
		'msvolume3' : 'long',
		# 매도 거래량3
		'mdvolume3' : 'long',
		# 거래량 순매수3
		'msvol3' : 'long',
		# 매수 거래대금3
		'msvalue3' : 'long',
		# 매도 거래대금3
		'mdvalue3' : 'long',
		# 거래대금 순매수3
		'msval3' : 'long',
		# 투자자코드4(증권)
		'tjjcode4' : 'char',
		# 매수 거래량4
		'msvolume4' : 'long',
		# 매도 거래량4
		'mdvolume4' : 'long',
		# 거래량 순매수4
		'msvol4' : 'long',
		# 매수 거래대금4
		'msvalue4' : 'long',
		# 매도 거래대금4
		'mdvalue4' : 'long',
		# 거래대금 순매수4
		'msval4' : 'long',
		# 투자자코드5(투신)
		'tjjcode5' : 'char',
		# 매수 거래량5
		'msvolume5' : 'long',
		# 매도 거래량5
		'mdvolume5' : 'long',
		# 거래량 순매수5
		'msvol5' : 'long',
		# 매수 거래대금5
		'msvalue5' : 'long',
		# 매도 거래대금5
		'mdvalue5' : 'long',
		# 거래대금 순매수5
		'msval5' : 'long',
		# 투자자코드6(은행)
		'tjjcode6' : 'char',
		# 매수 거래량6
		'msvolume6' : 'long',
		# 매도 거래량6
		'mdvolume6' : 'long',
		# 거래량 순매수6
		'msvol6' : 'long',
		# 매수 거래대금6
		'msvalue6' : 'long',
		# 매도 거래대금6
		'mdvalue6' : 'long',
		# 거래대금 순매수6
		'msval6' : 'long',
		# 투자자코드7(보험)
		'tjjcode7' : 'char',
		# 매수 거래량7
		'msvolume7' : 'long',
		# 매도 거래량7
		'mdvolume7' : 'long',
		# 거래량 순매수7
		'msvol7' : 'long',
		# 매수 거래대금7
		'msvalue7' : 'long',
		# 매도 거래대금7
		'mdvalue7' : 'long',
		# 거래대금 순매수7
		'msval7' : 'long',
		# 투자자코드8(종금)
		'tjjcode8' : 'char',
		# 매수 거래량8
		'msvolume8' : 'long',
		# 매도 거래량8
		'mdvolume8' : 'long',
		# 거래량 순매수8
		'msvol8' : 'long',
		# 매수 거래대금8
		'msvalue8' : 'long',
		# 매도 거래대금8
		'mdvalue8' : 'long',
		# 거래대금 순매수8
		'msval8' : 'long',
		# 투자자코드9(기금)
		'tjjcode9' : 'char',
		# 매수 거래량9
		'msvolume9' : 'long',
		# 매도 거래량9
		'mdvolume9' : 'long',
		# 거래량 순매수9
		'msvol9' : 'long',
		# 매수 거래대금9
		'msvalue9' : 'long',
		# 매도 거래대금9
		'mdvalue9' : 'long',
		# 거래대금 순매수9
		'msval9' : 'long',
		# 투자자코드10(선물업자)
		'tjjcode10' : 'char',
		# 매수 거래량10
		'msvolume10' : 'long',
		# 매도 거래량10
		'mdvolume10' : 'long',
		# 거래량 순매수10
		'msvol10' : 'long',
		# 매수 거래대금10
		'msvalue10' : 'long',
		# 매도 거래대금10
		'mdvalue10' : 'long',
		# 거래대금 순매수10
		'msval10' : 'long',
		# 투자자코드11(기타)
		'tjjcode11' : 'char',
		# 매수 거래량11
		'msvolume11' : 'long',
		# 매도 거래량11
		'mdvolume11' : 'long',
		# 거래량 순매수11
		'msvol11' : 'long',
		# 매수 거래대금11
		'msvalue11' : 'long',
		# 매도 거래대금11
		'mdvalue11' : 'long',
		# 거래대금 순매수11
		'msval11' : 'long',
		# 업종코드
		'upcode' : 'char',
		# 투자자코드0(사모펀드)
		'tjjcode0' : 'char',
		# 매수 거래량0
		'msvolume0' : 'long',
		# 매도 거래량0
		'mdvolume0' : 'long',
		# 거래량 순매수0
		'msvol0' : 'long',
		# 매수 거래대금0
		'msvalue0' : 'long',
		# 매도 거래대금0
		'mdvalue0' : 'long',
		# 거래대금 순매수0
		'msval0' : 'long'
	}
}

# 업종별투자자별매매현황(BM)
db_outblock_subscription_BM_ = {
	'OutBlock' : {
		# 투자자코드
		'tjjcode' : 'char',
		# 수신시간
		'tjjtime' : 'char',
		# 매수 거래량
		'msvolume' : 'long',
		# 매도 거래량
		'mdvolume' : 'long',
		# 거래량 순매수
		'msvol' : 'long',
		# 거래량 순매수 직전대비
		'p_msvol' : 'long',
		# 매수 거래대금
		'msvalue' : 'long',
		# 매도 거래대금
		'mdvalue' : 'long',
		# 거래대금 순매수
		'msval' : 'long',
		# 거래대금 순매수 직전대비
		'p_msval' : 'long',
		# 업종코드
		'upcode' : 'char'
	}
}

# 선물주문체결
db_outblock_subscription_C01 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 일련번호
		'seq' : 'long',
		# trcode
		'trcode' : 'char',
		# 매칭그룹번호
		'megrpno' : 'char',
		# 보드ID
		'boardid' : 'char',
		# 회원번호
		'memberno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 주문번호
		'ordno' : 'char',
		# 원주문번호
		'ordordno' : 'char',
		# 종목코드
		'expcode' : 'char',
		# 약정번호
		'yakseq' : 'char',
		# 체결가격
		'cheprice' : 'float',
		# 체결수량
		'chevol' : 'long',
		# 세션ID
		'sessionid' : 'char',
		# 체결일자
		'chedate' : 'char',
		# 체결시각
		'chetime' : 'char',
		# 최근월체결가격
		'spdprc1' : 'float',
		# 차근월체결가격
		'spdprc2' : 'float',
		# 매도수구분
		'dosugb' : 'char',
		# 계좌번호1
		'accno1' : 'char',
		# 시장조성호가구분
		'sihogagb' : 'char',
		# 위탁사번호
		'jakino' : 'char',
		# 대용주권계좌번호
		'daeyong' : 'char',
		# mem_filler
		'mem_filler' : 'char',
		# mem_accno
		'mem_accno' : 'char',
		# mem_filler1
		'mem_filler' : 'char'
	}
}

# 선물옵션 CME 매매거래현황
db_outblock_query_CCEAQ01100 = {
	'CCEAQ01100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 정렬순서구분
		'StnlnSeqTp' : 'char'
	},
	'CCEAQ01100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 매매손익금액
		'BnsplAmt' : 'long',
		# 선물옵션약정금액
		'FnoCtrctAmt' : 'long',
		# 수수료합계금액
		'CmsnAmtSumAmt' : 'long'
	},
	'CCEAQ01100OutBlock3' : [
		{
			# 매매일
			'BnsDt' : 'char',
			# 주문번호
			'OrdNo' : 'long',
			# 약정번호
			'CtrctNo' : 'long',
			# 체결번호
			'ExecNo' : 'long',
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 당초약정지수체결가
			'BgnCtrctIdxExecPrc' : 'double',
			# 당초금액
			'BgnAmt' : 'long',
			# 약정수량
			'CtrctQty' : 'long',
			# 체결가
			'ExecPrc' : 'double',
			# 약정금액
			'CtrctAmt' : 'long',
			# 수수료금액
			'CmsnAmt' : 'long',
			# 매매손익금액
			'BnsplAmt' : 'long'
		}
	]
}

# 선물옵션 CME 주문체결내역조회
db_outblock_query_CCEAQ06000 = {
	'CCEAQ06000OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 선택입력구분
		'ChoicInptTpCode' : 'char',
		# 지점번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 선물옵션분류코드
		'FnoClssCode' : 'char',
		# 상품군코드
		'PrdgrpCode' : 'char',
		# 체결구분
		'PrdtExecTpCode' : 'char',
		# 선물옵션거래유형코드
		'FnoTrdPtnCode' : 'char',
		# 시작주문번호2
		'SrtOrdNo2' : 'long',
		# 종료번호
		'EndNo' : 'long',
		# 정렬순서구분
		'StnlnSeqTp' : 'char'
	},
	'CCEAQ06000OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 선물주문수량
		'FutsOrdQty' : 'long',
		# 선물체결수량
		'FutsExecQty' : 'long'
	},
	'CCEAQ06000OutBlock3' : [
		{
			# 계좌번호1
			'AcntNo1' : 'char',
			# 주문일
			'OrdDt' : 'char',
			# 주문번호
			'OrdNo' : 'long',
			# 원주문번호
			'OrgOrdNo' : 'long',
			# 주문시각
			'OrdTime' : 'char',
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 정정취소구분명
			'MrcTpNm' : 'char',
			# 선물옵션호가유형코드
			'FnoOrdprcPtnCode' : 'char',
			# 선물옵션호가유형명
			'FnoOrdprcPtnNm' : 'char',
			# 주문가
			'OrdPrc' : 'double',
			# 주문수량
			'OrdQty' : 'long',
			# 주문구분명
			'OrdTpNm' : 'char',
			# 체결구분명
			'ExecTpNm' : 'char',
			# 체결가
			'ExecPrc' : 'double',
			# 체결수량
			'ExecQty' : 'long',
			# 약정시각
			'CtrctTime' : 'char',
			# 약정번호
			'CtrctNo' : 'long',
			# 체결번호
			'ExecNo' : 'long',
			# 매매손익금액
			'BnsplAmt' : 'long',
			# 미체결수량
			'UnercQty' : 'long',
			# 사용자ID
			'UserId' : 'char',
			# 통신매체코드
			'CommdaCode' : 'char',
			# 통신매체코드명
			'CommdaCodeNm' : 'char',
			# IP주소
			'IpAddr' : 'char',
			# 거래유형구분
			'TrdPtnTpNm' : 'char',
			# 그룹ID
			'GrpId' : 'char'
		}
	]
}

# 선물옵션 CME 주문가능 수량/금액 조회
db_outblock_query_CCEAQ10100 = {
	'CCEAQ10100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회구분
		'QryTp' : 'char',
		# 주문금액
		'OrdAmt' : 'long',
		# 비율값
		'RatVal' : 'double',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 주문가
		'OrdPrc' : 'double',
		# 선물옵션호가유형코드
		'FnoOrdprcPtnCode' : 'char'
	},
	'CCEAQ10100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 조회일
		'QryDt' : 'char',
		# 현재가
		'NowPrc' : 'double',
		# 주문가능수량
		'OrdAbleQty' : 'long',
		# 신규주문가능수량
		'NewOrdAbleQty' : 'long',
		# 청산주문가능수량
		'LqdtOrdAbleQty' : 'long',
		# 사용예정증거금액
		'UsePreargMgn' : 'long',
		# 사용예정현금증거금액
		'UsePreargMnyMgn' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long'
	}
}

# 선물옵션 CME 계좌잔고 및 평가현황
db_outblock_query_CCEAQ50600 = {
	'CCEAQ50600OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 잔고평가구분
		'BalEvalTp' : 'char',
		# 선물가격평가구분
		'FutsPrcEvalTp' : 'char'
	},
	'CCEAQ50600OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 평가예탁금총액
		'EvalDpsamtTotamt' : 'long',
		# 현금평가예탁금액
		'MnyEvalDpstgAmt' : 'long',
		# 예탁금총액
		'DpsamtTotamt' : 'long',
		# 예탁현금
		'DpstgMny' : 'long',
		# 인출가능총금액
		'PsnOutAbleTotAmt' : 'long',
		# 인출가능현금액
		'PsnOutAbleCurAmt' : 'long',
		# 주문가능총금액
		'OrdAbleTotAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 위탁증거금총액
		'CsgnMgnTotamt' : 'long',
		# 현금위탁증거금액
		'MnyCsgnMgn' : 'long',
		# 추가증거금총액
		'AddMgnTotamt' : 'long',
		# 현금추가증거금액
		'MnyAddMgn' : 'long',
		# 수수료
		'CmsnAmt' : 'long',
		# 선물평가손익금액
		'FutsEvalPnlAmt' : 'long',
		# 옵션평가손익금액
		'OptEvalPnlAmt' : 'long',
		# 옵션평가금액
		'OptEvalAmt' : 'long',
		# 옵션매매손익금액
		'OptBnsplAmt' : 'long',
		# 선물정산차금
		'FutsAdjstDfamt' : 'long',
		# 총손익금액
		'TotPnlAmt' : 'long',
		# 순손익금액
		'NetPnlAmt' : 'long',
		# 총평가금액
		'TotEvalAmt' : 'long',
		# 입금금액
		'MnyinAmt' : 'long',
		# 출금금액
		'MnyoutAmt' : 'long'
	},
	'CCEAQ50600OutBlock3' : [
		{
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 미결제수량
			'UnsttQty' : 'long',
			# 평균가
			'FnoAvrPrc' : 'double',
			# 현재가
			'NowPrc' : 'double',
			# 대비가
			'CmpPrc' : 'double',
			# 평가손익
			'EvalPnl' : 'long',
			# 손익률
			'PnlRat' : 'double',
			# 평가금액
			'EvalAmt' : 'long'
		}
	]
}

# CME 정상주문
db_outblock_query_CCEAT00100 = {
	'CCEAT00100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 선물옵션주문유형코드
		'FnoOrdPtnCode' : 'char',
		# 선물옵션호가유형코드
		'FnoOrdprcPtnCode' : 'char',
		# 선물옵션거래유형코드
		'FnoTrdPtnCode' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 주문수량
		'OrdQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 협의매매완료시각
		'DscusBnsCmpltTime' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문일련번호
		'OrdSeqno' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 항목번호
		'ItemNo' : 'long',
		# 운용지시번호
		'OpDrtnNo' : 'char',
		# 관리사원번호
		'MgempNo' : 'char',
		# 펀드ID
		'FundId' : 'char',
		# 펀드주문번호
		'FundOrdNo' : 'long'
	},
	'CCEAT00100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금
		'OrdMgn' : 'long',
		# 현금주문증거금
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# CME 정정주문
db_outblock_query_CCEAT00200 = {
	'CCEAT00200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 선물옵션주문유형코드
		'FnoOrdPtnCode' : 'char',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 선물옵션호가유형코드
		'FnoOrdprcPtnCode' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 정정수량
		'MdfyQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 협의매매완료시각
		'DscusBnsCmpltTime' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문일련번호
		'OrdSeqno' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long',
		# 관리사원번호
		'MgempNo' : 'char',
		# 펀드ID
		'FundId' : 'char',
		# 펀드원주문번호
		'FundOrgOrdNo' : 'long',
		# 펀드주문번호
		'FundOrdNo' : 'long'
	},
	'CCEAT00200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금액
		'OrdMgn' : 'long',
		# 현금주문증거금액
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# CME 취소주문
db_outblock_query_CCEAT00300 = {
	'CCEAT00300OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 선물옵션주문유형코드
		'FnoOrdPtnCode' : 'char',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 취소수량
		'CancQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 협의매매완료시각
		'DscusBnsCmpltTime' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문일련번호
		'OrdSeqno' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long',
		# 관리사원번호
		'MgempNo' : 'char',
		# 펀드ID
		'FundId' : 'char',
		# 펀드원주문번호
		'FundOrgOrdNo' : 'long',
		# 펀드주문번호
		'FundOrdNo' : 'long'
	},
	'CCEAT00300OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금액
		'OrdMgn' : 'long',
		# 현금주문증거금액
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 선물옵션 CME 예탁금증거금조회
db_outblock_query_CCEBQ10500 = {
	'CCEBQ10500OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char'
	},
	'CCEBQ10500OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 예탁금총액
		'DpsamtTotamt' : 'long',
		# 예수금
		'Dps' : 'long',
		# 대용금액
		'SubstAmt' : 'long',
		# 충당예탁금총액
		'FilupDpsamtTotamt' : 'long',
		# 충당예수금
		'FilupDps' : 'long',
		# 선물손익금액
		'FutsPnlAmt' : 'long',
		# 인출가능금액
		'WthdwAbleAmt' : 'long',
		# 인출가능현금액
		'PsnOutAbleCurAmt' : 'long',
		# 인출가능대용금액
		'PsnOutAbleSubstAmt' : 'long',
		# 증거금액
		'Mgn' : 'long',
		# 현금증거금액
		'MnyMgn' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 추가증거금액
		'AddMgn' : 'long',
		# 현금추가증거금액
		'MnyAddMgn' : 'long',
		# 금전일수표입금액
		'AmtPrdayChckInAmt' : 'long',
		# 선물옵션전일대용매도금액
		'FnoPrdaySubstSellAmt' : 'long',
		# 선물옵션금일대용매도금액
		'FnoCrdaySubstSellAmt' : 'long',
		# 선물옵션전일가입금액
		'FnoPrdayFdamt' : 'long',
		# 선물옵션금일가입금액
		'FnoCrdayFdamt' : 'long',
		# 외화대용금액
		'FcurrSubstAmt' : 'long',
		# 선물옵션계좌사후증거금명
		'FnoAcntAfmgnNm' : 'char'
	},
	'CCEBQ10500OutBlock3' : [
		{
			# 상품군코드명
			'PdGrpCodeNm' : 'char',
			# 순위험증거금액
			'NetRiskMgn' : 'long',
			# 가격증거금액
			'PrcMgn' : 'long',
			# 스프레드증거금액
			'SprdMgn' : 'long',
			# 가격변동증거금액
			'PrcFlctMgn' : 'long',
			# 최소증거금액
			'MinMgn' : 'long',
			# 주문증거금액
			'OrdMgn' : 'long',
			# 옵션순매수금액
			'OptNetBuyAmt' : 'long',
			# 위탁증거금액
			'CsgnMgn' : 'long',
			# 유지증거금액
			'MaintMgn' : 'long',
			# 선물매수체결금액
			'FutsBuyExecAmt' : 'long',
			# 선물매도체결금액
			'FutsSellExecAmt' : 'long',
			# 옵션매수체결금액
			'OptBuyExecAmt' : 'long',
			# 옵션매도체결금액
			'OptSellExecAmt' : 'long',
			# 선물손익금액
			'FutsPnlAmt' : 'long',
			# 총위험위탁증거금
			'TotRiskCsgnMgn' : 'long',
			# 인수도위탁증거금
			'UndCsgnMgn' : 'long',
			# 증거금감면금액
			'MgnRdctAmt' : 'long'
		}
	]
}

# 상품선물실시간상하한가(D0)
db_outblock_subscription_CD0 = {
	'OutBlock' : {
		# 접속매매여부
		'gubun' : 'char',
		# 실시간가격제한여부
		'dy_gubun' : 'char',
		# 실시간상한가
		'dy_uplmtprice' : 'float',
		# 실시간하한가
		'dy_dnlmtprice' : 'float',
		# 단축코드
		'futcode' : 'char'
	}
}

# 계좌 거래내역
db_outblock_query_CDPCQ04700 = {
	'CDPCQ04700OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 조회구분
		'QryTp' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 시작번호
		'SrtNo' : 'long',
		# 상품유형코드
		'PdptnCode' : 'char',
		# 종목대분류코드
		'IsuLgclssCode' : 'char',
		# 종목번호
		'IsuNo' : 'char'
	},
	'CDPCQ04700OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char'
	},
	'CDPCQ04700OutBlock3' : [
		{
			# 계좌번호
			'AcntNo' : 'char',
			# 거래일자
			'TrdDt' : 'char',
			# 거래번호
			'TrdNo' : 'long',
			# 구분코드명
			'TpCodeNm' : 'char',
			# 적요번호
			'SmryNo' : 'char',
			# 적요명
			'SmryNm' : 'char',
			# 취소구분
			'CancTpNm' : 'char',
			# 거래수량
			'TrdQty' : 'long',
			# 거래세
			'Trtax' : 'long',
			# 외화정산금액
			'FcurrAdjstAmt' : 'double',
			# 정산금액
			'AdjstAmt' : 'long',
			# 연체합
			'OvdSum' : 'long',
			# 예수금전잔금액
			'DpsBfbalAmt' : 'long',
			# 매도담보상환금
			'SellPldgRfundAmt' : 'long',
			# 예탁담보대출전잔금액
			'DpspdgLoanBfbalAmt' : 'long',
			# 거래매체명
			'TrdmdaNm' : 'char',
			# 원거래번호
			'OrgTrdNo' : 'long',
			# 종목명
			'IsuNm' : 'char',
			# 거래단가
			'TrdUprc' : 'double',
			# 수수료
			'CmsnAmt' : 'long',
			# 외화수수료금액
			'FcurrCmsnAmt' : 'double',
			# 상환차이금액
			'RfundDiffAmt' : 'long',
			# 변제금합계
			'RepayAmtSum' : 'long',
			# 유가증권금잔수량
			'SecCrbalQty' : 'long',
			# 매도대금담보대출상환이자금액
			'CslLoanRfundIntrstAmt' : 'long',
			# 예탁담보대출금잔금액
			'DpspdgLoanCrbalAmt' : 'long',
			# 처리시각
			'TrxTime' : 'char',
			# 출납번호
			'Inouno' : 'long',
			# 종목번호
			'IsuNo' : 'char',
			# 거래금액
			'TrdAmt' : 'long',
			# 수표금액
			'ChckAmt' : 'long',
			# 세금합계금액
			'TaxSumAmt' : 'long',
			# 외화세금합계금액
			'FcurrTaxSumAmt' : 'double',
			# 이자이용료
			'IntrstUtlfee' : 'long',
			# 배당금액
			'MnyDvdAmt' : 'long',
			# 미수발생금액
			'RcvblOcrAmt' : 'long',
			# 처리지점번호
			'TrxBrnNo' : 'char',
			# 처리지점명
			'TrxBrnNm' : 'char',
			# 예탁담보대출금액
			'DpspdgLoanAmt' : 'long',
			# 예탁담보대출상환금액
			'DpspdgLoanRfundAmt' : 'long',
			# 기준가
			'BasePrc' : 'double',
			# 예수금금잔금액
			'DpsCrbalAmt' : 'long',
			# 과표
			'BoaAmt' : 'long',
			# 출금가능금액
			'MnyoutAbleAmt' : 'long',
			# 수익증권담보대출발생금
			'BcrLoanOcrAmt' : 'long',
			# 수익증권담보대출전잔금
			'BcrLoanBfbalAmt' : 'long',
			# 매매기준가
			'BnsBasePrc' : 'double',
			# 과세기준가
			'TaxchrBasePrc' : 'double',
			# 거래좌수
			'TrdUnit' : 'long',
			# 잔고좌수
			'BalUnit' : 'long',
			# 제세금
			'EvrTax' : 'long',
			# 평가금액
			'EvalAmt' : 'long',
			# 수익증권담보대출상환금
			'BcrLoanRfundAmt' : 'long',
			# 수익증권담보대출금잔금
			'BcrLoanCrbalAmt' : 'long',
			# 추가증거금발생총액
			'AddMgnOcrTotamt' : 'long',
			# 추가현금증거금발생금액
			'AddMnyMgnOcrAmt' : 'long',
			# 추가증거금납부총액
			'AddMgnDfryTotamt' : 'long',
			# 추가현금증거금납부금액
			'AddMnyMgnDfryAmt' : 'long',
			# 매매손익금액
			'BnsplAmt' : 'long',
			# 소득세
			'Ictax' : 'long',
			# 주민세
			'Ihtax' : 'long',
			# 대출일
			'LoanDt' : 'char',
			# 통화코드
			'CrcyCode' : 'char',
			# 외화금액
			'FcurrAmt' : 'double',
			# 외화거래금액
			'FcurrTrdAmt' : 'double',
			# 외화예수금
			'FcurrDps' : 'double',
			# 외화예수금전잔금액
			'FcurrDpsBfbalAmt' : 'double',
			# 상대계좌명
			'OppAcntNm' : 'char',
			# 상대계좌번호
			'OppAcntNo' : 'char',
			# 대출상환금액
			'LoanRfundAmt' : 'long',
			# 대출이자금액
			'LoanIntrstAmt' : 'long',
			# 의뢰인명
			'AskpsnNm' : 'char',
			# 주문일자
			'OrdDt' : 'char',
			# 거래환율
			'TrdXchrat' : 'double',
			# 감면수수료
			'RdctCmsn' : 'double',
			# 외화인지세
			'FcurrStmpTx' : 'double',
			# 외화전자금융거래세
			'FcurrElecfnTrtax' : 'double',
			# 외화증권거래세
			'FcstckTrtax' : 'double'
		}
	],
	'CDPCQ04700OutBlock4' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 손익합계금액
		'PnlSumAmt' : 'long',
		# 약정누계
		'CtrctAsm' : 'long',
		# 수수료합계금액
		'CmsnAmtSumAmt' : 'long'
	},
	'CDPCQ04700OutBlock5' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 입금금액
		'MnyinAmt' : 'long',
		# 입고금액
		'SecinAmt' : 'long',
		# 출금금액
		'MnyoutAmt' : 'long',
		# 출고금액
		'SecoutAmt' : 'long',
		# 차이금액
		'DiffAmt' : 'long',
		# 차이금액0
		'DiffAmt0' : 'long',
		# 매도수량
		'SellQty' : 'long',
		# 매도금액
		'SellAmt' : 'long',
		# 매도수수료
		'SellCmsn' : 'long',
		# 제세금
		'EvrTax' : 'long',
		# 외화매도정산금액
		'FcurrSellAdjstAmt' : 'double',
		# 매수수량
		'BuyQty' : 'long',
		# 매수금액
		'BuyAmt' : 'long',
		# 매수수수료
		'BuyCmsn' : 'long',
		# 체결세금
		'ExecTax' : 'long',
		# 외화매수정산금액
		'FcurrBuyAdjstAmt' : 'double'
	}
}

# 유렉스 주문체결내역조회
db_outblock_query_CEXAQ21100 = {
	'CEXAQ21100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 선택입력구분
		'ChoicInptTpCode' : 'char',
		# 지점번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 체결구분
		'PrdtExecTpCode' : 'char',
		# 정렬순서구분
		'StnlnSeqTp' : 'char'
	},
	'CEXAQ21100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 주문수량
		'OrdQty' : 'long',
		# 체결수량
		'ExecQty' : 'long'
	},
	'CEXAQ21100OutBlock3' : [
		{
			# 계좌번호1
			'AcntNo1' : 'char',
			# 주문일
			'OrdDt' : 'char',
			# 주문번호
			'OrdNo' : 'long',
			# 원주문번호
			'OrgOrdNo' : 'long',
			# 주문시각
			'OrdTime' : 'char',
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 정정취소구분명
			'MrcTpNm' : 'char',
			# 유렉스가격조건구분코드
			'ErxPrcCndiTpCode' : 'char',
			# 선물옵션호가유형명
			'FnoOrdprcPtnNm' : 'char',
			# 주문조건가격
			'OrdCndiPrc' : 'double',
			# 주문가
			'OrdPrc' : 'double',
			# 주문수량
			'OrdQty' : 'long',
			# 주문구분명
			'OrdTpNm' : 'char',
			# 체결가
			'ExecPrc' : 'double',
			# 체결수량
			'ExecQty' : 'long',
			# 미체결수량
			'UnercQty' : 'long',
			# 통신매체코드
			'CommdaCode' : 'char',
			# 통신매체명
			'CommdaNm' : 'char'
		}
	]
}

# 유렉스 주문가능 수량/금액 조회
db_outblock_query_CEXAQ21200 = {
	'CEXAQ21200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회구분
		'QryTp' : 'char',
		# 주문금액
		'OrdAmt' : 'long',
		# 비율값
		'RatVal' : 'double',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 주문가
		'OrdPrc' : 'double',
		# 유렉스가격조건구분코드
		'ErxPrcCndiTpCode' : 'char'
	},
	'CEXAQ21200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 조회일
		'QryDt' : 'char',
		# 현재가
		'NowPrc' : 'double',
		# 주문가능수량
		'OrdAbleQty' : 'long',
		# 신규주문가능수량
		'NewOrdAbleQty' : 'long',
		# 청산주문가능수량
		'LqdtOrdAbleQty' : 'long',
		# 사용예정증거금액
		'UsePreargMgn' : 'long',
		# 사용예정현금증거금액
		'UsePreargMnyMgn' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long'
	}
}

# 유렉스 야간장잔고및 평가현황
db_outblock_query_CEXAQ31100 = {
	'CEXAQ31100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 종목코드
		'IsuCode' : 'char',
		# 잔고평가구분
		'BalEvalTp' : 'char',
		# 선물가격평가구분
		'FutsPrcEvalTp' : 'char'
	},
	'CEXAQ31100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 매매손익금액
		'BnsplAmt' : 'long',
		# 정산차금
		'AdjstDfamt' : 'long',
		# 총평가금액
		'TotEvalAmt' : 'long',
		# 총손익금액
		'TotPnlAmt' : 'long'
	},
	'CEXAQ31100OutBlock3' : [
		{
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 미결제수량
			'UnsttQty' : 'long',
			# 청산가능수량
			'LqdtAbleQty' : 'long',
			# 평균가
			'FnoAvrPrc' : 'double',
			# 기준가
			'BasePrc' : 'double',
			# 현재가
			'NowPrc' : 'double',
			# 대비가
			'CmpPrc' : 'double',
			# 평가금액
			'EvalAmt' : 'long',
			# 평가손익
			'EvalPnl' : 'long',
			# 손익률
			'PnlRat' : 'double',
			# 미결제금액
			'UnsttAmt' : 'long',
			# 매매손익금액
			'BnsplAmt' : 'long'
		}
	]
}

# 유렉스 예탁금 및 통합잔고조회
db_outblock_query_CEXAQ31200 = {
	'CEXAQ31200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 잔고평가구분
		'BalEvalTp' : 'char',
		# 선물가격평가구분
		'FutsPrcEvalTp' : 'char'
	},
	'CEXAQ31200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 평가예탁금총액
		'EvalDpsamtTotamt' : 'long',
		# 현금평가예탁금액
		'MnyEvalDpstgAmt' : 'long',
		# 예탁금총액
		'DpsamtTotamt' : 'long',
		# 예탁현금
		'DpstgMny' : 'long',
		# 인출가능총금액
		'PsnOutAbleTotAmt' : 'long',
		# 인출가능현금액
		'PsnOutAbleCurAmt' : 'long',
		# 주문가능총금액
		'OrdAbleTotAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 위탁증거금총액
		'CsgnMgnTotamt' : 'long',
		# 현금위탁증거금액
		'MnyCsgnMgn' : 'long',
		# 추가증거금총액
		'AddMgnTotamt' : 'long',
		# 현금추가증거금액
		'MnyAddMgn' : 'long',
		# 수수료
		'CmsnAmt' : 'long',
		# 선물평가손익금액
		'FutsEvalPnlAmt' : 'long',
		# 옵션평가손익금액
		'OptEvalPnlAmt' : 'long',
		# 옵션평가금액
		'OptEvalAmt' : 'long',
		# 옵션매매손익금액
		'OptBnsplAmt' : 'long',
		# 선물정산차금
		'FutsAdjstDfamt' : 'long',
		# 총손익금액
		'TotPnlAmt' : 'long',
		# 순손익금액
		'NetPnlAmt' : 'long',
		# 총평가금액
		'TotEvalAmt' : 'long',
		# 입금금액
		'MnyinAmt' : 'long',
		# 출금금액
		'MnyoutAmt' : 'long',
		# 선물수수료금액
		'FutsCmsnAmt' : 'long'
	},
	'CEXAQ31200OutBlock3' : [
		{
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 미결제수량
			'UnsttQty' : 'long',
			# 평균가
			'FnoAvrPrc' : 'double',
			# 현재가
			'NowPrc' : 'double',
			# 대비가
			'CmpPrc' : 'double',
			# 평가손익
			'EvalPnl' : 'long',
			# 손익률
			'PnlRat' : 'double',
			# 평가금액
			'EvalAmt' : 'long',
			# 청산가능수량
			'LqdtAbleQty' : 'long'
		}
	]
}

# 유렉스 매수/매도주문
db_outblock_query_CEXAT11100 = {
	'CEXAT11100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 유렉스가격조건구분코드
		'ErxPrcCndiTpCode' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 주문수량
		'OrdQty' : 'long',
		# 주문조건가격
		'OrdCndiPrc' : 'double',
		# 통신매체코드
		'CommdaCode' : 'char'
	},
	'CEXAT11100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금
		'OrdMgn' : 'long',
		# 현금주문증거금
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 유렉스 정정주문
db_outblock_query_CEXAT11200 = {
	'CEXAT11200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분코드
		'BnsTpCode' : 'char',
		# 유렉스가격조건구분코드
		'ErxPrcCndiTpCode' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 정정수량
		'MdfyQty' : 'long',
		# 주문조건가격
		'OrdCndiPrc' : 'double',
		# 통신매체코드
		'CommdaCode' : 'char'
	},
	'CEXAT11200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금액
		'OrdMgn' : 'long',
		# 현금주문증거금액
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 유렉스 취소주문
db_outblock_query_CEXAT11300 = {
	'CEXAT11300OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 취소수량
		'CancQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char'
	},
	'CEXAT11300OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금액
		'OrdMgn' : 'long',
		# 현금주문증거금액
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 선물옵션 계좌주문체결내역조회
db_outblock_query_CFOAQ00600 = {
	'CFOAQ00600OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 선물옵션분류코드
		'FnoClssCode' : 'char',
		# 상품군코드
		'PrdgrpCode' : 'char',
		# 체결구분
		'PrdtExecTpCode' : 'char',
		# 정렬순서구분
		'StnlnSeqTp' : 'char',
		# 통신매체코드
		'CommdaCode' : 'char'
	},
	'CFOAQ00600OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 선물주문수량
		'FutsOrdQty' : 'long',
		# 선물체결수량
		'FutsExecQty' : 'long',
		# 옵션주문수량
		'OptOrdQty' : 'long',
		# 옵션체결수량
		'OptExecQty' : 'long'
	},
	'CFOAQ00600OutBlock3' : [
		{
			# 주문일
			'OrdDt' : 'char',
			# 주문번호
			'OrdNo' : 'long',
			# 원주문번호
			'OrgOrdNo' : 'long',
			# 주문시각
			'OrdTime' : 'char',
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 정정취소구분명
			'MrcTpNm' : 'char',
			# 선물옵션호가유형코드
			'FnoOrdprcPtnCode' : 'char',
			# 선물옵션호가유형명
			'FnoOrdprcPtnNm' : 'char',
			# 주문가
			'OrdPrc' : 'double',
			# 주문수량
			'OrdQty' : 'long',
			# 주문구분명
			'OrdTpNm' : 'char',
			# 체결구분명
			'ExecTpNm' : 'char',
			# 체결가
			'ExecPrc' : 'double',
			# 체결수량
			'ExecQty' : 'long',
			# 약정시각
			'CtrctTime' : 'char',
			# 약정번호
			'CtrctNo' : 'long',
			# 체결번호
			'ExecNo' : 'long',
			# 매매손익금액
			'BnsplAmt' : 'long',
			# 미체결수량
			'UnercQty' : 'long',
			# 사용자ID
			'UserId' : 'char',
			# 통신매체코드
			'CommdaCode' : 'char',
			# 통신매체코드명
			'CommdaCodeNm' : 'char'
		}
	]
}

# 선물옵션 주문가능수량조회
db_outblock_query_CFOAQ10100 = {
	'CFOAQ10100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회구분
		'QryTp' : 'char',
		# 주문금액
		'OrdAmt' : 'long',
		# 비율값
		'RatVal' : 'double',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 주문가
		'OrdPrc' : 'double',
		# 선물옵션호가유형코드
		'FnoOrdprcPtnCode' : 'char'
	},
	'CFOAQ10100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 조회일
		'QryDt' : 'char',
		# 현재가
		'NowPrc' : 'double',
		# 주문가능수량
		'OrdAbleQty' : 'long',
		# 신규주문가능수량
		'NewOrdAbleQty' : 'long',
		# 청산주문가능수량
		'LqdtOrdAbleQty' : 'long',
		# 사용예정증거금액
		'UsePreargMgn' : 'long',
		# 사용예정현금증거금액
		'UsePreargMnyMgn' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long'
	}
}

# 선물옵션 정상주문
db_outblock_query_CFOAT00100 = {
	'CFOAT00100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 선물옵션주문유형코드
		'FnoOrdPtnCode' : 'char',
		# 선물옵션호가유형코드
		'FnoOrdprcPtnCode' : 'char',
		# 선물옵션거래유형코드
		'FnoTrdPtnCode' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 주문수량
		'OrdQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 협의매매완료시각
		'DscusBnsCmpltTime' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문일련번호
		'OrdSeqno' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 항목번호
		'ItemNo' : 'long',
		# 운용지시번호
		'OpDrtnNo' : 'char',
		# 관리사원번호
		'MgempNo' : 'char',
		# 펀드ID
		'FundId' : 'char',
		# 펀드주문번호
		'FundOrdNo' : 'long'
	},
	'CFOAT00100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금
		'OrdMgn' : 'long',
		# 현금주문증거금
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 선물옵션 정정주문
db_outblock_query_CFOAT00200 = {
	'CFOAT00200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 선물옵션주문유형코드
		'FnoOrdPtnCode' : 'char',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 선물옵션호가유형코드
		'FnoOrdprcPtnCode' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 정정수량
		'MdfyQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 협의매매완료시각
		'DscusBnsCmpltTime' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문일련번호
		'OrdSeqno' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long',
		# 관리사원번호
		'MgempNo' : 'char',
		# 펀드ID
		'FundId' : 'char',
		# 펀드원주문번호
		'FundOrgOrdNo' : 'long',
		# 펀드주문번호
		'FundOrdNo' : 'long'
	},
	'CFOAT00200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금액
		'OrdMgn' : 'long',
		# 현금주문증거금액
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 선물옵션 취소주문
db_outblock_query_CFOAT00300 = {
	'CFOAT00300OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 선물옵션종목번호
		'FnoIsuNo' : 'char',
		# 선물옵션주문유형코드
		'FnoOrdPtnCode' : 'char',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 취소수량
		'CancQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 협의매매완료시각
		'DscusBnsCmpltTime' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문일련번호
		'OrdSeqno' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long',
		# 관리사원번호
		'MgempNo' : 'char',
		# 펀드ID
		'FundId' : 'char',
		# 펀드원주문번호
		'FundOrgOrdNo' : 'long',
		# 펀드주문번호
		'FundOrdNo' : 'long'
	},
	'CFOAT00300OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 주문증거금액
		'OrdMgn' : 'long',
		# 현금주문증거금액
		'MnyOrdMgn' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long'
	}
}

# 선물옵션 계좌예탁금증거금조회
db_outblock_query_CFOBQ10500 = {
	'CFOBQ10500OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char'
	},
	'CFOBQ10500OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 예탁금총액
		'DpsamtTotamt' : 'long',
		# 예수금
		'Dps' : 'long',
		# 대용금액
		'SubstAmt' : 'long',
		# 충당예탁금총액
		'FilupDpsamtTotamt' : 'long',
		# 충당예수금
		'FilupDps' : 'long',
		# 선물손익금액
		'FutsPnlAmt' : 'long',
		# 인출가능금액
		'WthdwAbleAmt' : 'long',
		# 인출가능현금액
		'PsnOutAbleCurAmt' : 'long',
		# 인출가능대용금액
		'PsnOutAbleSubstAmt' : 'long',
		# 증거금액
		'Mgn' : 'long',
		# 현금증거금액
		'MnyMgn' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 추가증거금액
		'AddMgn' : 'long',
		# 현금추가증거금액
		'MnyAddMgn' : 'long',
		# 금전일수표입금액
		'AmtPrdayChckInAmt' : 'long',
		# 선물옵션전일대용매도금액
		'FnoPrdaySubstSellAmt' : 'long',
		# 선물옵션금일대용매도금액
		'FnoCrdaySubstSellAmt' : 'long',
		# 선물옵션전일가입금액
		'FnoPrdayFdamt' : 'long',
		# 선물옵션금일가입금액
		'FnoCrdayFdamt' : 'long',
		# 외화대용금액
		'FcurrSubstAmt' : 'long',
		# 선물옵션계좌사후증거금명
		'FnoAcntAfmgnNm' : 'char'
	},
	'CFOBQ10500OutBlock3' : [
		{
			# 상품군코드명
			'PdGrpCodeNm' : 'char',
			# 순위험증거금액
			'NetRiskMgn' : 'long',
			# 가격증거금액
			'PrcMgn' : 'long',
			# 스프레드증거금액
			'SprdMgn' : 'long',
			# 가격변동증거금액
			'PrcFlctMgn' : 'long',
			# 최소증거금액
			'MinMgn' : 'long',
			# 주문증거금액
			'OrdMgn' : 'long',
			# 옵션순매수금액
			'OptNetBuyAmt' : 'long',
			# 위탁증거금액
			'CsgnMgn' : 'long',
			# 유지증거금액
			'MaintMgn' : 'long',
			# 선물매수체결금액
			'FutsBuyExecAmt' : 'long',
			# 선물매도체결금액
			'FutsSellExecAmt' : 'long',
			# 옵션매수체결금액
			'OptBuyExecAmt' : 'long',
			# 옵션매도체결금액
			'OptSellExecAmt' : 'long',
			# 선물손익금액
			'FutsPnlAmt' : 'long',
			# 총위험위탁증거금
			'TotRiskCsgnMgn' : 'long',
			# 인수도위탁증거금
			'UndCsgnMgn' : 'long',
			# 증거금감면금액
			'MgnRdctAmt' : 'long'
		}
	]
}

# 선물옵션 옵션매도시 주문증거금조회
db_outblock_query_CFOBQ10800 = {
	'CFOBQ10800OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 상품군코드
		'PrdgrpClssCode' : 'char',
		# 기초자산코드
		'ClssGrpCode' : 'char',
		# 최근월물구분
		'FstmmTpCode' : 'char'
	},
	'CFOBQ10800OutBlock2' : [
		{
			# 행사가
			'ElwXrcPrc' : 'double',
			# 선물옵션종목번호
			'FnoIsuNo' : 'char',
			# 한글종목명1
			'HanglIsuNm1' : 'char',
			# 구분명1
			'TpNm1' : 'char',
			# 이론가1
			'Thrprc1' : 'double',
			# 기준가1
			'BasePrc1' : 'double',
			# 주문증거금액1
			'OrdMgn1' : 'long',
			# 선물옵션종목번호0
			'FnoIsuNo0' : 'char',
			# 한글종목명2
			'HanglIsuNm2' : 'char',
			# 구분명2
			'TpNm2' : 'char',
			# 이론가2
			'Thrprc2' : 'double',
			# 기준가2
			'BasePrc2' : 'double',
			# 주문증거금액2
			'OrdMgn2' : 'long'
		}
	]
}

# 선물옵션가정산예탁금상세
db_outblock_query_CFOEQ11100 = {
	'CFOEQ11100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 매매일
		'BnsDt' : 'char'
	},
	'CFOEQ11100OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 개장시예탁금총액
		'OpnmkDpsamtTotamt' : 'long',
		# 개장시예수금
		'OpnmkDps' : 'long',
		# 개장시현금미수금
		'OpnmkMnyrclAmt' : 'long',
		# 개장시대용금액
		'OpnmkSubstAmt' : 'long',
		# 총금액
		'TotAmt' : 'long',
		# 예수금
		'Dps' : 'long',
		# 현금미수금액
		'MnyrclAmt' : 'long',
		# 대용지정금액
		'SubstDsgnAmt' : 'long',
		# 위탁증거금액
		'CsgnMgn' : 'long',
		# 현금위탁증거금액
		'MnyCsgnMgn' : 'long',
		# 유지증거금액
		'MaintMgn' : 'long',
		# 현금유지증거금액
		'MnyMaintMgn' : 'long',
		# 출금가능총액
		'OutAbleAmt' : 'long',
		# 출금가능금액
		'MnyoutAbleAmt' : 'long',
		# 출금가능대용
		'SubstOutAbleAmt' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 추가증거금구분
		'AddMgnOcrTpCode' : 'char',
		# 추가증거금액
		'AddMgn' : 'long',
		# 현금추가증거금액
		'MnyAddMgn' : 'long',
		# 익일예탁총액
		'NtdayTotAmt' : 'long',
		# 익일예탁현금
		'NtdayDps' : 'long',
		# 익일미수금
		'NtdayMnyrclAmt' : 'long',
		# 익일예탁대용
		'NtdaySubstAmt' : 'long',
		# 익일위탁증거금
		'NtdayCsgnMgn' : 'long',
		# 익일위탁증거금현금
		'NtdayMnyCsgnMgn' : 'long',
		# 익일유지증거금
		'NtdayMaintMgn' : 'long',
		# 익일유지증거금현금
		'NtdayMnyMaintMgn' : 'long',
		# 익일인출가능금액
		'NtdayOutAbleAmt' : 'long',
		# 익일인출가능금액
		'NtdayMnyoutAbleAmt' : 'long',
		# 익일인출가능대용
		'NtdaySubstOutAbleAmt' : 'long',
		# 익일주문가능금액
		'NtdayOrdAbleAmt' : 'long',
		# 익일주문가능현금
		'NtdayMnyOrdAbleAmt' : 'long',
		# 익일추가증거금구분
		'NtdayAddMgnTp' : 'char',
		# 익일추가증거금
		'NtdayAddMgn' : 'long',
		# 익일추가증거금현금
		'NtdayMnyAddMgn' : 'long',
		# 익일결제금액
		'NtdaySettAmt' : 'long',
		# 평가예탁금총액
		'EvalDpsamtTotamt' : 'long',
		# 현금평가예탁금액
		'MnyEvalDpstgAmt' : 'long',
		# 예탁금이용료지급예정금액
		'DpsamtUtlfeeGivPrergAmt' : 'long',
		# 세금
		'TaxAmt' : 'long',
		# 위탁증거금 비율
		'CsgnMgnrat' : 'double',
		# 위탁증거금현금비율
		'CsgnMnyMgnrat' : 'double',
		# 예탁총액부족금액(위탁증거금기준)
		'DpstgTotamtLackAmt' : 'long',
		# 예탁현금부족금액(위탁증거금기준)
		'DpstgMnyLackAmt' : 'long',
		# 실입금액
		'RealInAmt' : 'long',
		# 입금액
		'InAmt' : 'long',
		# 출금액
		'OutAmt' : 'long',
		# 선물정산차금
		'FutsAdjstDfamt' : 'long',
		# 선물당일차금
		'FutsThdayDfamt' : 'long',
		# 선물갱신차금
		'FutsUpdtDfamt' : 'long',
		# 선물최종결제차금
		'FutsLastSettDfamt' : 'long',
		# 옵션결제차금
		'OptSettDfamt' : 'long',
		# 옵션매수금액
		'OptBuyAmt' : 'long',
		# 옵션매도금액
		'OptSellAmt' : 'long',
		# 옵션행사차금
		'OptXrcDfamt' : 'long',
		# 옵션배정차금
		'OptAsgnDfamt' : 'long',
		# 실물인수도금액
		'RealGdsUndAmt' : 'long',
		# 실물인수도배정대금
		'RealGdsUndAsgnAmt' : 'long',
		# 실물인수도행사대금
		'RealGdsUndXrcAmt' : 'long',
		# 수수료
		'CmsnAmt' : 'long',
		# 선물수수료
		'FutsCmsn' : 'long',
		# 옵션수수료
		'OptCmsn' : 'long',
		# 선물약정수량
		'FutsCtrctQty' : 'long',
		# 선물약정금액
		'FutsCtrctAmt' : 'long',
		# 옵션약정수량
		'OptCtrctQty' : 'long',
		# 옵션약정금액
		'OptCtrctAmt' : 'long',
		# 선물미결제수량
		'FutsUnsttQty' : 'long',
		# 선물미결제금액
		'FutsUnsttAmt' : 'long',
		# 옵션미결제수량
		'OptUnsttQty' : 'long',
		# 옵션미결제금액
		'OptUnsttAmt' : 'long',
		# 선물매수미결제수량
		'FutsBuyUnsttQty' : 'long',
		# 선물매수미결제금액
		'FutsBuyUnsttAmt' : 'long',
		# 선물매도미결제수량
		'FutsSellUnsttQty' : 'long',
		# 선물매도미결제금액
		'FutsSellUnsttAmt' : 'long',
		# 옵션매수미결제수량
		'OptBuyUnsttQty' : 'long',
		# 옵션매수미결제금액
		'OptBuyUnsttAmt' : 'long',
		# 옵션매도미결제수량
		'OptSellUnsttQty' : 'long',
		# 옵션매도미결제금액
		'OptSellUnsttAmt' : 'long',
		# 선물매수약정수량
		'FutsBuyctrQty' : 'long',
		# 선물매수약정금액
		'FutsBuyctrAmt' : 'long',
		# 선물매도약정수량
		'FutsSlctrQty' : 'long',
		# 선물매도약정금액
		'FutsSlctrAmt' : 'long',
		# 옵션매수약정수량
		'OptBuyctrQty' : 'long',
		# 옵션매수약정금액
		'OptBuyctrAmt' : 'long',
		# 옵션매도약정수량
		'OptSlctrQty' : 'long',
		# 옵션매도약정금액
		'OptSlctrAmt' : 'long',
		# 선물매매손익금액
		'FutsBnsplAmt' : 'long',
		# 옵션매매손익금액
		'OptBnsplAmt' : 'long',
		# 선물평가손익금액
		'FutsEvalPnlAmt' : 'long',
		# 옵션평가손익금액
		'OptEvalPnlAmt' : 'long',
		# 선물평가금액
		'FutsEvalAmt' : 'long',
		# 옵션평가금액
		'OptEvalAmt' : 'long',
		# 장종료후현금입금금액
		'MktEndAfMnyInAmt' : 'long',
		# 장종료후현금출금금액
		'MktEndAfMnyOutAmt' : 'long',
		# 장종료후대용지정금액
		'MktEndAfSubstDsgnAmt' : 'long',
		# 장종료후대용해지금액
		'MktEndAfSubstAbndAmt' : 'long'
	}
}

# 선물옵션 일별 계좌손익내역
db_outblock_query_CFOEQ82600 = {
	'CFOEQ82600OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 조회구분
		'QryTp' : 'char',
		# 정렬순서구분
		'StnlnSeqTp' : 'char',
		# 선물옵션잔고평가구분코드
		'FnoBalEvalTpCode' : 'char'
	},
	'CFOEQ82600OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 선물정산차금
		'FutsAdjstDfamt' : 'long',
		# 옵션매매손익금액
		'OptBnsplAmt' : 'long',
		# 선물옵션수수료
		'FnoCmsnAmt' : 'long',
		# 손익합계금액
		'PnlSumAmt' : 'long',
		# 입금합계금액
		'MnyinSumAmt' : 'long',
		# 출금합계금액
		'MnyoutSumAmt' : 'long',
		# 계좌명
		'AcntNm' : 'char'
	},
	'CFOEQ82600OutBlock3' : [
		{
			# 조회일
			'QryDt' : 'char',
			# 예탁총액
			'DpstgTotamt' : 'long',
			# 예탁현금
			'DpstgMny' : 'long',
			# 선물옵션증거금액
			'FnoMgn' : 'long',
			# 선물손익금액
			'FutsPnlAmt' : 'long',
			# 옵션매매손익금액
			'OptBsnPnlAmt' : 'long',
			# 옵션평가손익금액
			'OptEvalPnlAmt' : 'long',
			# 수수료
			'CmsnAmt' : 'long',
			# 합계금액1
			'SumAmt1' : 'long',
			# 합계금액
			'SumAmt2' : 'long',
			# 손익합계금액
			'PnlSumAmt' : 'long',
			# 선물매수금액
			'FutsBuyAmt' : 'long',
			# 선물매도금액
			'FutsSellAmt' : 'long',
			# 옵션매수금액
			'OptBuyAmt' : 'long',
			# 옵션매도금액
			'OptSellAmt' : 'long',
			# 입금액
			'InAmt' : 'long',
			# 출금액
			'OutAmt' : 'long',
			# 평가금액
			'EvalAmt' : 'long',
			# 합산평가금액
			'AddupEvalAmt' : 'long',
			# 금액2
			'Amt2' : 'long'
		}
	]
}

# 계좌 미결제 약정현황(평균가)
db_outblock_query_CFOFQ02400 = {
	'CFOFQ02400OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 등록시장코드
		'RegMktCode' : 'char',
		# 매수일자
		'BuyDt' : 'char'
	},
	'CFOFQ02400OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 선물약정수량
		'FutsCtrctQty' : 'long',
		# 옵션약정수량
		'OptCtrctQty' : 'long',
		# 약정수량
		'CtrctQty' : 'long',
		# 선물약정금액
		'FutsCtrctAmt' : 'long',
		# 선물매수약정금액
		'FutsBuyctrAmt' : 'long',
		# 선물매도약정금액
		'FutsSlctrAmt' : 'long',
		# 콜옵션약정금액
		'CalloptCtrctAmt' : 'long',
		# 콜매수금액
		'CallBuyAmt' : 'long',
		# 콜매도금액
		'CallSellAmt' : 'long',
		# 풋옵션약정금액
		'PutoptCtrctAmt' : 'long',
		# 풋매수금액
		'PutBuyAmt' : 'long',
		# 풋매도금액
		'PutSellAmt' : 'long',
		# 전체약정금액
		'AllCtrctAmt' : 'long',
		# 매수약정누계금액
		'BuyctrAsmAmt' : 'long',
		# 매도약정누계금액
		'SlctrAsmAmt' : 'long',
		# 선물손익합계
		'FutsPnlSum' : 'long',
		# 옵션손익합계
		'OptPnlSum' : 'long',
		# 전체손익합계
		'AllPnlSum' : 'long'
	},
	'CFOFQ02400OutBlock3' : [
		{
			# 선물옵션품목구분
			'FnoClssCode' : 'char',
			# 선물매도수량
			'FutsSellQty' : 'long',
			# 선물매도손익
			'FutsSellPnl' : 'long',
			# 선물매수수량
			'FutsBuyQty' : 'long',
			# 선물매수손익
			'FutsBuyPnl' : 'long',
			# 콜매도수량
			'CallSellQty' : 'long',
			# 콜매도손익
			'CallSellPnl' : 'long',
			# 콜매수수량
			'CallBuyQty' : 'long',
			# 콜매수손익
			'CallBuyPnl' : 'long',
			# 풋매도수량
			'PutSellQty' : 'long',
			# 풋매도손익
			'PutSellPnl' : 'long',
			# 풋매수수량
			'PutBuyQty' : 'long',
			# 풋매수손익
			'PutBuyPnl' : 'long'
		}
	],
	'CFOFQ02400OutBlock4' : [
		{
			# 종목번호
			'IsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 잔고수량
			'BalQty' : 'long',
			# 평균가
			'FnoAvrPrc' : 'double',
			# 당초금액
			'BgnAmt' : 'long',
			# 당일청산수량
			'ThdayLqdtQty' : 'long',
			# 현재가
			'Curprc' : 'double',
			# 평가금액
			'EvalAmt' : 'long',
			# 평가손익금액
			'EvalPnlAmt' : 'long',
			# 평가수익률
			'EvalErnrat' : 'double'
		}
	]
}

# 챠트엑셀데이터조회
db_outblock_query_ChartExcel = {
	'ChartExcelOutBlock' : {
		# 지표ID
		'indexid' : 'long',
		# 레코드갯수
		'rec_cnt' : 'long',
		# 유효 데이터 컬럼 갯수
		'validdata_cnt' : 'long'
	},
	'ChartExcelOutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'volume' : 'float',
			# 지표값1
			'value1' : 'float',
			# 지표값2
			'value2' : 'float',
			# 지표값3
			'value3' : 'float',
			# 지표값4
			'value4' : 'float',
			# 지표값5
			'value5' : 'float',
			# 위치
			'pos' : 'long'
		}
	]
}

# 챠트지표데이터조회
db_outblock_query_ChartIndex = {
	'ChartIndexOutBlock' : {
		# 지표ID
		'indexid' : 'long',
		# 레코드갯수
		'rec_cnt' : 'long',
		# 유효 데이터 컬럼 갯수
		'validdata_cnt' : 'long'
	},
	'ChartIndexOutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'volume' : 'float',
			# 지표값1
			'value1' : 'float',
			# 지표값2
			'value2' : 'float',
			# 지표값3
			'value3' : 'float',
			# 지표값4
			'value4' : 'float',
			# 지표값5
			'value5' : 'float',
			# 위치
			'pos' : 'long'
		}
	]
}

# 예탁담보융자가능종목현황조회
db_outblock_query_CLNAQ00100 = {
	'CLNAQ00100OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 조회구분
		'QryTp' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 유가증권구분
		'SecTpCode' : 'char',
		# 대출이자등급코드
		'LoanIntrstGrdCode' : 'char',
		# 대출구분
		'LoanTp' : 'char'
	},
	'CLNAQ00100OutBlock2' : [
		{
			# 종목번호
			'IsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 액면가
			'Parprc' : 'double',
			# 전일종가
			'PrdayCprc' : 'double',
			# 비율값
			'RatVal' : 'double',
			# 대용가
			'SubstPrc' : 'double',
			# 등록구분
			'RegTpNm' : 'char',
			# 현물증거금징수분류명
			'SpotMgnLevyClssNm' : 'char',
			# 거래정지사유
			'FnoTrdStopRsnCnts' : 'char',
			# 요주의유형명
			'DgrsPtnNm' : 'char',
			# 사고유형
			'AcdPtnNm' : 'char',
			# 시장구분
			'MktTpNm' : 'char',
			# 한도값
			'LmtVal' : 'long',
			# 계좌한도값
			'AcntLmtVal' : 'long',
			# 대출등급코드
			'LoanGrdCode' : 'char',
			# 대출금액
			'LoanAmt' : 'long',
			# 대출가능율
			'LoanAbleRat' : 'double',
			# 대출이율1
			'LoanIntrat1' : 'double',
			# 등록자ID
			'RegPsnId' : 'char',
			# 비율값
			'Rat01' : 'double',
			# 비율값
			'Rat02' : 'double'
		}
	],
	'CLNAQ00100OutBlock3' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 대출금합계금액
		'LrgMnyoutSumAmt' : 'long'
	}
}

# CME접수
db_outblock_subscription_CM0 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'userId' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# CME체결
db_outblock_subscription_CM1 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'userId' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# CME확인
db_outblock_subscription_CM2 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'userId' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# 계좌별신용한도조회
db_outblock_query_CSPAQ00600 = {
	'CSPAQ00600OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 대출상세분류코드
		'LoanDtlClssCode' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 주문가
		'OrdPrc' : 'double'
	},
	'CSPAQ00600OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 주문가
		'OrdPrc' : 'double',
		# 대주한도
		'SloanLmtAmt' : 'long',
		# 대주금액합계
		'SloanAmtSum' : 'long',
		# 대주신규금액
		'SloanNewAmt' : 'long',
		# 대주상환금액
		'SloanRfundAmt' : 'long',
		# 유통융자한도금액
		'MktcplMloanLmtAmt' : 'long',
		# 유통융자금액합계
		'MktcplMloanAmtSum' : 'long',
		# 유통융자신규금액
		'MktcplMloanNewAmt' : 'long',
		# 유통융자상환금액
		'MktcplMloanRfundAmt' : 'long',
		# 자기융자한도금액
		'SfaccMloanLmtAmt' : 'long',
		# 자기융자금액합계
		'SfaccMloanAmtSum' : 'long',
		# 자기융자신규금액
		'SfaccMloanNewAmt' : 'long',
		# 자기융자상환금액
		'SfaccMloanRfundAmt' : 'long',
		# 지점유통융자한도금액
		'BrnMktcplMloanLmtAmt' : 'long',
		# 지점유통융자신규금액
		'BrnMktcplMloanNewAmt' : 'long',
		# 지점유통융자상환금액
		'BrnMktcplMloanRfundAmt' : 'long',
		# 지점유통융자사용금액
		'BrnMktcplMloanUseAmt' : 'long',
		# 지점자기융자한도금액
		'BrnSfaccMloanLmtAmt' : 'long',
		# 지점자기융자신규금액
		'BrnSfaccMloanNewAmt' : 'long',
		# 지점자기융자상환금액
		'BrnSfaccMloanRfundAmt' : 'long',
		# 지점자기융자사용금액
		'BrnSfaccMloanUseAmt' : 'long',
		# 이용사융자한도관리여부
		'FirmMloanLmtMgmtYn' : 'char',
		# 이용사신용종목제한구분
		'FirmCrdtIsuRestrcTp' : 'char',
		# 담보유지비율
		'PldgMaintRat' : 'double',
		# 이용사명
		'FirmNm' : 'char',
		# 담보비율
		'PldgRat' : 'double',
		# 예탁자산합계
		'DpsastSum' : 'long',
		# 한도변경가능금액
		'LmtChgAbleAmt' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long',
		# 미수불가주문가능수량
		'RcvblUablOrdAbleQty' : 'long'
	}
}

# 현물계좌예수금 주문가능금액 총평가 조회
db_outblock_query_CSPAQ12200 = {
	'CSPAQ12200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 관리지점번호
		'MgmtBrnNo' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 잔고생성구분
		'BalCreTp' : 'char'
	},
	'CSPAQ12200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 출금가능금액
		'MnyoutAbleAmt' : 'long',
		# 거래소금액
		'SeOrdAbleAmt' : 'long',
		# 코스닥금액
		'KdqOrdAbleAmt' : 'long',
		# 잔고평가금액
		'BalEvalAmt' : 'long',
		# 미수금액
		'RcvblAmt' : 'long',
		# 예탁자산총액
		'DpsastTotamt' : 'long',
		# 손익율
		'PnlRat' : 'double',
		# 투자원금
		'InvstOrgAmt' : 'long',
		# 투자손익금액
		'InvstPlAmt' : 'long',
		# 신용담보주문금액
		'CrdtPldgOrdAmt' : 'long',
		# 예수금
		'Dps' : 'long',
		# 대용금액
		'SubstAmt' : 'long',
		# D1예수금
		'D1Dps' : 'long',
		# D2예수금
		'D2Dps' : 'long',
		# 현금미수금액
		'MnyrclAmt' : 'long',
		# 증거금현금
		'MgnMny' : 'long',
		# 증거금대용
		'MgnSubst' : 'long',
		# 수표금액
		'ChckAmt' : 'long',
		# 대용주문가능금액
		'SubstOrdAbleAmt' : 'long',
		# 증거금률100퍼센트주문가능금액
		'MgnRat100pctOrdAbleAmt' : 'long',
		# 증거금률35%주문가능금액
		'MgnRat35ordAbleAmt' : 'long',
		# 증거금률50%주문가능금액
		'MgnRat50ordAbleAmt' : 'long',
		# 전일매도정산금액
		'PrdaySellAdjstAmt' : 'long',
		# 전일매수정산금액
		'PrdayBuyAdjstAmt' : 'long',
		# 금일매도정산금액
		'CrdaySellAdjstAmt' : 'long',
		# 금일매수정산금액
		'CrdayBuyAdjstAmt' : 'long',
		# D1연체변제소요금액
		'D1ovdRepayRqrdAmt' : 'long',
		# D2연체변제소요금액
		'D2ovdRepayRqrdAmt' : 'long',
		# D1추정인출가능금액
		'D1PrsmptWthdwAbleAmt' : 'long',
		# D2추정인출가능금액
		'D2PrsmptWthdwAbleAmt' : 'long',
		# 예탁담보대출금액
		'DpspdgLoanAmt' : 'long',
		# 신용설정보증금
		'Imreq' : 'long',
		# 융자금액
		'MloanAmt' : 'long',
		# 변경후담보비율
		'ChgAfPldgRat' : 'double',
		# 원담보금액
		'OrgPldgAmt' : 'long',
		# 부담보금액
		'SubPldgAmt' : 'long',
		# 소요담보금액
		'RqrdPldgAmt' : 'long',
		# 원담보부족금액
		'OrgPdlckAmt' : 'long',
		# 담보부족금액
		'PdlckAmt' : 'long',
		# 추가담보현금
		'AddPldgMny' : 'long',
		# D1주문가능금액
		'D1OrdAbleAmt' : 'long',
		# 신용이자미납금액
		'CrdtIntdltAmt' : 'long',
		# 기타대여금액
		'EtclndAmt' : 'long',
		# 익일추정반대매매금액
		'NtdayPrsmptCvrgAmt' : 'long',
		# 원담보합계금액
		'OrgPldgSumAmt' : 'long',
		# 신용주문가능금액
		'CrdtOrdAbleAmt' : 'long',
		# 부담보합계금액
		'SubPldgSumAmt' : 'long',
		# 신용담보금현금
		'CrdtPldgAmtMny' : 'long',
		# 신용담보대용금액
		'CrdtPldgSubstAmt' : 'long',
		# 추가신용담보현금
		'AddCrdtPldgMny' : 'long',
		# 신용담보재사용금액
		'CrdtPldgRuseAmt' : 'long',
		# 추가신용담보대용
		'AddCrdtPldgSubst' : 'long',
		# 매도대금담보대출금액
		'CslLoanAmtdt1' : 'long',
		# 처분제한금액
		'DpslRestrcAmt' : 'long'
	}
}

# BEP단가조회
db_outblock_query_CSPAQ12300 = {
	'CSPAQ12300OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 잔고생성구분
		'BalCreTp' : 'char',
		# 수수료적용구분
		'CmsnAppTpCode' : 'char',
		# D2잔고기준조회구분
		'D2balBaseQryTp' : 'char',
		# 단가구분
		'UprcTpCode' : 'char'
	},
	'CSPAQ12300OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 지점명
		'BrnNm' : 'char',
		# 계좌명
		'AcntNm' : 'char',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 출금가능금액
		'MnyoutAbleAmt' : 'long',
		# 거래소금액
		'SeOrdAbleAmt' : 'long',
		# 코스닥금액
		'KdqOrdAbleAmt' : 'long',
		# HTS주문가능금액
		'HtsOrdAbleAmt' : 'long',
		# 증거금률100퍼센트주문가능금액
		'MgnRat100pctOrdAbleAmt' : 'long',
		# 잔고평가금액
		'BalEvalAmt' : 'long',
		# 매입금액
		'PchsAmt' : 'long',
		# 미수금액
		'RcvblAmt' : 'long',
		# 손익율
		'PnlRat' : 'double',
		# 투자원금
		'InvstOrgAmt' : 'long',
		# 투자손익금액
		'InvstPlAmt' : 'long',
		# 신용담보주문금액
		'CrdtPldgOrdAmt' : 'long',
		# 예수금
		'Dps' : 'long',
		# D1예수금
		'D1Dps' : 'long',
		# D2예수금
		'D2Dps' : 'long',
		# 주문일
		'OrdDt' : 'char',
		# 현금증거금액
		'MnyMgn' : 'long',
		# 대용증거금액
		'SubstMgn' : 'long',
		# 대용금액
		'SubstAmt' : 'long',
		# 전일매수체결금액
		'PrdayBuyExecAmt' : 'long',
		# 전일매도체결금액
		'PrdaySellExecAmt' : 'long',
		# 금일매수체결금액
		'CrdayBuyExecAmt' : 'long',
		# 금일매도체결금액
		'CrdaySellExecAmt' : 'long',
		# 평가손익합계
		'EvalPnlSum' : 'long',
		# 예탁자산총액
		'DpsastTotamt' : 'long',
		# 제비용
		'Evrprc' : 'long',
		# 재사용금액
		'RuseAmt' : 'long',
		# 기타대여금액
		'EtclndAmt' : 'long',
		# 가정산금액
		'PrcAdjstAmt' : 'long',
		# D1수수료
		'D1CmsnAmt' : 'long',
		# D2수수료
		'D2CmsnAmt' : 'long',
		# D1제세금
		'D1EvrTax' : 'long',
		# D2제세금
		'D2EvrTax' : 'long',
		# D1결제예정금액
		'D1SettPrergAmt' : 'long',
		# D2결제예정금액
		'D2SettPrergAmt' : 'long',
		# 전일KSE현금증거금
		'PrdayKseMnyMgn' : 'long',
		# 전일KSE대용증거금
		'PrdayKseSubstMgn' : 'long',
		# 전일KSE신용현금증거금
		'PrdayKseCrdtMnyMgn' : 'long',
		# 전일KSE신용대용증거금
		'PrdayKseCrdtSubstMgn' : 'long',
		# 금일KSE현금증거금
		'CrdayKseMnyMgn' : 'long',
		# 금일KSE대용증거금
		'CrdayKseSubstMgn' : 'long',
		# 금일KSE신용현금증거금
		'CrdayKseCrdtMnyMgn' : 'long',
		# 금일KSE신용대용증거금
		'CrdayKseCrdtSubstMgn' : 'long',
		# 전일코스닥현금증거금
		'PrdayKdqMnyMgn' : 'long',
		# 전일코스닥대용증거금
		'PrdayKdqSubstMgn' : 'long',
		# 전일코스닥신용현금증거금
		'PrdayKdqCrdtMnyMgn' : 'long',
		# 전일코스닥신용대용증거금
		'PrdayKdqCrdtSubstMgn' : 'long',
		# 금일코스닥현금증거금
		'CrdayKdqMnyMgn' : 'long',
		# 금일코스닥대용증거금
		'CrdayKdqSubstMgn' : 'long',
		# 금일코스닥신용현금증거금
		'CrdayKdqCrdtMnyMgn' : 'long',
		# 금일코스닥신용대용증거금
		'CrdayKdqCrdtSubstMgn' : 'long',
		# 전일프리보드현금증거금
		'PrdayFrbrdMnyMgn' : 'long',
		# 전일프리보드대용증거금
		'PrdayFrbrdSubstMgn' : 'long',
		# 금일프리보드현금증거금
		'CrdayFrbrdMnyMgn' : 'long',
		# 금일프리보드대용증거금
		'CrdayFrbrdSubstMgn' : 'long',
		# 전일장외현금증거금
		'PrdayCrbmkMnyMgn' : 'long',
		# 전일장외대용증거금
		'PrdayCrbmkSubstMgn' : 'long',
		# 금일장외현금증거금
		'CrdayCrbmkMnyMgn' : 'long',
		# 금일장외대용증거금
		'CrdayCrbmkSubstMgn' : 'long',
		# 예탁담보수량
		'DpspdgQty' : 'long',
		# 매수정산금(D+2)
		'BuyAdjstAmtD2' : 'long',
		# 매도정산금(D+2)
		'SellAdjstAmtD2' : 'long',
		# 변제소요금(D+1)
		'RepayRqrdAmtD1' : 'long',
		# 변제소요금(D+2)
		'RepayRqrdAmtD2' : 'long',
		# 대출금액
		'LoanAmt' : 'long'
	},
	'CSPAQ12300OutBlock3' : [
		{
			# 종목번호
			'IsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 유가증권잔고유형코드
			'SecBalPtnCode' : 'char',
			# 유가증권잔고유형명
			'SecBalPtnNm' : 'char',
			# 잔고수량
			'BalQty' : 'long',
			# 매매기준잔고수량
			'BnsBaseBalQty' : 'long',
			# 금일매수체결수량
			'CrdayBuyExecQty' : 'long',
			# 금일매도체결수량
			'CrdaySellExecQty' : 'long',
			# 매도가
			'SellPrc' : 'double',
			# 매수가
			'BuyPrc' : 'double',
			# 매도손익금액
			'SellPnlAmt' : 'long',
			# 손익율
			'PnlRat' : 'double',
			# 현재가
			'NowPrc' : 'double',
			# 신용금액
			'CrdtAmt' : 'long',
			# 만기일
			'DueDt' : 'char',
			# 전일매도체결가
			'PrdaySellExecPrc' : 'double',
			# 전일매도수량
			'PrdaySellQty' : 'long',
			# 전일매수체결가
			'PrdayBuyExecPrc' : 'double',
			# 전일매수수량
			'PrdayBuyQty' : 'long',
			# 대출일
			'LoanDt' : 'char',
			# 평균단가
			'AvrUprc' : 'double',
			# 매도가능수량
			'SellAbleQty' : 'long',
			# 매도주문수량
			'SellOrdQty' : 'long',
			# 금일매수체결금액
			'CrdayBuyExecAmt' : 'long',
			# 금일매도체결금액
			'CrdaySellExecAmt' : 'long',
			# 전일매수체결금액
			'PrdayBuyExecAmt' : 'long',
			# 전일매도체결금액
			'PrdaySellExecAmt' : 'long',
			# 잔고평가금액
			'BalEvalAmt' : 'long',
			# 평가손익
			'EvalPnl' : 'long',
			# 현금주문가능금액
			'MnyOrdAbleAmt' : 'long',
			# 주문가능금액
			'OrdAbleAmt' : 'long',
			# 매도미체결수량
			'SellUnercQty' : 'long',
			# 매도미결제수량
			'SellUnsttQty' : 'long',
			# 매수미체결수량
			'BuyUnercQty' : 'long',
			# 매수미결제수량
			'BuyUnsttQty' : 'long',
			# 미결제수량
			'UnsttQty' : 'long',
			# 미체결수량
			'UnercQty' : 'long',
			# 전일종가
			'PrdayCprc' : 'double',
			# 매입금액
			'PchsAmt' : 'long',
			# 등록시장코드
			'RegMktCode' : 'char',
			# 대출상세분류코드
			'LoanDtlClssCode' : 'char',
			# 예탁담보대출수량
			'DpspdgLoanQty' : 'long'
		}
	]
}

# 현물계좌주문체결내역조회
db_outblock_query_CSPAQ13700 = {
	'CSPAQ13700OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 체결여부
		'ExecYn' : 'char',
		# 주문일
		'OrdDt' : 'char',
		# 시작주문번호2
		'SrtOrdNo2' : 'long',
		# 역순구분
		'BkseqTpCode' : 'char',
		# 주문유형코드
		'OrdPtnCode' : 'char'
	},
	'CSPAQ13700OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 매도체결금액
		'SellExecAmt' : 'long',
		# 매수체결금액
		'BuyExecAmt' : 'long',
		# 매도체결수량
		'SellExecQty' : 'long',
		# 매수체결수량
		'BuyExecQty' : 'long',
		# 매도주문수량
		'SellOrdQty' : 'long',
		# 매수주문수량
		'BuyOrdQty' : 'long'
	},
	'CSPAQ13700OutBlock3' : [
		{
			# 주문일
			'OrdDt' : 'char',
			# 관리지점번호
			'MgmtBrnNo' : 'char',
			# 주문시장코드
			'OrdMktCode' : 'char',
			# 주문번호
			'OrdNo' : 'long',
			# 원주문번호
			'OrgOrdNo' : 'long',
			# 종목번호
			'IsuNo' : 'char',
			# 종목명
			'IsuNm' : 'char',
			# 매매구분
			'BnsTpCode' : 'char',
			# 매매구분
			'BnsTpNm' : 'char',
			# 주문유형코드
			'OrdPtnCode' : 'char',
			# 주문유형명
			'OrdPtnNm' : 'char',
			# 주문처리유형코드
			'OrdTrxPtnCode' : 'long',
			# 주문처리유형명
			'OrdTrxPtnNm' : 'char',
			# 정정취소구분
			'MrcTpCode' : 'char',
			# 정정취소구분명
			'MrcTpNm' : 'char',
			# 정정취소수량
			'MrcQty' : 'long',
			# 정정취소가능수량
			'MrcAbleQty' : 'long',
			# 주문수량
			'OrdQty' : 'long',
			# 주문가격
			'OrdPrc' : 'double',
			# 체결수량
			'ExecQty' : 'long',
			# 체결가
			'ExecPrc' : 'double',
			# 체결처리시각
			'ExecTrxTime' : 'char',
			# 최종체결시각
			'LastExecTime' : 'char',
			# 호가유형코드
			'OrdprcPtnCode' : 'char',
			# 호가유형명
			'OrdprcPtnNm' : 'char',
			# 주문조건구분
			'OrdCndiTpCode' : 'char',
			# 전체체결수량
			'AllExecQty' : 'long',
			# 통신매체코드
			'RegCommdaCode' : 'char',
			# 통신매체명
			'CommdaNm' : 'char',
			# 회원번호
			'MbrNo' : 'char',
			# 예약주문여부
			'RsvOrdYn' : 'char',
			# 대출일
			'LoanDt' : 'char',
			# 주문시각
			'OrdTime' : 'char',
			# 운용지시번호
			'OpDrtnNo' : 'char',
			# 주문자ID
			'OdrrId' : 'char'
		}
	]
}

# 현물주문
db_outblock_query_CSPAT00600 = {
	'CSPAT00600OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 주문수량
		'OrdQty' : 'long',
		# 주문가
		'OrdPrc' : 'double',
		# 매매구분
		'BnsTpCode' : 'char',
		# 호가유형코드
		'OrdprcPtnCode' : 'char',
		# 프로그램호가유형코드
		'PrgmOrdprcPtnCode' : 'char',
		# 공매도가능여부
		'StslAbleYn' : 'char',
		# 공매도호가구분
		'StslOrdprcTpCode' : 'char',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 신용거래코드
		'MgntrnCode' : 'char',
		# 대출일
		'LoanDt' : 'char',
		# 회원번호
		'MbrNo' : 'char',
		# 주문조건구분
		'OrdCndiTpCode' : 'char',
		# 전략코드
		'StrtgCode' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문회차
		'OrdSeqNo' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long',
		# 운용지시번호
		'OpDrtnNo' : 'char',
		# 유동성공급자여부
		'LpYn' : 'char',
		# 반대매매구분
		'CvrgTpCode' : 'char'
	},
	'CSPAT00600OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 주문시각
		'OrdTime' : 'char',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 주문유형코드
		'OrdPtnCode' : 'char',
		# 단축종목번호
		'ShtnIsuNo' : 'char',
		# 관리사원번호
		'MgempNo' : 'char',
		# 주문금액
		'OrdAmt' : 'long',
		# 예비주문번호
		'SpareOrdNo' : 'long',
		# 반대매매일련번호
		'CvrgSeqno' : 'long',
		# 예약주문번호
		'RsvOrdNo' : 'long',
		# 실물주문수량
		'SpotOrdQty' : 'long',
		# 재사용주문수량
		'RuseOrdQty' : 'long',
		# 현금주문금액
		'MnyOrdAmt' : 'long',
		# 대용주문금액
		'SubstOrdAmt' : 'long',
		# 재사용주문금액
		'RuseOrdAmt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char'
	}
}

# 현물정정주문
db_outblock_query_CSPAT00700 = {
	'CSPAT00700OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 주문수량
		'OrdQty' : 'long',
		# 호가유형코드
		'OrdprcPtnCode' : 'char',
		# 주문조건구분
		'OrdCndiTpCode' : 'char',
		# 주문가
		'OrdPrc' : 'double',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 전략코드
		'StrtgCode' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 주문회차
		'OrdSeqNo' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long'
	},
	'CSPAT00700OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 모주문번호
		'PrntOrdNo' : 'long',
		# 주문시각
		'OrdTime' : 'char',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 주문유형코드
		'OrdPtnCode' : 'char',
		# 단축종목번호
		'ShtnIsuNo' : 'char',
		# 프로그램호가유형코드
		'PrgmOrdprcPtnCode' : 'char',
		# 공매도호가구분
		'StslOrdprcTpCode' : 'char',
		# 공매도가능여부
		'StslAbleYn' : 'char',
		# 신용거래코드
		'MgntrnCode' : 'char',
		# 대출일
		'LoanDt' : 'char',
		# 반대매매주문구분
		'CvrgOrdTp' : 'char',
		# 유동성공급자여부
		'LpYn' : 'char',
		# 관리사원번호
		'MgempNo' : 'char',
		# 주문금액
		'OrdAmt' : 'long',
		# 매매구분
		'BnsTpCode' : 'char',
		# 예비주문번호
		'SpareOrdNo' : 'long',
		# 반대매매일련번호
		'CvrgSeqno' : 'long',
		# 예약주문번호
		'RsvOrdNo' : 'long',
		# 현금주문금액
		'MnyOrdAmt' : 'long',
		# 대용주문금액
		'SubstOrdAmt' : 'long',
		# 재사용주문금액
		'RuseOrdAmt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char'
	}
}

# 현물취소주문
db_outblock_query_CSPAT00800 = {
	'CSPAT00800OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 원주문번호
		'OrgOrdNo' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 주문수량
		'OrdQty' : 'long',
		# 통신매체코드
		'CommdaCode' : 'char',
		# 그룹ID
		'GrpId' : 'char',
		# 전략코드
		'StrtgCode' : 'char',
		# 주문회차
		'OrdSeqNo' : 'long',
		# 포트폴리오번호
		'PtflNo' : 'long',
		# 바스켓번호
		'BskNo' : 'long',
		# 트렌치번호
		'TrchNo' : 'long',
		# 아이템번호
		'ItemNo' : 'long'
	},
	'CSPAT00800OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 주문번호
		'OrdNo' : 'long',
		# 모주문번호
		'PrntOrdNo' : 'long',
		# 주문시각
		'OrdTime' : 'char',
		# 주문시장코드
		'OrdMktCode' : 'char',
		# 주문유형코드
		'OrdPtnCode' : 'char',
		# 단축종목번호
		'ShtnIsuNo' : 'char',
		# 프로그램호가유형코드
		'PrgmOrdprcPtnCode' : 'char',
		# 공매도호가구분
		'StslOrdprcTpCode' : 'char',
		# 공매도가능여부
		'StslAbleYn' : 'char',
		# 신용거래코드
		'MgntrnCode' : 'char',
		# 대출일
		'LoanDt' : 'char',
		# 반대매매주문구분
		'CvrgOrdTp' : 'char',
		# 유동성공급자여부
		'LpYn' : 'char',
		# 관리사원번호
		'MgempNo' : 'char',
		# 매매구분
		'BnsTpCode' : 'char',
		# 예비주문번호
		'SpareOrdNo' : 'long',
		# 반대매매일련번호
		'CvrgSeqno' : 'long',
		# 예약주문번호
		'RsvOrdNo' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char'
	}
}

# 현물계좌증거금률별주문가능수량조회
db_outblock_query_CSPBQ00200 = {
	'CSPBQ00200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 매매구분
		'BnsTpCode' : 'char',
		# 계좌번호
		'AcntNo' : 'char',
		# 입력비밀번호
		'InptPwd' : 'char',
		# 종목번호
		'IsuNo' : 'char',
		# 주문가격
		'OrdPrc' : 'double',
		# 통신매체코드
		'RegCommdaCode' : 'char'
	},
	'CSPBQ00200OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 종목명
		'IsuNm' : 'char',
		# 예수금
		'Dps' : 'long',
		# 대용금액
		'SubstAmt' : 'long',
		# 신용담보재사용금액
		'CrdtPldgRuseAmt' : 'long',
		# 현금주문가능금액
		'MnyOrdAbleAmt' : 'long',
		# 대용주문가능금액
		'SubstOrdAbleAmt' : 'long',
		# 현금증거금액
		'MnyMgn' : 'long',
		# 대용증거금액
		'SubstMgn' : 'long',
		# 거래소금액
		'SeOrdAbleAmt' : 'long',
		# 코스닥금액
		'KdqOrdAbleAmt' : 'long',
		# 추정예수금(D+1)
		'PrsmptDpsD1' : 'long',
		# 추정예수금(D+2)
		'PrsmptDpsD2' : 'long',
		# 출금가능금액
		'MnyoutAbleAmt' : 'long',
		# 미수금액
		'RcvblAmt' : 'long',
		# 수수료율
		'CmsnRat' : 'double',
		# 추가징수금액
		'AddLevyAmt' : 'long',
		# 재사용대상금액
		'RuseObjAmt' : 'long',
		# 현금재사용대상금액
		'MnyRuseObjAmt' : 'long',
		# 이용사증거금률
		'FirmMgnRat' : 'double',
		# 대용재사용대상금액
		'SubstRuseObjAmt' : 'long',
		# 종목증거금률
		'IsuMgnRat' : 'double',
		# 계좌증거금률
		'AcntMgnRat' : 'double',
		# 거래증거금률
		'TrdMgnrt' : 'double',
		# 수수료
		'Cmsn' : 'long',
		# 증거금률20퍼센트주문가능금액
		'MgnRat20pctOrdAbleAmt' : 'long',
		# 증거금률100퍼센트현금주문가능수량?
		'MgnRat20OrdAbleQty' : 'long',
		# 증거금률30퍼센트주문가능금액
		'MgnRat30pctOrdAbleAmt' : 'long',
		# 증거금률30퍼센트주문가능수량??
		'MgnRat30OrdAbleQty' : 'long',
		# 증거금률40퍼센트주문가능금액
		'MgnRat40pctOrdAbleAmt' : 'long',
		# 증거금률40퍼센트주문가능수량??
		'MgnRat40OrdAbleQty' : 'long',
		# 증거금률100퍼센트주문가능금액
		'MgnRat100pctOrdAbleAmt' : 'long',
		# 증거금률100퍼센트주문가능수량??
		'MgnRat100OrdAbleQty' : 'long',
		# 증거금률100퍼센트현금주문가능금액?
		'MgnRat100MnyOrdAbleAmt' : 'long',
		# 증거금률100퍼센트현금주문가능수량
		'MgnRat100MnyOrdAbleQty' : 'long',
		# 증거금률20퍼센트재사용가능금액
		'MgnRat20pctRuseAbleAmt' : 'long',
		# 증거금률30퍼센트재사용가능금액
		'MgnRat30pctRuseAbleAmt' : 'long',
		# 증거금률40퍼센트재사용가능금액
		'MgnRat40pctRuseAbleAmt' : 'long',
		# 증거금률100퍼센트재사용가능금액
		'MgnRat100pctRuseAbleAmt' : 'long',
		# 주문가능수량
		'OrdAbleQty' : 'long',
		# 주문가능금액
		'OrdAbleAmt' : 'long'
	}
}

# 시간외단일가VI발동해제(DVI)
db_outblock_subscription_DVI = {
	'OutBlock' : {
		# 구분
		'vi_gubun' : 'char',
		# VI발동기준가격
		'vi_recprice' : 'long',
		# VI발동가격
		'vi_trgprice' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# EUREX연계KP200지수옵션선물체결(EC0)
db_outblock_subscription_EC0 = {
	'OutBlock' : {
		# 체결시간(24시간)
		'chetime' : 'char',
		# 체결시간(36시간)
		'chetime1' : 'char',
		# 정규장종가대비구분
		'sign' : 'char',
		# 정규장종가대비
		'change' : 'float',
		# 정규장종가기준등락율
		'drate' : 'float',
		# 현재가
		'price' : 'float',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금(미제공)
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수(미제공)
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수(미제공)
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 미결제약정수량
		'openyak' : 'long',
		# KOSPI200지수
		'k200jisu' : 'float',
		# KOSPI등가
		'eqva' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 미결제약정증감
		'openyakcha' : 'long',
		# 시간가치
		'timevalue' : 'float',
		# 장운영정보
		'jgubun' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 단축코드
		'optcode' : 'char'
	}
}

# EUREX연계KP200지수옵션선물호가(EH0)
db_outblock_subscription_EH0 = {
	'OutBlock' : {
		# 호가시간(24시간)
		'hotime' : 'char',
		# 호가시간(36시간)
		'hotime1' : 'char',
		# 매도호가1
		'offerho1' : 'double',
		# 매수호가1
		'bidho1' : 'double',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1(미제공)
		'offercnt1' : 'long',
		# 매수호가건수1(미제공)
		'bidcnt1' : 'long',
		# 매도호가2
		'offerho2' : 'double',
		# 매수호가2
		'bidho2' : 'double',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2(미제공)
		'offercnt2' : 'long',
		# 매수호가건수2(미제공)
		'bidcnt2' : 'long',
		# 매도호가3
		'offerho3' : 'double',
		# 매수호가3
		'bidho3' : 'double',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3(미제공)
		'offercnt3' : 'long',
		# 매수호가건수3(미제공)
		'bidcnt3' : 'long',
		# 매도호가4(미제공)
		'offerho4' : 'double',
		# 매수호가4(미제공)
		'bidho4' : 'double',
		# 매도호가수량4(미제공)
		'offerrem4' : 'long',
		# 매수호가수량4(미제공)
		'bidrem4' : 'long',
		# 매도호가건수4(미제공)
		'offercnt4' : 'long',
		# 매수호가건수4(미제공)
		'bidcnt4' : 'long',
		# 매도호가5(미제공)
		'offerho5' : 'double',
		# 매수호가5(미제공)
		'bidho5' : 'double',
		# 매도호가수량5(미제공)
		'offerrem5' : 'long',
		# 매수호가수량5(미제공)
		'bidrem5' : 'long',
		# 매도호가건수5(미제공)
		'offercnt5' : 'long',
		# 매수호가건수5(미제공)
		'bidcnt5' : 'long',
		# 매도호가총수량
		'totofferrem' : 'long',
		# 매수호가총수량
		'totbidrem' : 'long',
		# 매도호가총건수
		'totoffercnt' : 'long',
		# 매수호가총건수
		'totbidcnt' : 'long',
		# 단축코드
		'optcode' : 'char',
		# 단일가호가여부
		'danhochk' : 'char'
	}
}

# 뉴ELW투자지표민감도(ESN)
db_outblock_subscription_ESN = {
	'OutBlock' : {
		# 시간
		'time' : 'char',
		# 장중이론가
		'theoryprice' : 'float',
		# 델타
		'delt' : 'float',
		# 감마
		'gama' : 'float',
		# 세타
		'ceta' : 'float',
		# 베가
		'vega' : 'float',
		# 로우
		'rhox' : 'float',
		# 내재변동성
		'impv' : 'float',
		# E.기어링
		'egearing' : 'float',
		# 단축코드
		'shcode' : 'char',
		# ELW현재가
		'elwclose' : 'long',
		# ELW전일대비구분
		'sign' : 'char',
		# ELW전일대비
		'change' : 'long',
		# 일자
		'date' : 'char',
		# 틱환산
		'tickvalue' : 'float',
		# LP내재변동성
		'lp_impv' : 'float'
	}
}

# EUX접수
db_outblock_subscription_EU0 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'OrderID' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# EUX체결
db_outblock_subscription_EU1 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'OrderID' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# EUX확인
db_outblock_subscription_EU2 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'OrderID' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# KOSPI200선물체결(C0)
db_outblock_subscription_FC0 = {
	'OutBlock' : {
		# 체결시간
		'chetime' : 'char',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'float',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 미결제약정수량
		'openyak' : 'long',
		# KOSPI200지수
		'k200jisu' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 괴리율
		'kasis' : 'float',
		# 시장BASIS
		'sbasis' : 'float',
		# 이론BASIS
		'ibasis' : 'float',
		# 미결제약정증감
		'openyakcha' : 'long',
		# 장운영정보
		'jgubun' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 단축코드
		'futcode' : 'char'
	}
}

# KOSPI200선물실시간상하한가(D0)
db_outblock_subscription_FD0 = {
	'OutBlock' : {
		# 접속매매여부
		'gubun' : 'char',
		# 실시간가격제한여부
		'dy_gubun' : 'char',
		# 실시간상한가
		'dy_uplmtprice' : 'float',
		# 실시간하한가
		'dy_dnlmtprice' : 'float',
		# 단축코드
		'futcode' : 'char'
	}
}

# KOSPI200선물호가(H0)
db_outblock_subscription_FH0 = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 매도호가1
		'offerho1' : 'double',
		# 매수호가1
		'bidho1' : 'double',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'offercnt1' : 'long',
		# 매수호가건수1
		'bidcnt1' : 'long',
		# 매도호가2
		'offerho2' : 'double',
		# 매수호가2
		'bidho2' : 'double',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'offercnt2' : 'long',
		# 매수호가건수2
		'bidcnt2' : 'long',
		# 매도호가3
		'offerho3' : 'double',
		# 매수호가3
		'bidho3' : 'double',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'offercnt3' : 'long',
		# 매수호가건수3
		'bidcnt3' : 'long',
		# 매도호가4
		'offerho4' : 'double',
		# 매수호가4
		'bidho4' : 'double',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'offercnt4' : 'long',
		# 매수호가건수4
		'bidcnt4' : 'long',
		# 매도호가5
		'offerho5' : 'double',
		# 매수호가5
		'bidho5' : 'double',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'offercnt5' : 'long',
		# 매수호가건수5
		'bidcnt5' : 'long',
		# 매도호가총수량
		'totofferrem' : 'long',
		# 매수호가총수량
		'totbidrem' : 'long',
		# 매도호가총건수
		'totoffercnt' : 'long',
		# 매수호가총건수
		'totbidcnt' : 'long',
		# 단축코드
		'futcode' : 'char',
		# 단일가호가여부
		'danhochk' : 'char',
		# 배분적용구분
		'alloc_gubun' : 'char'
	}
}

# 주식계좌 기간별수익률 상세
db_outblock_query_FOCCQ33600 = {
	'FOCCQ33600OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 기간구분
		'TermTp' : 'char'
	},
	'FOCCQ33600OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 매매약정금액
		'BnsctrAmt' : 'long',
		# 입금금액
		'MnyinAmt' : 'long',
		# 출금금액
		'MnyoutAmt' : 'long',
		# 투자원금평잔금액
		'InvstAvrbalPramt' : 'long',
		# 투자손익금액
		'InvstPlAmt' : 'long',
		# 투자수익률
		'InvstErnrat' : 'double'
	},
	'FOCCQ33600OutBlock3' : [
		{
			# 기준일
			'BaseDt' : 'char',
			# 기초평가금액
			'FdEvalAmt' : 'long',
			# 기말평가금액
			'EotEvalAmt' : 'long',
			# 투자원금평잔금액
			'InvstAvrbalPramt' : 'long',
			# 매매약정금액
			'BnsctrAmt' : 'long',
			# 입금고액
			'MnyinSecinAmt' : 'long',
			# 출금고액
			'MnyoutSecoutAmt' : 'long',
			# 평가손익금액
			'EvalPnlAmt' : 'long',
			# 기간수익률
			'TermErnrat' : 'double',
			# 지수
			'Idx' : 'double'
		}
	]
}

# 선물옵션 기간별 계좌 수익률 현황
db_outblock_query_FOCCQ33700 = {
	'FOCCQ33700OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌번호
		'AcntNo' : 'char',
		# 비밀번호
		'Pwd' : 'char',
		# 조회시작일
		'QrySrtDt' : 'char',
		# 조회종료일
		'QryEndDt' : 'char',
		# 조회구분
		'QryTp' : 'char',
		# 기준금액구분
		'BaseAmtTp' : 'char',
		# 조회기간구분
		'QryTermTp' : 'char',
		# 손익산출구분코드
		'PnlCalcTpCode' : 'char'
	},
	'FOCCQ33700OutBlock2' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 계좌명
		'AcntNm' : 'char',
		# 입금액
		'InAmt' : 'long',
		# 출금액
		'OutAmt' : 'long',
		# 선물옵션약정금액
		'FnoCtrctAmt' : 'long',
		# 투자원금평잔금액
		'InvstPramtAvrbalAmt' : 'long',
		# 선물정산차금
		'FutsAdjstDfamt' : 'long',
		# 옵션매매손익금액
		'OptBsnPnlAmt' : 'long',
		# 옵션평가손익금액
		'OptEvalPnlAmt' : 'long',
		# 투자손익금액
		'InvstPlAmt' : 'long',
		# 수익률
		'ErnRat' : 'double'
	},
	'FOCCQ33700OutBlock3' : [
		{
			# 거래일
			'TrdDt' : 'char',
			# 기초예탁자산금액
			'FdDpsastAmt' : 'long',
			# 기말예탁자산금액
			'EotDpsastAmt' : 'long',
			# 입금액
			'InAmt' : 'long',
			# 출금액
			'OutAmt' : 'long',
			# 투자원금평잔금액
			'InvstAvrbalPramt' : 'long',
			# 투자손익금액
			'InvstPlAmt' : 'long',
			# 수익률
			'Ernrat' : 'double',
			# 선물옵션약정금액
			'FnoCtrctAmt' : 'long',
			# 회전율
			'Trnrat' : 'double',
			# 선물정산차금
			'FutsAdjstDfamt' : 'long',
			# 옵션매매손익금액
			'OptBsnPnlAmt' : 'long',
			# 옵션평가손익금액
			'OptEvalPnlAmt' : 'long'
		}
	]
}

# 선물주문정정취소
db_outblock_subscription_H01 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 일련번호
		'seq' : 'long',
		# trcode
		'trcode' : 'char',
		# 매칭그룹번호
		'megrpno' : 'char',
		# 보드ID
		'boardid' : 'char',
		# 회원번호
		'memberno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 주문번호
		'ordno' : 'char',
		# 원주문번호
		'ordordno' : 'char',
		# 종목코드
		'expcode' : 'char',
		# 매도수구분
		'dosugb' : 'char',
		# 정정취소구분
		'mocagb' : 'char',
		# 계좌번호1
		'accno1' : 'char',
		# 호가수량
		'qty2' : 'long',
		# 호가가격
		'price' : 'float',
		# 주문유형
		'ordgb' : 'char',
		# 호가구분
		'hogagb' : 'char',
		# 시장조성호가구분
		'sihogagb' : 'char',
		# 자사주신고서ID
		'treaid' : 'char',
		# 자사주매매방법
		'treacode' : 'char',
		# 매도유형코드
		'askcode' : 'char',
		# 신용구분코드
		'creditcode' : 'char',
		# 위탁자기구분
		'jakigb' : 'char',
		# 위탁사번호
		'trustnum' : 'char',
		# 프로그램구분
		'ptgb' : 'char',
		# 대용주권계좌번호
		'substocnum' : 'char',
		# 계좌구분코드
		'accgb' : 'char',
		# 계좌증거금코드
		'accmarggb' : 'char',
		# 국가코드
		'nationcode' : 'char',
		# 투자자구분
		'investgb' : 'char',
		# 외국인코드
		'forecode' : 'char',
		# 주문매체구분
		'medcode' : 'char',
		# 주문식별자번호
		'ordid' : 'char',
		# MAC주소
		'macid' : 'char',
		# 호가일자
		'orddate' : 'char',
		# 회원사주문시각
		'rcvtime' : 'char',
		# mem_filler
		'mem_filler' : 'char',
		# mem_accno
		'mem_accno' : 'char',
		# mem_filler1
		'mem_filler' : 'char',
		# 매칭접수시간
		'ordacpttm' : 'char',
		# 실정정취소수량
		'qty' : 'long',
		# 자동취소구분
		'autogb' : 'char',
		# 거부사유
		'rejcode' : 'char',
		# 프로그램호가신고
		'prgordde' : 'char'
	}
}

# KOSPI호가잔량(H1)
db_outblock_subscription_H1_ = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가잔량1
		'offerrem1' : 'long',
		# 매수호가잔량1
		'bidrem1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가잔량2
		'offerrem2' : 'long',
		# 매수호가잔량2
		'bidrem2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가잔량3
		'offerrem3' : 'long',
		# 매수호가잔량3
		'bidrem3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가잔량4
		'offerrem4' : 'long',
		# 매수호가잔량4
		'bidrem4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가잔량5
		'offerrem5' : 'long',
		# 매수호가잔량5
		'bidrem5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가잔량6
		'offerrem6' : 'long',
		# 매수호가잔량6
		'bidrem6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가잔량7
		'offerrem7' : 'long',
		# 매수호가잔량7
		'bidrem7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가잔량8
		'offerrem8' : 'long',
		# 매수호가잔량8
		'bidrem8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가잔량9
		'offerrem9' : 'long',
		# 매수호가잔량9
		'bidrem9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가잔량10
		'offerrem10' : 'long',
		# 매수호가잔량10
		'bidrem10' : 'long',
		# 총매도호가잔량
		'totofferrem' : 'long',
		# 총매수호가잔량
		'totbidrem' : 'long',
		# 동시호가구분
		'donsigubun' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 배분적용구분
		'alloc_gubun' : 'char'
	}
}

# KOSPI장전시간외호가잔량(H2)
db_outblock_subscription_H2_ = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 시간외매도잔량
		'tmofferrem' : 'long',
		# 시간외매수잔량
		'tmbidrem' : 'long',
		# 시간외매도수량직전대비
		'pretmoffercha' : 'long',
		# 시간외매수수량직전대비
		'pretmbidcha' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# ELW장전시간외호가잔량(h2)
db_outblock_subscription_h2_4ELW = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 시간외매도잔량
		'tmofferrem' : 'long',
		# 시간외매수잔량
		'tmbidrem' : 'long',
		# 시간외매도수량직전대비
		'pretmoffercha' : 'long',
		# 시간외매수수량직전대비
		'pretmbidcha' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# ELW호가잔량(h3)
db_outblock_subscription_h3_4ELW = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가잔량1
		'offerrem1' : 'long',
		# 매수호가잔량1
		'bidrem1' : 'long',
		# LP매도호가수량1
		'lp_offerho1' : 'long',
		# LP매수호가수량1
		'lp_bidho1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가잔량2
		'offerrem2' : 'long',
		# 매수호가잔량2
		'bidrem2' : 'long',
		# LP매도호가수량2
		'lp_offerho2' : 'long',
		# LP매수호가수량2
		'lp_bidho2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가잔량3
		'offerrem3' : 'long',
		# 매수호가잔량3
		'bidrem3' : 'long',
		# LP매도호가수량3
		'lp_offerho3' : 'long',
		# LP매수호가수량3
		'lp_bidho3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가잔량4
		'offerrem4' : 'long',
		# 매수호가잔량4
		'bidrem4' : 'long',
		# LP매도호가수량4
		'lp_offerho4' : 'long',
		# LP매수호가수량4
		'lp_bidho4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가잔량5
		'offerrem5' : 'long',
		# 매수호가잔량5
		'bidrem5' : 'long',
		# LP매도호가수량5
		'lp_offerho5' : 'long',
		# LP매수호가수량5
		'lp_bidho5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가잔량6
		'offerrem6' : 'long',
		# 매수호가잔량6
		'bidrem6' : 'long',
		# LP매도호가수량6
		'lp_offerho6' : 'long',
		# LP매수호가수량6
		'lp_bidho6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가잔량7
		'offerrem7' : 'long',
		# 매수호가잔량7
		'bidrem7' : 'long',
		# LP매도호가수량7
		'lp_offerho7' : 'long',
		# LP매수호가수량7
		'lp_bidho7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가잔량8
		'offerrem8' : 'long',
		# 매수호가잔량8
		'bidrem8' : 'long',
		# LP매도호가수량8
		'lp_offerho8' : 'long',
		# LP매수호가수량8
		'lp_bidho8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가잔량9
		'offerrem9' : 'long',
		# 매수호가잔량9
		'bidrem9' : 'long',
		# LP매도호가수량9
		'lp_offerho9' : 'long',
		# LP매수호가수량9
		'lp_bidho9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가잔량10
		'offerrem10' : 'long',
		# 매수호가잔량10
		'bidrem10' : 'long',
		# LP매도호가수량10
		'lp_offerho10' : 'long',
		# LP매수호가수량10
		'lp_bidho10' : 'long',
		# 총매도호가잔량
		'totofferrem' : 'long',
		# 총매수호가잔량
		'totbidrem' : 'long',
		# 동시호가구분
		'donsigubun' : 'char',
		# 스프레드
		'spread' : 'float',
		# 단축코드
		'shcode' : 'char'
	}
}

# KOSDAQ호가잔량(HA)
db_outblock_subscription_HA_ = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가잔량1
		'offerrem1' : 'long',
		# 매수호가잔량1
		'bidrem1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가잔량2
		'offerrem2' : 'long',
		# 매수호가잔량2
		'bidrem2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가잔량3
		'offerrem3' : 'long',
		# 매수호가잔량3
		'bidrem3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가잔량4
		'offerrem4' : 'long',
		# 매수호가잔량4
		'bidrem4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가잔량5
		'offerrem5' : 'long',
		# 매수호가잔량5
		'bidrem5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가잔량6
		'offerrem6' : 'long',
		# 매수호가잔량6
		'bidrem6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가잔량7
		'offerrem7' : 'long',
		# 매수호가잔량7
		'bidrem7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가잔량8
		'offerrem8' : 'long',
		# 매수호가잔량8
		'bidrem8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가잔량9
		'offerrem9' : 'long',
		# 매수호가잔량9
		'bidrem9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가잔량10
		'offerrem10' : 'long',
		# 매수호가잔량10
		'bidrem10' : 'long',
		# 총매도호가잔량
		'totofferrem' : 'long',
		# 총매수호가잔량
		'totbidrem' : 'long',
		# 동시호가구분
		'donsigubun' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 배분적용구분
		'alloc_gubun' : 'char'
	}
}

# KOSDAQ장전시간외호가잔량(HB)
db_outblock_subscription_HB_ = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 시간외매도잔량
		'tmofferrem' : 'long',
		# 시간외매수잔량
		'tmbidrem' : 'long',
		# 시간외매도수량직전대비
		'pretmoffercha' : 'long',
		# 시간외매수수량직전대비
		'pretmbidcha' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# 코스피ETF종목실시간NAV(I5)
db_outblock_subscription_I5_ = {
	'OutBlock' : {
		# 시간
		'time' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 누적거래량
		'volume' : 'float',
		# NAV대비
		'navdiff' : 'float',
		# NAV
		'nav' : 'float',
		# 전일대비
		'navchange' : 'float',
		# 추적오차
		'crate' : 'float',
		# 괴리
		'grate' : 'float',
		# 지수
		'jisu' : 'float',
		# 전일대비
		'jichange' : 'float',
		# 전일대비율
		'jirate' : 'float',
		# 단축코드
		'shcode' : 'char'
	}
}

# 지수(IJ)
db_outblock_subscription_IJ_ = {
	'OutBlock' : {
		# 시간
		'time' : 'char',
		# 지수
		'jisu' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일비
		'change' : 'float',
		# 등락율
		'drate' : 'float',
		# 체결량
		'cvolume' : 'long',
		# 거래량
		'volume' : 'long',
		# 거래대금
		'value' : 'long',
		# 상한종목수
		'upjo' : 'long',
		# 상승종목수
		'highjo' : 'long',
		# 보합종목수
		'unchgjo' : 'long',
		# 하락종목수
		'lowjo' : 'long',
		# 하한종목수
		'downjo' : 'long',
		# 상승종목비율
		'upjrate' : 'float',
		# 시가지수
		'openjisu' : 'float',
		# 시가시간
		'opentime' : 'char',
		# 고가지수
		'highjisu' : 'float',
		# 고가시간
		'hightime' : 'char',
		# 저가지수
		'lowjisu' : 'float',
		# 저가시간
		'lowtime' : 'char',
		# 외인순매수수량
		'frgsvolume' : 'long',
		# 기관순매수수량
		'orgsvolume' : 'long',
		# 외인순매수금액
		'frgsvalue' : 'long',
		# 기관순매수금액
		'orgsvalue' : 'long',
		# 업종코드
		'upcode' : 'char'
	}
}

# 주식선물체결(JC0)
db_outblock_subscription_JC0 = {
	'OutBlock' : {
		# 단축코드
		'futcode' : 'char',
		# 체결시간
		'chetime' : 'char',
		# 대비기호
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'double',
		# 현재가
		'price' : 'long',
		# 시가
		'open' : 'long',
		# 고가
		'high' : 'long',
		# 저가
		'low' : 'long',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'double',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 미결제약정수량
		'openyak' : 'long',
		# KOSPI200지수
		'k200jisu' : 'double',
		# 이론가
		'theoryprice' : 'long',
		# 괴리율
		'kasis' : 'double',
		# 시장BASIS
		'sbasis' : 'long',
		# 이론BASIS
		'ibasis' : 'long',
		# 미결제약정증감
		'openyakcha' : 'long',
		# 장운영정보
		'jgubun' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 기초자산현재가
		'basprice' : 'long'
	}
}

# 주식선물실시간상하한가(JD0)
db_outblock_subscription_JD0 = {
	'OutBlock' : {
		# 접속매매여부
		'gubun' : 'char',
		# 실시간가격제한여부
		'dy_gubun' : 'char',
		# 실시간상한가
		'dy_uplmtprice' : 'long',
		# 실시간하한가
		'dy_dnlmtprice' : 'long',
		# 단축코드
		'futcode' : 'char'
	}
}

# 주식선물호가(JH0)
db_outblock_subscription_JH0 = {
	'OutBlock' : {
		# 단축코드
		'futcode' : 'char',
		# 호가시간
		'hotime' : 'char',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'offercnt1' : 'long',
		# 매수호가건수1
		'bidcnt1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'offercnt2' : 'long',
		# 매수호가건수2
		'bidcnt2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'offercnt3' : 'long',
		# 매수호가건수3
		'bidcnt3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'offercnt4' : 'long',
		# 매수호가건수4
		'bidcnt4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'offercnt5' : 'long',
		# 매수호가건수5
		'bidcnt5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가수량6
		'offerrem6' : 'long',
		# 매수호가수량6
		'bidrem6' : 'long',
		# 매도호가건수6
		'offercnt6' : 'long',
		# 매수호가건수6
		'bidcnt6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가수량7
		'offerrem7' : 'long',
		# 매수호가수량7
		'bidrem7' : 'long',
		# 매도호가건수7
		'offercnt7' : 'long',
		# 매수호가건수7
		'bidcnt7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가수량8
		'offerrem8' : 'long',
		# 매수호가수량8
		'bidrem8' : 'long',
		# 매도호가건수8
		'offercnt8' : 'long',
		# 매수호가건수8
		'bidcnt8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가수량9
		'offerrem9' : 'long',
		# 매수호가수량9
		'bidrem9' : 'long',
		# 매도호가건수9
		'offercnt9' : 'long',
		# 매수호가건수9
		'bidcnt9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가수량10
		'offerrem10' : 'long',
		# 매수호가수량10
		'bidrem10' : 'long',
		# 매도호가건수10
		'offercnt10' : 'long',
		# 매수호가건수10
		'bidcnt10' : 'long',
		# 매도호가총수량
		'totofferrem' : 'long',
		# 매수호가총수량
		'totbidrem' : 'long',
		# 매도호가총건수
		'totoffercnt' : 'long',
		# 매수호가총건수
		'totbidcnt' : 'long'
	}
}

# 장운영정보(JIF)
db_outblock_subscription_JIF = {
	'OutBlock' : {
		# 장구분
		'jangubun' : 'char',
		# 장상태
		'jstatus' : 'char'
	}
}

# KOSPI거래원(K1)
db_outblock_subscription_K1_ = {
	'OutBlock' : {
		# 매도증권사코드1
		'offerno1' : 'char',
		# 매수증권사코드1
		'bidno1' : 'char',
		# 매도회원사명1
		'offertrad1' : 'char',
		# 매수회원사명1
		'bidtrad1' : 'char',
		# 매도거래량1
		'tradmdvol1' : 'long',
		# 매수거래량1
		'tradmsvol1' : 'long',
		# 매도거래량비중1
		'tradmdrate1' : 'float',
		# 매도거래량비중1
		'tradmsrate1' : 'float',
		# 매도거래량직전대비1
		'tradmdcha1' : 'long',
		# 매수거래량직전대비1
		'tradmscha1' : 'long',
		# 매도증권사코드2
		'offerno2' : 'char',
		# 매수증권사코드2
		'bidno2' : 'char',
		# 매도회원사명2
		'offertrad2' : 'char',
		# 매수회원사명2
		'bidtrad2' : 'char',
		# 매도거래량2
		'tradmdvol2' : 'long',
		# 매수거래량2
		'tradmsvol2' : 'long',
		# 매도거래량비중2
		'tradmdrate2' : 'float',
		# 매수거래량비중2
		'tradmsrate2' : 'float',
		# 매도거래량직전대비2
		'tradmdcha2' : 'long',
		# 매수거래량직전대비2
		'tradmscha2' : 'long',
		# 매도증권사코드3
		'offerno3' : 'char',
		# 매수증권사코드3
		'bidno3' : 'char',
		# 매도회원사명3
		'offertrad3' : 'char',
		# 매수회원사명3
		'bidtrad3' : 'char',
		# 매도거래량3
		'tradmdvol3' : 'long',
		# 매수거래량3
		'tradmsvol3' : 'long',
		# 매도거래량비중3
		'tradmdrate3' : 'float',
		# 매수거래량비중3
		'tradmsrate3' : 'float',
		# 매도거래량직전대비3
		'tradmdcha3' : 'long',
		# 매수거래량직전대비3
		'tradmscha3' : 'long',
		# 매도증권사코드4
		'offerno4' : 'char',
		# 매수증권사코드4
		'bidno4' : 'char',
		# 매도회원사명4
		'offertrad4' : 'char',
		# 매수회원사명4
		'bidtrad4' : 'char',
		# 매도거래량4
		'tradmdvol4' : 'long',
		# 매수거래량4
		'tradmsvol4' : 'long',
		# 매도거래량비중4
		'tradmdrate4' : 'float',
		# 매수거래량비중4
		'tradmsrate4' : 'float',
		# 매도거래량직전대비4
		'tradmdcha4' : 'long',
		# 매수거래량직전대비4
		'tradmscha4' : 'long',
		# 매도증권사코드5
		'offerno5' : 'char',
		# 매수증권사코드5
		'bidno5' : 'char',
		# 매도회원사명5
		'offertrad5' : 'char',
		# 매수회원사명5
		'bidtrad5' : 'char',
		# 매도거래량5
		'tradmdvol5' : 'long',
		# 매수거래량5
		'tradmsvol5' : 'long',
		# 매도거래량비중5
		'tradmdrate5' : 'float',
		# 매수거래량비중5
		'tradmsrate5' : 'float',
		# 매도거래량직전대비5
		'tradmdcha5' : 'long',
		# 매수거래량직전대비5
		'tradmscha5' : 'long',
		# 외국계증권사매도합계
		'ftradmdvol' : 'char',
		# 외국계증권사매수합계
		'ftradmsvol' : 'char',
		# 외국계증권사매도거래량비중
		'ftradmdrate' : 'float',
		# 외국계증권사매수거래량비중
		'ftradmsrate' : 'float',
		# 외국계증권사매도거래량직전대비
		'ftradmdcha' : 'char',
		# 외국계증권사매수거래량직전대비
		'ftradmscha' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 매도거래대금1
		'tradmdval1' : 'long',
		# 매수거래대금1
		'tradmsval1' : 'long',
		# 매도평균단가1
		'tradmdavg1' : 'long',
		# 매수평균단가1
		'tradmsavg1' : 'long',
		# 매도거래대금2
		'tradmdval2' : 'long',
		# 매수거래대금2
		'tradmsval2' : 'long',
		# 매도평균단가2
		'tradmdavg2' : 'long',
		# 매수평균단가2
		'tradmsavg2' : 'long',
		# 매도거래대금3
		'tradmdval3' : 'long',
		# 매수거래대금3
		'tradmsval3' : 'long',
		# 매도평균단가3
		'tradmdavg3' : 'long',
		# 매수평균단가3
		'tradmsavg3' : 'long',
		# 매도거래대금4
		'tradmdval4' : 'long',
		# 매수거래대금4
		'tradmsval4' : 'long',
		# 매도평균단가4
		'tradmdavg4' : 'long',
		# 매수평균단가4
		'tradmsavg4' : 'long',
		# 매도거래대금5
		'tradmdval5' : 'long',
		# 매수거래대금5
		'tradmsval5' : 'long',
		# 매도평균단가5
		'tradmdavg5' : 'long',
		# 매수평균단가5
		'tradmsavg5' : 'long',
		# 외국계증권사매도거래대금
		'ftradmdval' : 'long',
		# 외국계증권사매수거래대금
		'ftradmsval' : 'long',
		# 외국계증권사매도평균단가
		'ftradmdavg' : 'long',
		# 외국계증권사매수평균단가
		'ftradmsavg' : 'long'
	}
}

# ELW거래원(k1)
db_outblock_subscription_k1_4ELW = {
	'OutBlock' : {
		# 매도증권사코드1
		'offerno1' : 'char',
		# 매수증권사코드1
		'bidno1' : 'char',
		# 매도회원사명1
		'offertrad1' : 'char',
		# 매수회원사명1
		'bidtrad1' : 'char',
		# 매도거래량1
		'tradmdvol1' : 'long',
		# 매수거래량1
		'tradmsvol1' : 'long',
		# 매도거래량비중1
		'tradmdrate1' : 'float',
		# 매도거래량비중1
		'tradmsrate1' : 'float',
		# 매도거래량직전대비1
		'tradmdcha1' : 'long',
		# 매수거래량직전대비1
		'tradmscha1' : 'long',
		# 매도증권사코드2
		'offerno2' : 'char',
		# 매수증권사코드2
		'bidno2' : 'char',
		# 매도회원사명2
		'offertrad2' : 'char',
		# 매수회원사명2
		'bidtrad2' : 'char',
		# 매도거래량2
		'tradmdvol2' : 'long',
		# 매수거래량2
		'tradmsvol2' : 'long',
		# 매도거래량비중2
		'tradmdrate2' : 'float',
		# 매수거래량비중2
		'tradmsrate2' : 'float',
		# 매도거래량직전대비2
		'tradmdcha2' : 'long',
		# 매수거래량직전대비2
		'tradmscha2' : 'long',
		# 매도증권사코드3
		'offerno3' : 'char',
		# 매수증권사코드3
		'bidno3' : 'char',
		# 매도회원사명3
		'offertrad3' : 'char',
		# 매수회원사명3
		'bidtrad3' : 'char',
		# 매도거래량3
		'tradmdvol3' : 'long',
		# 매수거래량3
		'tradmsvol3' : 'long',
		# 매도거래량비중3
		'tradmdrate3' : 'float',
		# 매수거래량비중3
		'tradmsrate3' : 'float',
		# 매도거래량직전대비3
		'tradmdcha3' : 'long',
		# 매수거래량직전대비3
		'tradmscha3' : 'long',
		# 매도증권사코드4
		'offerno4' : 'char',
		# 매수증권사코드4
		'bidno4' : 'char',
		# 매도회원사명4
		'offertrad4' : 'char',
		# 매수회원사명4
		'bidtrad4' : 'char',
		# 매도거래량4
		'tradmdvol4' : 'long',
		# 매수거래량4
		'tradmsvol4' : 'long',
		# 매도거래량비중4
		'tradmdrate4' : 'float',
		# 매수거래량비중4
		'tradmsrate4' : 'float',
		# 매도거래량직전대비4
		'tradmdcha4' : 'long',
		# 매수거래량직전대비4
		'tradmscha4' : 'long',
		# 매도증권사코드5
		'offerno5' : 'char',
		# 매수증권사코드5
		'bidno5' : 'char',
		# 매도회원사명5
		'offertrad5' : 'char',
		# 매수회원사명5
		'bidtrad5' : 'char',
		# 매도거래량5
		'tradmdvol5' : 'long',
		# 매수거래량5
		'tradmsvol5' : 'long',
		# 매도거래량비중5
		'tradmdrate5' : 'float',
		# 매수거래량비중5
		'tradmsrate5' : 'float',
		# 매도거래량직전대비5
		'tradmdcha5' : 'long',
		# 매수거래량직전대비5
		'tradmscha5' : 'long',
		# 외국계증권사매도합계
		'ftradmdvol' : 'char',
		# 외국계증권사매수합계
		'ftradmsvol' : 'char',
		# 외국계증권사매도거래량비중
		'ftradmdrate' : 'float',
		# 외국계증권사매수거래량비중
		'ftradmsrate' : 'float',
		# 외국계증권사매도거래량직전대비
		'ftradmdcha' : 'char',
		# 외국계증권사매수거래량직전대비
		'ftradmscha' : 'char',
		# 단축코드
		'shcode' : 'char'
	}
}

# KOSDAQ체결(K3)
db_outblock_subscription_K3_ = {
	'OutBlock' : {
		# 체결시간
		'chetime' : 'char',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 시가
		'open' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 고가
		'high' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 저가
		'low' : 'long',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 가중평균가
		'w_avrg' : 'long',
		# 매도호가
		'offerho' : 'long',
		# 매수호가
		'bidho' : 'long',
		# 장정보
		'status' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# KOSDAQ프로그램매매종목별(KH)
db_outblock_subscription_KH_ = {
	'OutBlock' : {
		# 수신시간
		'time' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'long',
		# 전일대비
		'change' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 등락율
		'drate' : 'float',
		# 차익매도호가 잔량
		'cdhrem' : 'long',
		# 차익매수호가 잔량
		'cshrem' : 'long',
		# 비차익매도호가 잔량
		'bdhrem' : 'long',
		# 비차익매수호가 잔량
		'bshrem' : 'long',
		# 차익매도호가 수량
		'cdhvolume' : 'long',
		# 차익매수호가 수량
		'cshvolume' : 'long',
		# 비차익매도호가 수량
		'bdhvolume' : 'long',
		# 비차익매수호가 수량
		'bshvolume' : 'long',
		# 전체매도위탁체결수량
		'dwcvolume' : 'long',
		# 전체매수위탁체결수량
		'swcvolume' : 'long',
		# 전체매도자기체결수량
		'djcvolume' : 'long',
		# 전체매수자기체결수량
		'sjcvolume' : 'long',
		# 전체매도체결수량
		'tdvolume' : 'long',
		# 전체매수체결수량
		'tsvolume' : 'long',
		# 전체순매수 수량
		'tvol' : 'long',
		# 전체매도위탁체결금액
		'dwcvalue' : 'long',
		# 전체매수위탁체결금액
		'swcvalue' : 'long',
		# 전체매도자기체결금액
		'djcvalue' : 'long',
		# 전체매수자기체결금액
		'sjcvalue' : 'long',
		# 전체매도체결금액
		'tdvalue' : 'long',
		# 전체매수체결금액
		'tsvalue' : 'long',
		# 전체순매수 금액
		'tval' : 'long',
		# 매도 사전공시수량
		'pdgvolume' : 'long',
		# 매수 사전공시수량
		'psgvolume' : 'long',
		# 종목코드
		'shcode' : 'char'
	}
}

# KOSDAQ프로그램매매전체집계(KM)
db_outblock_subscription_KM_ = {
	'OutBlock' : {
		# 수신시간
		'time' : 'char',
		# 차익매도호가 잔량
		'cdhrem' : 'long',
		# 차익매수호가 잔량
		'cshrem' : 'long',
		# 비차익매도호가 잔량
		'bdhrem' : 'long',
		# 비차익매수호가 잔량
		'bshrem' : 'long',
		# 차익매도호가 수량
		'cdhvolume' : 'long',
		# 차익매수호가 수량
		'cshvolume' : 'long',
		# 비차익매도호가 수량
		'bdhvolume' : 'long',
		# 비차익매수호가 수량
		'bshvolume' : 'long',
		# 차익매도위탁체결수량
		'cdwvolume' : 'long',
		# 차익매도자기체결수량
		'cdjvolume' : 'long',
		# 차익매수위탁체결수량
		'cswvolume' : 'long',
		# 차익매수자기체결수량
		'csjvolume' : 'long',
		# 차익위탁순매수 수량
		'cwvol' : 'long',
		# 차익자기순매수 수량
		'cjvol' : 'long',
		# 비차익매도위탁체결수량
		'bdwvolume' : 'long',
		# 비차익매도자기체결수량
		'bdjvolume' : 'long',
		# 비차익매수위탁체결수량
		'bswvolume' : 'long',
		# 비차익매수자기체결수량
		'bsjvolume' : 'long',
		# 비차익위탁순매수 수량
		'bwvol' : 'long',
		# 비차익자기순매수 수량
		'bjvol' : 'long',
		# 전체매도위탁체결수량
		'dwvolume' : 'long',
		# 전체매수위탁체결수량
		'swvolume' : 'long',
		# 전체위탁순매수 수량
		'wvol' : 'long',
		# 전체매도자기체결수량
		'djvolume' : 'long',
		# 전체매수자기체결수량
		'sjvolume' : 'long',
		# 전체자기순매수 수량
		'jvol' : 'long',
		# 차익매도위탁체결금액
		'cdwvalue' : 'long',
		# 차익매도자기체결금액
		'cdjvalue' : 'long',
		# 차익매수위탁체결금액
		'cswvalue' : 'long',
		# 차익매수자기체결금액
		'csjvalue' : 'long',
		# 차익위탁순매수 금액
		'cwval' : 'long',
		# 차익자기순매수 금액
		'cjval' : 'long',
		# 비차익매도위탁체결금액
		'bdwvalue' : 'long',
		# 비차익매도자기체결금액
		'bdjvalue' : 'long',
		# 비차익매수위탁체결금액
		'bswvalue' : 'long',
		# 비차익매수자기체결금액
		'bsjvalue' : 'long',
		# 비차익위탁순매수 금액
		'bwval' : 'long',
		# 비차익자기순매수 금액
		'bjval' : 'long',
		# 전체매도위탁체결금액
		'dwvalue' : 'long',
		# 전체매수위탁체결금액
		'swvalue' : 'long',
		# 전체위탁순매수 금액
		'wval' : 'long',
		# 전체매도자기체결금액
		'djvalue' : 'long',
		# 전체매수자기체결금액
		'sjvalue' : 'long',
		# 전체자기순매수 금액
		'jval' : 'long',
		# KOSDAQ50 지수
		'k50jisu' : 'float',
		# KOSDAQ50 전일대비구분
		'k50sign' : 'char',
		# KOSDAQ50 전일대비
		'change' : 'float',
		# KOSDAQ50 베이시스
		'k50basis' : 'float',
		# 차익매도체결수량합계
		'cdvolume' : 'long',
		# 차익매수체결수량합계
		'csvolume' : 'long',
		# 차익순매수 수량합계
		'cvol' : 'long',
		# 비차익매도체결수량합계
		'bdvolume' : 'long',
		# 비차익매수체결수량합계
		'bsvolume' : 'long',
		# 비차익순매수 수량합계
		'bvol' : 'long',
		# 전체매도체결수량합계
		'tdvolume' : 'long',
		# 전체매수체결수량합계
		'tsvolume' : 'long',
		# 전체순매수 수량합계
		'tvol' : 'long',
		# 차익매도체결금액합계
		'cdvalue' : 'long',
		# 차익매수체결금액합계
		'csvalue' : 'long',
		# 차익순매수 금액합계
		'cval' : 'long',
		# 비차익매도체결금액합계
		'bdvalue' : 'long',
		# 비차익매수체결금액합계
		'bsvalue' : 'long',
		# 비차익순매수 금액합계
		'bval' : 'long',
		# 전체매도체결금액합계
		'tdvalue' : 'long',
		# 전체매수체결금액합계
		'tsvalue' : 'long',
		# 전체순매수 금액합계
		'tval' : 'long',
		# 차익매도체결수량직전대비
		'p_cdvolcha' : 'long',
		# 차익매수체결수량직전대비
		'p_csvolcha' : 'long',
		# 차익순매수 수량직전대비
		'p_cvolcha' : 'long',
		# 비차익매도체결수량직전대비
		'p_bdvolcha' : 'long',
		# 비차익매수체결수량직전대비
		'p_bsvolcha' : 'long',
		# 비차익순매수 수량직전대비
		'p_bvolcha' : 'long',
		# 전체매도체결수량직전대비
		'p_tdvolcha' : 'long',
		# 전체매수체결수량직전대비
		'p_tsvolcha' : 'long',
		# 전체순매수 수량직전대비
		'p_tvolcha' : 'long',
		# 차익매도체결금액직전대비
		'p_cdvalcha' : 'long',
		# 차익매수체결금액직전대비
		'p_csvalcha' : 'long',
		# 차익순매수 금액직전대비
		'p_cvalcha' : 'long',
		# 비차익매도체결금액직전대비
		'p_bdvalcha' : 'long',
		# 비차익매수체결금액직전대비
		'p_bsvalcha' : 'long',
		# 비차익순매수 금액직전대비
		'p_bvalcha' : 'long',
		# 전체매도체결금액직전대비
		'p_tdvalcha' : 'long',
		# 전체매수체결금액직전대비
		'p_tsvalcha' : 'long',
		# 전체순매수 금액직전대비
		'p_tvalcha' : 'long',
		# 구분값
		'gubun' : 'char'
	}
}

# KOSDAQ우선호가(KS)
db_outblock_subscription_KS_ = {
	'OutBlock' : {
		# 매도호가
		'offerho' : 'long',
		# 매수호가
		'bidho' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# US지수(MK2)
db_outblock_subscription_MK2 = {
	'OutBlock' : {
		# 일자
		'date' : 'char',
		# 시간
		'time' : 'char',
		# 한국일자
		'kodate' : 'char',
		# 한국시간
		'kotime' : 'char',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'uprate' : 'float',
		# 매수호가
		'bidho' : 'float',
		# 매수잔량
		'bidrem' : 'long',
		# 매도호가
		'offerho' : 'float',
		# 매도잔량
		'offerrem' : 'long',
		# 누적거래량
		'volume' : 'float',
		# 심벌
		'xsymbol' : 'char',
		# 체결거래량
		'cvolume' : 'float'
	}
}

# 파생상품증거금율조회
db_outblock_query_MMDAQ91200 = {
	'MMDAQ91200OutBlock1' : {
		# 레코드갯수
		'RecCnt' : 'long',
		# 종목대분류코드
		'IsuLgclssCode' : 'char',
		# 종목중분류코드
		'IsuMdclssCode' : 'char'
	},
	'MMDAQ91200OutBlock2' : [
		{
			# 종목소분류코드
			'IsuSmclssCode' : 'char',
			# 종목중분류코드
			'IsuMdclssCode' : 'char',
			# 종목대중분류명
			'IsuLrgMdclssNm' : 'char',
			# 종목대중소분류명
			'IsuLrgMidSmclssNm' : 'char',
			# 단축한글종목명
			'ShtnHanglIsuNm' : 'char',
			# 위탁증거금율
			'CsgnMgnrt' : 'double',
			# 유지증거금율
			'MaintMgnrt' : 'double',
			# 현금증거금율
			'MnyMgnrt' : 'double',
			# 잔여일수
			'RmndDays' : 'long'
		}
	]
}

# CME연계KP200지수선물체결(NC0)
db_outblock_subscription_NC0 = {
	'OutBlock' : {
		# 체결시간(24시간)
		'chetime' : 'char',
		# 체결시간(36시간)
		'chetime1' : 'char',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'float',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 미결제약정수량
		'openyak' : 'long',
		# KOSPI200지수
		'k200jisu' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 괴리율
		'kasis' : 'float',
		# 시장BASIS
		'sbasis' : 'float',
		# 이론BASIS
		'ibasis' : 'float',
		# 미결제약정증감
		'openyakcha' : 'long',
		# 장운영정보
		'jgubun' : 'char',
		# 미사용filler
		'jnilvolume' : 'long',
		# 단축코드
		'futcode' : 'char'
	}
}

# CME연계KP200지수선물호가(NH0)
db_outblock_subscription_NH0 = {
	'OutBlock' : {
		# 호가시간(24시간)
		'hotime' : 'char',
		# 호가시간(36시간)
		'hotime1' : 'char',
		# 매도호가1
		'offerho1' : 'double',
		# 매수호가1
		'bidho1' : 'double',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'offercnt1' : 'long',
		# 매수호가건수1
		'bidcnt1' : 'long',
		# 매도호가2
		'offerho2' : 'double',
		# 매수호가2
		'bidho2' : 'double',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'offercnt2' : 'long',
		# 매수호가건수2
		'bidcnt2' : 'long',
		# 매도호가3
		'offerho3' : 'double',
		# 매수호가3
		'bidho3' : 'double',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'offercnt3' : 'long',
		# 매수호가건수3
		'bidcnt3' : 'long',
		# 매도호가4
		'offerho4' : 'double',
		# 매수호가4
		'bidho4' : 'double',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'offercnt4' : 'long',
		# 매수호가건수4
		'bidcnt4' : 'long',
		# 매도호가5
		'offerho5' : 'double',
		# 매수호가5
		'bidho5' : 'double',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'offercnt5' : 'long',
		# 매수호가건수5
		'bidcnt5' : 'long',
		# 매도호가총수량
		'totofferrem' : 'long',
		# 매수호가총수량
		'totbidrem' : 'long',
		# 매도호가총건수
		'totoffercnt' : 'long',
		# 매수호가총건수
		'totbidcnt' : 'long',
		# 단축코드
		'futcode' : 'char'
	}
}

# 실시간 뉴스 제목 패킷(NWS)
db_outblock_subscription_NWS = {
	'OutBlock' : {
		# 날짜
		'date' : 'char',
		# 시간
		'time' : 'char',
		# 뉴스구분자
		'id' : 'char',
		# 키값
		'realkey' : 'char',
		# 제목
		'title' : 'char',
		# 단축종목코드
		'code' : 'char',
		# BODY길이
		'bodysize' : 'long'
	}
}

# 선물접수
db_outblock_subscription_O01 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# tr코드
		'trcode1' : 'char',
		# 회사번호
		'firmno' : 'char',
		# 계좌번호
		'acntno' : 'char',
		# 계좌번호
		'acntno1' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 지점번호
		'brnno' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문번호
		'ordno1' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno1' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 모주문번호
		'prntordno' : 'char',
		# 모주문번호
		'prntordno1' : 'long',
		# 종목번호
		'isuno' : 'char',
		# 선물옵션종목번호
		'fnoIsuno' : 'char',
		# 선물옵션종목명
		'fnoIsunm' : 'char',
		# 상품군분류코드
		'pdgrpcode' : 'char',
		# 선물옵션종목유형구분
		'fnoIsuptntp' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 정정취소구분
		'mrctp' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 호가유형코드
		'hogatype' : 'char',
		# 거래유형코드
		'mmgb' : 'char',
		# 주문가격
		'ordprc' : 'double',
		# 미체결수량
		'unercqty' : 'long',
		# 통신매체
		'commdacode' : 'char',
		# 수수료합산코드
		'peeamtcode' : 'char',
		# 관리사원
		'mgempno' : 'char',
		# 선물옵션거래단위금액
		'fnotrdunitamt' : 'double',
		# 처리시각
		'trxtime' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'char',
		# 포트폴리오 번호
		'ptflno' : 'char',
		# 바스켓번호
		'bskno' : 'char',
		# 트렌치번호
		'trchno' : 'char',
		# 아이템번호
		'Itemno' : 'char',
		# 주문자Id
		'userId' : 'char',
		# 운영지시번호
		'opdrtnno' : 'char',
		# 부적격코드
		'rjtcode' : 'char',
		# 정정취소확인수량
		'mrccnfqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정취소수량
		'orgordmrcqty' : 'long',
		# 약정시각(체결시각)
		'ctrcttime' : 'char',
		# 약정번호
		'ctrctno' : 'char',
		# 체결가격
		'execprc' : 'double',
		# 체결수량
		'execqty' : 'long',
		# 신규체결수량
		'newqty' : 'long',
		# 청산체결수량
		'qdtqty' : 'long',
		# 최종결제수량
		'lastqty' : 'long',
		# 전체체결수량
		'lallexecqty' : 'long',
		# 전체체결금액
		'allexecamt' : 'long',
		# 잔고평가구분
		'fnobalevaltp' : 'char',
		# 매매손익금액
		'bnsplamt' : 'long',
		# 선물옵션종목번호1
		'fnoIsuno1' : 'char',
		# 매매구분1
		'bnstp1' : 'char',
		# 체결가1
		'execprc1' : 'double',
		# 신규체결수량1
		'newqty1' : 'long',
		# 청산체결수량1
		'qdtqty1' : 'long',
		# 전체체결금액1
		'allexecamt1' : 'long',
		# 선물옵션종목번호2
		'fnoIsuno2' : 'char',
		# 매매구분2
		'bnstp2' : 'char',
		# 체결가2
		'execprc2' : 'double',
		# 신규체결수량2
		'newqty2' : 'long',
		# 청산체결수량2
		'lqdtqty2' : 'long',
		# 전체체결금액2
		'allexecamt2' : 'long',
		# 예수금
		'dps' : 'long',
		# 선물대용지정금액
		'ftsubtdsgnamt' : 'long',
		# 증거금
		'mgn' : 'long',
		# 증거금현금
		'mnymgn' : 'long',
		# 주문가능금액
		'ordableamt' : 'long',
		# 주문가능현금액
		'mnyordableamt' : 'long',
		# 잔고 종목번호1
		'fnoIsuno_1' : 'char',
		# 잔고 매매구분1
		'bnstp_1' : 'char',
		# 미결제수량1
		'unsttqty_1' : 'long',
		# 주문가능수량1
		'lqdtableqty_1' : 'long',
		# 평균가1
		'avrprc_1' : 'double',
		# 잔고 종목번호2
		'fnoIsuno_2' : 'char',
		# 잔고 매매구분2
		'bnstp_2' : 'char',
		# 미결제수량2
		'unsttqty_2' : 'long',
		# 주문가능수량2
		'lqdtableqty_2' : 'long',
		# 평균가2
		'avrprc_2' : 'double'
	}
}

# KOSPI200옵션체결(C0)
db_outblock_subscription_OC0 = {
	'OutBlock' : {
		# 체결시간
		'chetime' : 'char',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'float',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 미결제약정수량
		'openyak' : 'long',
		# KOSPI200지수
		'k200jisu' : 'float',
		# KOSPI등가
		'eqva' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 미결제약정증감
		'openyakcha' : 'long',
		# 시간가치
		'timevalue' : 'float',
		# 장운영정보
		'jgubun' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 단축코드
		'optcode' : 'char'
	}
}

# KOSPI200옵션실시간상하한가(D0)
db_outblock_subscription_OD0 = {
	'OutBlock' : {
		# 접속매매여부
		'gubun' : 'char',
		# 실시간가격제한여부
		'dy_gubun' : 'char',
		# 실시간상한가
		'dy_uplmtprice' : 'float',
		# 실시간하한가
		'dy_dnlmtprice' : 'float',
		# 단축코드
		'opttcode' : 'char'
	}
}

# KOSPI200옵션호가(H0)
db_outblock_subscription_OH0 = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 매도호가1
		'offerho1' : 'double',
		# 매수호가1
		'bidho1' : 'double',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'offercnt1' : 'long',
		# 매수호가건수1
		'bidcnt1' : 'long',
		# 매도호가2
		'offerho2' : 'double',
		# 매수호가2
		'bidho2' : 'double',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'offercnt2' : 'long',
		# 매수호가건수2
		'bidcnt2' : 'long',
		# 매도호가3
		'offerho3' : 'double',
		# 매수호가3
		'bidho3' : 'double',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'offercnt3' : 'long',
		# 매수호가건수3
		'bidcnt3' : 'long',
		# 매도호가4
		'offerho4' : 'double',
		# 매수호가4
		'bidho4' : 'double',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'offercnt4' : 'long',
		# 매수호가건수4
		'bidcnt4' : 'long',
		# 매도호가5
		'offerho5' : 'double',
		# 매수호가5
		'bidho5' : 'double',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'offercnt5' : 'long',
		# 매수호가건수5
		'bidcnt5' : 'long',
		# 매도호가총수량
		'totofferrem' : 'long',
		# 매수호가총수량
		'totbidrem' : 'long',
		# 매도호가총건수
		'totoffercnt' : 'long',
		# 매수호가총건수
		'totbidcnt' : 'long',
		# 단축코드
		'optcode' : 'char',
		# 단일가호가여부
		'danhochk' : 'char',
		# 배분적용구분
		'alloc_gubun' : 'char'
	}
}

# KOSDAQ거래원(OK)
db_outblock_subscription_OK_ = {
	'OutBlock' : {
		# 매도증권사코드1
		'offerno1' : 'char',
		# 매수증권사코드1
		'bidno1' : 'char',
		# 매도회원사명1
		'offertrad1' : 'char',
		# 매수회원사명1
		'bidtrad1' : 'char',
		# 매도거래량1
		'tradmdvol1' : 'long',
		# 매수거래량1
		'tradmsvol1' : 'long',
		# 매도거래량비중1
		'tradmdrate1' : 'float',
		# 매도거래량비중1
		'tradmsrate1' : 'float',
		# 매도거래량직전대비1
		'tradmdcha1' : 'long',
		# 매수거래량직전대비1
		'tradmscha1' : 'long',
		# 매도증권사코드2
		'offerno2' : 'char',
		# 매수증권사코드2
		'bidno2' : 'char',
		# 매도회원사명2
		'offertrad2' : 'char',
		# 매수회원사명2
		'bidtrad2' : 'char',
		# 매도거래량2
		'tradmdvol2' : 'long',
		# 매수거래량2
		'tradmsvol2' : 'long',
		# 매도거래량비중2
		'tradmdrate2' : 'float',
		# 매수거래량비중2
		'tradmsrate2' : 'float',
		# 매도거래량직전대비2
		'tradmdcha2' : 'long',
		# 매수거래량직전대비2
		'tradmscha2' : 'long',
		# 매도증권사코드3
		'offerno3' : 'char',
		# 매수증권사코드3
		'bidno3' : 'char',
		# 매도회원사명3
		'offertrad3' : 'char',
		# 매수회원사명3
		'bidtrad3' : 'char',
		# 매도거래량3
		'tradmdvol3' : 'long',
		# 매수거래량3
		'tradmsvol3' : 'long',
		# 매도거래량비중3
		'tradmdrate3' : 'float',
		# 매수거래량비중3
		'tradmsrate3' : 'float',
		# 매도거래량직전대비3
		'tradmdcha3' : 'long',
		# 매수거래량직전대비3
		'tradmscha3' : 'long',
		# 매도증권사코드4
		'offerno4' : 'char',
		# 매수증권사코드4
		'bidno4' : 'char',
		# 매도회원사명4
		'offertrad4' : 'char',
		# 매수회원사명4
		'bidtrad4' : 'char',
		# 매도거래량4
		'tradmdvol4' : 'long',
		# 매수거래량4
		'tradmsvol4' : 'long',
		# 매도거래량비중4
		'tradmdrate4' : 'float',
		# 매수거래량비중4
		'tradmsrate4' : 'float',
		# 매도거래량직전대비4
		'tradmdcha4' : 'long',
		# 매수거래량직전대비4
		'tradmscha4' : 'long',
		# 매도증권사코드5
		'offerno5' : 'char',
		# 매수증권사코드5
		'bidno5' : 'char',
		# 매도회원사명5
		'offertrad5' : 'char',
		# 매수회원사명5
		'bidtrad5' : 'char',
		# 매도거래량5
		'tradmdvol5' : 'long',
		# 매수거래량5
		'tradmsvol5' : 'long',
		# 매도거래량비중5
		'tradmdrate5' : 'float',
		# 매수거래량비중5
		'tradmsrate5' : 'float',
		# 매도거래량직전대비5
		'tradmdcha5' : 'long',
		# 매수거래량직전대비5
		'tradmscha5' : 'long',
		# 외국계증권사매도합계
		'ftradmdvol' : 'char',
		# 외국계증권사매수합계
		'ftradmsvol' : 'char',
		# 외국계증권사매도거래량비중
		'ftradmdrate' : 'float',
		# 외국계증권사매수거래량비중
		'ftradmsrate' : 'float',
		# 외국계증권사매도거래량직전대비
		'ftradmdcha' : 'char',
		# 외국계증권사매수거래량직전대비
		'ftradmscha' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 매도거래대금1
		'tradmdval1' : 'long',
		# 매수거래대금1
		'tradmsval1' : 'long',
		# 매도평균단가1
		'tradmdavg1' : 'long',
		# 매수평균단가1
		'tradmsavg1' : 'long',
		# 매도거래대금2
		'tradmdval2' : 'long',
		# 매수거래대금2
		'tradmsval2' : 'long',
		# 매도평균단가2
		'tradmdavg2' : 'long',
		# 매수평균단가2
		'tradmsavg2' : 'long',
		# 매도거래대금3
		'tradmdval3' : 'long',
		# 매수거래대금3
		'tradmsval3' : 'long',
		# 매도평균단가3
		'tradmdavg3' : 'long',
		# 매수평균단가3
		'tradmsavg3' : 'long',
		# 매도거래대금4
		'tradmdval4' : 'long',
		# 매수거래대금4
		'tradmsval4' : 'long',
		# 매도평균단가4
		'tradmdavg4' : 'long',
		# 매수평균단가4
		'tradmsavg4' : 'long',
		# 매도거래대금5
		'tradmdval5' : 'long',
		# 매수거래대금5
		'tradmsval5' : 'long',
		# 매도평균단가5
		'tradmdavg5' : 'long',
		# 매수평균단가5
		'tradmsavg5' : 'long',
		# 외국계증권사매도거래대금
		'ftradmdval' : 'long',
		# 외국계증권사매수거래대금
		'ftradmsval' : 'long',
		# 외국계증권사매도평균단가
		'ftradmdavg' : 'long',
		# 외국계증권사매수평균단가
		'ftradmsavg' : 'long'
	}
}

# KOSPI200옵션민감도(MG)
db_outblock_subscription_OMG = {
	'OutBlock' : {
		# 체결시간
		'chetime' : 'char',
		# 행사가
		'actprice' : 'float',
		# KOSPI200지수
		'k200jisu' : 'float',
		# 선물가격
		'fut200jisu' : 'float',
		# 현재가
		'price' : 'float',
		# 대표내재변동성
		'capimpv' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 델타(블랙숄즈)
		'delt' : 'float',
		# 감마(블랙숄즈)
		'gama' : 'float',
		# 세타(블랙숄즈)
		'ceta' : 'float',
		# 베가(블랙숄즈)
		'vega' : 'float',
		# 로우(블랙숄즈)
		'rhox' : 'float',
		# 이론가(블랙숄즈)
		'theoryprice' : 'float',
		# 전일가내재변동성
		'bimpv' : 'float',
		# 매도가내재변동성
		'offerimpv' : 'float',
		# 매수가내재변동성
		'bidimpv' : 'float',
		# 옵션코드
		'optcode' : 'char'
	}
}

# KOSPI프로그램매매종목별(PH)
db_outblock_subscription_PH_ = {
	'OutBlock' : {
		# 수신시간
		'time' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'long',
		# 전일대비
		'change' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 등락율
		'drate' : 'float',
		# 차익매도호가 잔량
		'cdhrem' : 'long',
		# 차익매수호가 잔량
		'cshrem' : 'long',
		# 비차익매도호가 잔량
		'bdhrem' : 'long',
		# 비차익매수호가 잔량
		'bshrem' : 'long',
		# 차익매도호가 수량
		'cdhvolume' : 'long',
		# 차익매수호가 수량
		'cshvolume' : 'long',
		# 비차익매도호가 수량
		'bdhvolume' : 'long',
		# 비차익매수호가 수량
		'bshvolume' : 'long',
		# 전체매도위탁체결수량
		'dwcvolume' : 'long',
		# 전체매수위탁체결수량
		'swcvolume' : 'long',
		# 전체매도자기체결수량
		'djcvolume' : 'long',
		# 전체매수자기체결수량
		'sjcvolume' : 'long',
		# 전체매도체결수량
		'tdvolume' : 'long',
		# 전체매수체결수량
		'tsvolume' : 'long',
		# 전체순매수 수량
		'tvol' : 'long',
		# 전체매도위탁체결금액
		'dwcvalue' : 'long',
		# 전체매수위탁체결금액
		'swcvalue' : 'long',
		# 전체매도자기체결금액
		'djcvalue' : 'long',
		# 전체매수자기체결금액
		'sjcvalue' : 'long',
		# 전체매도체결금액
		'tdvalue' : 'long',
		# 전체매수체결금액
		'tsvalue' : 'long',
		# 전체순매수 금액
		'tval' : 'long',
		# 매도 사전공시수량
		'pdgvolume' : 'long',
		# 매수 사전공시수량
		'psgvolume' : 'long',
		# 종목코드
		'shcode' : 'char'
	}
}

# KOSPI프로그램매매전체집계(PM)
db_outblock_subscription_PM_ = {
	'OutBlock' : {
		# 수신시간
		'time' : 'char',
		# 차익매도호가 잔량
		'cdhrem' : 'long',
		# 차익매수호가 잔량
		'cshrem' : 'long',
		# 비차익매도호가 잔량
		'bdhrem' : 'long',
		# 비차익매수호가 잔량
		'bshrem' : 'long',
		# 차익매도호가 수량
		'cdhvolume' : 'long',
		# 차익매수호가 수량
		'cshvolume' : 'long',
		# 비차익매도호가 수량
		'bdhvolume' : 'long',
		# 비차익매수호가 수량
		'bshvolume' : 'long',
		# 차익매도위탁체결수량
		'cdwvolume' : 'long',
		# 차익매도자기체결수량
		'cdjvolume' : 'long',
		# 차익매수위탁체결수량
		'cswvolume' : 'long',
		# 차익매수자기체결수량
		'csjvolume' : 'long',
		# 차익위탁순매수 수량
		'cwvol' : 'long',
		# 차익자기순매수 수량
		'cjvol' : 'long',
		# 비차익매도위탁체결수량
		'bdwvolume' : 'long',
		# 비차익매도자기체결수량
		'bdjvolume' : 'long',
		# 비차익매수위탁체결수량
		'bswvolume' : 'long',
		# 비차익매수자기체결수량
		'bsjvolume' : 'long',
		# 비차익위탁순매수 수량
		'bwvol' : 'long',
		# 비차익자기순매수 수량
		'bjvol' : 'long',
		# 전체매도위탁체결수량
		'dwvolume' : 'long',
		# 전체매수위탁체결수량
		'swvolume' : 'long',
		# 전체위탁순매수 수량
		'wvol' : 'long',
		# 전체매도자기체결수량
		'djvolume' : 'long',
		# 전체매수자기체결수량
		'sjvolume' : 'long',
		# 전체자기순매수 수량
		'jvol' : 'long',
		# 차익매도위탁체결금액
		'cdwvalue' : 'long',
		# 차익매도자기체결금액
		'cdjvalue' : 'long',
		# 차익매수위탁체결금액
		'cswvalue' : 'long',
		# 차익매수자기체결금액
		'csjvalue' : 'long',
		# 차익위탁순매수 금액
		'cwval' : 'long',
		# 차익자기순매수 금액
		'cjval' : 'long',
		# 비차익매도위탁체결금액
		'bdwvalue' : 'long',
		# 비차익매도자기체결금액
		'bdjvalue' : 'long',
		# 비차익매수위탁체결금액
		'bswvalue' : 'long',
		# 비차익매수자기체결금액
		'bsjvalue' : 'long',
		# 비차익위탁순매수 금액
		'bwval' : 'long',
		# 비차익자기순매수 금액
		'bjval' : 'long',
		# 전체매도위탁체결금액
		'dwvalue' : 'long',
		# 전체매수위탁체결금액
		'swvalue' : 'long',
		# 전체위탁순매수 금액
		'wval' : 'long',
		# 전체매도자기체결금액
		'djvalue' : 'long',
		# 전체매수자기체결금액
		'sjvalue' : 'long',
		# 전체자기순매수 금액
		'jval' : 'long',
		# KOSPI200 지수
		'k200jisu' : 'float',
		# KOSPI200 전일대비구분
		'k200sign' : 'char',
		# KOSPI200 전일대비
		'change' : 'float',
		# KOSPI200 베이시스
		'k200basis' : 'float',
		# 차익매도체결수량합계
		'cdvolume' : 'long',
		# 차익매수체결수량합계
		'csvolume' : 'long',
		# 차익순매수 수량합계
		'cvol' : 'long',
		# 비차익매도체결수량합계
		'bdvolume' : 'long',
		# 비차익매수체결수량합계
		'bsvolume' : 'long',
		# 비차익순매수 수량합계
		'bvol' : 'long',
		# 전체매도체결수량합계
		'tdvolume' : 'long',
		# 전체매수체결수량합계
		'tsvolume' : 'long',
		# 전체순매수 수량합계
		'tvol' : 'long',
		# 차익매도체결금액합계
		'cdvalue' : 'long',
		# 차익매수체결금액합계
		'csvalue' : 'long',
		# 차익순매수 금액합계
		'cval' : 'long',
		# 비차익매도체결금액합계
		'bdvalue' : 'long',
		# 비차익매수체결금액합계
		'bsvalue' : 'long',
		# 비차익순매수 금액합계
		'bval' : 'long',
		# 전체매도체결금액합계
		'tdvalue' : 'long',
		# 전체매수체결금액합계
		'tsvalue' : 'long',
		# 전체순매수 금액합계
		'tval' : 'long',
		# 차익매도체결수량직전대비
		'p_cdvolcha' : 'long',
		# 차익매수체결수량직전대비
		'p_csvolcha' : 'long',
		# 차익순매수 수량직전대비
		'p_cvolcha' : 'long',
		# 비차익매도체결수량직전대비
		'p_bdvolcha' : 'long',
		# 비차익매수체결수량직전대비
		'p_bsvolcha' : 'long',
		# 비차익순매수 수량직전대비
		'p_bvolcha' : 'long',
		# 전체매도체결수량직전대비
		'p_tdvolcha' : 'long',
		# 전체매수체결수량직전대비
		'p_tsvolcha' : 'long',
		# 전체순매수 수량직전대비
		'p_tvolcha' : 'long',
		# 차익매도체결금액직전대비
		'p_cdvalcha' : 'long',
		# 차익매수체결금액직전대비
		'p_csvalcha' : 'long',
		# 차익순매수 금액직전대비
		'p_cvalcha' : 'long',
		# 비차익매도체결금액직전대비
		'p_bdvalcha' : 'long',
		# 비차익매수체결금액직전대비
		'p_bsvalcha' : 'long',
		# 비차익순매수 금액직전대비
		'p_bvalcha' : 'long',
		# 전체매도체결금액직전대비
		'p_tdvalcha' : 'long',
		# 전체매수체결금액직전대비
		'p_tsvalcha' : 'long',
		# 전체순매수 금액직전대비
		'p_tvalcha' : 'long',
		# 구분값
		'gubun' : 'char'
	}
}

# KOSPI우선호가(S2)
db_outblock_subscription_S2_ = {
	'OutBlock' : {
		# 매도호가
		'offerho' : 'long',
		# 매수호가
		'bidho' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# ELW우선호가(s2)
db_outblock_subscription_s2_4ELW = {
	'OutBlock' : {
		# 매도호가
		'offerho' : 'long',
		# 매수호가
		'bidho' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# KOSPI체결(S3)
db_outblock_subscription_S3_ = {
	'OutBlock' : {
		# 체결시간
		'chetime' : 'char',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 시가
		'open' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 고가
		'high' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 저가
		'low' : 'long',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 가중평균가
		'w_avrg' : 'long',
		# 매도호가
		'offerho' : 'long',
		# 매수호가
		'bidho' : 'long',
		# 장정보
		'status' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# ELW체결(s3)
db_outblock_subscription_s3_4ELW = {
	'OutBlock' : {
		# 체결시간
		'chetime' : 'char',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 시가
		'open' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 고가
		'high' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 저가
		'low' : 'long',
		# 체결구분
		'cgubun' : 'char',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 누적거래대금
		'value' : 'long',
		# 매도누적체결량
		'mdvolume' : 'long',
		# 매도누적체결건수
		'mdchecnt' : 'long',
		# 매수누적체결량
		'msvolume' : 'long',
		# 매수누적체결건수
		'mschecnt' : 'long',
		# 체결강도
		'cpower' : 'float',
		# 가중평균가
		'w_avrg' : 'long',
		# 매도호가
		'offerho' : 'long',
		# 매수호가
		'bidho' : 'long',
		# 장정보
		'status' : 'char',
		# 전일동시간대거래량
		'jnilvolume' : 'long',
		# 프리미엄
		'premium' : 'float',
		# ATM구분
		'moneyness' : 'char',
		# 단축코드
		'shcode' : 'char',
		# LP보유수량
		'lpvolume' : 'long'
	}
}

# KOSPI기세(S4)
db_outblock_subscription_S4_ = {
	'OutBlock' : {
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 시가
		'open' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 고가
		'high' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 저가
		'low' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# ELW기세(s4)
db_outblock_subscription_s4_ELW = {
	'OutBlock' : {
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 현재가
		'price' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 시가
		'open' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 고가
		'high' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 저가
		'low' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# 주식주문접수
db_outblock_subscription_SC0 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# 주문체결구분
		'ordchegb' : 'char',
		# 시장구분
		'marketgb' : 'char',
		# 주문구분
		'ordgb' : 'char',
		# 원주문번호
		'orgordno' : 'long',
		# 계좌번호
		'accno1' : 'char',
		# 계좌번호
		'accno2' : 'char',
		# 비밀번호
		'passwd' : 'char',
		# 종목번호
		'expcode' : 'char',
		# 단축종목번호
		'shtcode' : 'char',
		# 종목명
		'hname' : 'char',
		# 주문수량
		'ordqty' : 'long',
		# 주문가격
		'ordprice' : 'long',
		# 주문조건
		'hogagb' : 'char',
		# 호가유형코드
		'etfhogagb' : 'char',
		# 프로그램호가구분
		'pgmtype' : 'long',
		# 공매도호가구분
		'gmhogagb' : 'long',
		# 공매도가능여부
		'gmhogayn' : 'long',
		# 신용구분
		'singb' : 'char',
		# 대출일
		'loandt' : 'char',
		# 반대매매주문구분
		'cvrgordtp' : 'char',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹ID
		'groupid' : 'char',
		# 주문회차
		'ordseqno' : 'long',
		# 포트폴리오번호
		'prtno' : 'long',
		# 바스켓번호
		'basketno' : 'long',
		# 트렌치번호
		'trchno' : 'long',
		# 아아템번호
		'itemno' : 'long',
		# 차입구분
		'brwmgmyn' : 'long',
		# 회원사번호
		'mbrno' : 'long',
		# 처리구분
		'procgb' : 'char',
		# 관리지점번호
		'admbrchno' : 'char',
		# 선물계좌번호
		'futaccno' : 'char',
		# 선물상품구분
		'futmarketgb' : 'char',
		# 통신매체구분
		'tongsingb' : 'char',
		# 유동성공급자구분
		'lpgb' : 'char',
		# DUMMY
		'dummy' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 주문시각
		'ordtm' : 'char',
		# 모주문번호
		'prntordno' : 'long',
		# 관리사원번호
		'mgempno' : 'char',
		# 원주문미체결수량
		'orgordundrqty' : 'long',
		# 원주문정정수량
		'orgordmdfyqty' : 'long',
		# 원주문취소수량
		'ordordcancelqty' : 'long',
		# 비회원사송신번호
		'nmcpysndno' : 'long',
		# 주문금액
		'ordamt' : 'long',
		# 매매구분
		'bnstp' : 'char',
		# 예비주문번호
		'spareordno' : 'long',
		# 반대매매일련번호
		'cvrgseqno' : 'long',
		# 예약주문번호
		'rsvordno' : 'long',
		# 복수주문일련번호
		'mtordseqno' : 'long',
		# 예비주문수량
		'spareordqty' : 'long',
		# 주문사원번호
		'orduserid' : 'char',
		# 실물주문수량
		'spotordqty' : 'long',
		# 재사용주문수량
		'ordruseqty' : 'long',
		# 현금주문금액
		'mnyordamt' : 'long',
		# 주문대용금액
		'ordsubstamt' : 'long',
		# 재사용주문금액
		'ruseordamt' : 'long',
		# 수수료주문금액
		'ordcmsnamt' : 'long',
		# 사용신용담보재사용금
		'crdtuseamt' : 'long',
		# 잔고수량
		'secbalqty' : 'long',
		# 실물가능수량
		'spotordableqty' : 'long',
		# 재사용가능수량(매도)
		'ordableruseqty' : 'long',
		# 변동수량
		'flctqty' : 'long',
		# 잔고수량(D2)
		'secbalqtyd2' : 'long',
		# 매도주문가능수량
		'sellableqty' : 'long',
		# 미체결매도주문수량
		'unercsellordqty' : 'long',
		# 평균매입가
		'avrpchsprc' : 'long',
		# 매입금액
		'pchsamt' : 'long',
		# 예수금
		'deposit' : 'long',
		# 대용금
		'substamt' : 'long',
		# 위탁증거금현금
		'csgnmnymgn' : 'long',
		# 위탁증거금대용
		'csgnsubstmgn' : 'long',
		# 신용담보재사용금
		'crdtpldgruseamt' : 'long',
		# 주문가능현금
		'ordablemny' : 'long',
		# 주문가능대용
		'ordablesubstamt' : 'long',
		# 재사용가능금액
		'ruseableamt' : 'long'
	}
}

# 주식주문체결
db_outblock_subscription_SC1 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# 주문체결유형코드
		'ordxctptncode' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문유형코드
		'ordptncode' : 'char',
		# 관리지점번호
		'mgmtbrnno' : 'char',
		# 계좌번호
		'accno1' : 'char',
		# 계좌번호
		'accno2' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 종목번호
		'Isuno' : 'char',
		# 종목명
		'Isunm' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno' : 'long',
		# 체결번호
		'execno' : 'long',
		# 주문수량
		'ordqty' : 'long',
		# 주문가격
		'ordprc' : 'long',
		# 체결수량
		'execqty' : 'long',
		# 체결가격
		'execprc' : 'long',
		# 정정확인수량
		'mdfycnfqty' : 'long',
		# 정정확인가격
		'mdfycnfprc' : 'long',
		# 취소확인수량
		'canccnfqty' : 'long',
		# 거부수량
		'rjtqty' : 'long',
		# 주문처리유형코드
		'ordtrxptncode' : 'long',
		# 복수주문일련번호
		'mtiordseqno' : 'long',
		# 주문조건
		'ordcndi' : 'char',
		# 호가유형코드
		'ordprcptncode' : 'char',
		# 비저축체결수량
		'nsavtrdqty' : 'long',
		# 단축종목번호
		'shtnIsuno' : 'char',
		# 운용지시번호
		'opdrtnno' : 'char',
		# 반대매매주문구분
		'cvrgordtp' : 'char',
		# 미체결수량(주문)
		'unercqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정수량
		'orgordmdfyqty' : 'long',
		# 원주문취소수량
		'orgordcancqty' : 'long',
		# 주문평균체결가격
		'ordavrexecprc' : 'long',
		# 주문금액
		'ordamt' : 'long',
		# 표준종목번호
		'stdIsuno' : 'char',
		# 전표준종목번호
		'bfstdIsuno' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 주문거래유형코드
		'ordtrdptncode' : 'char',
		# 신용거래코드
		'mgntrncode' : 'char',
		# 수수료합산코드
		'adduptp' : 'char',
		# 통신매체코드
		'commdacode' : 'char',
		# 대출일
		'Loandt' : 'char',
		# 회원/비회원사번호
		'mbrnmbrno' : 'long',
		# 주문계좌번호
		'ordacntno' : 'char',
		# 집계지점번호
		'agrgbrnno' : 'char',
		# 관리사원번호
		'mgempno' : 'char',
		# 선물연계지점번호
		'futsLnkbrnno' : 'char',
		# 선물연계계좌번호
		'futsLnkacntno' : 'char',
		# 선물시장구분
		'futsmkttp' : 'char',
		# 등록시장코드
		'regmktcode' : 'char',
		# 현금증거금률
		'mnymgnrat' : 'long',
		# 대용증거금률
		'substmgnrat' : 'long',
		# 현금체결금액
		'mnyexecamt' : 'long',
		# 대용체결금액
		'ubstexecamt' : 'long',
		# 수수료체결금액
		'cmsnamtexecamt' : 'long',
		# 신용담보체결금액
		'crdtpldgexecamt' : 'long',
		# 신용체결금액
		'crdtexecamt' : 'long',
		# 전일재사용체결금액
		'prdayruseexecval' : 'long',
		# 금일재사용체결금액
		'crdayruseexecval' : 'long',
		# 실물체결수량
		'spotexecqty' : 'long',
		# 공매도체결수량
		'stslexecqty' : 'long',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'long',
		# 포트폴리오번호
		'ptflno' : 'long',
		# 바스켓번호
		'bskno' : 'long',
		# 트렌치번호
		'trchno' : 'long',
		# 아이템번호
		'itemno' : 'long',
		# 주문자Id
		'orduserId' : 'char',
		# 차입관리여부
		'brwmgmtYn' : 'long',
		# 외국인고유번호
		'frgrunqno' : 'char',
		# 거래세징수구분
		'trtzxLevytp' : 'char',
		# 유동성공급자구분
		'lptp' : 'char',
		# 체결시각
		'exectime' : 'char',
		# 거래소수신체결시각
		'rcptexectime' : 'char',
		# 잔여대출금액
		'rmndLoanamt' : 'long',
		# 잔고수량
		'secbalqty' : 'long',
		# 실물가능수량
		'spotordableqty' : 'long',
		# 재사용가능수량(매도)
		'ordableruseqty' : 'long',
		# 변동수량
		'flctqty' : 'long',
		# 잔고수량(d2)
		'secbalqtyd2' : 'long',
		# 매도주문가능수량
		'sellableqty' : 'long',
		# 미체결매도주문수량
		'unercsellordqty' : 'long',
		# 평균매입가
		'avrpchsprc' : 'long',
		# 매입금액
		'pchsant' : 'long',
		# 예수금
		'deposit' : 'long',
		# 대용금
		'substamt' : 'long',
		# 위탁증거금현금
		'csgnmnymgn' : 'long',
		# 위탁증거금대용
		'csgnsubstmgn' : 'long',
		# 신용담보재사용금
		'crdtpldgruseamt' : 'long',
		# 주문가능현금
		'ordablemny' : 'long',
		# 주문가능대용
		'ordablesubstamt' : 'long',
		# 재사용가능금액
		'ruseableamt' : 'long'
	}
}

# 주식주문정정
db_outblock_subscription_SC2 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# 주문체결유형코드
		'ordxctptncode' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문유형코드
		'ordptncode' : 'char',
		# 관리지점번호
		'mgmtbrnno' : 'char',
		# 계좌번호
		'accno1' : 'char',
		# 계좌번호
		'accno2' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 종목번호
		'Isuno' : 'char',
		# 종목명
		'Isunm' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno' : 'long',
		# 체결번호
		'execno' : 'long',
		# 주문수량
		'ordqty' : 'long',
		# 주문가격
		'ordprc' : 'long',
		# 체결수량
		'execqty' : 'long',
		# 체결가격
		'execprc' : 'long',
		# 정정확인수량
		'mdfycnfqty' : 'long',
		# 정정확인가격
		'mdfycnfprc' : 'long',
		# 취소확인수량
		'canccnfqty' : 'long',
		# 거부수량
		'rjtqty' : 'long',
		# 주문처리유형코드
		'ordtrxptncode' : 'long',
		# 복수주문일련번호
		'mtiordseqno' : 'long',
		# 주문조건
		'ordcndi' : 'char',
		# 호가유형코드
		'ordprcptncode' : 'char',
		# 비저축체결수량
		'nsavtrdqty' : 'long',
		# 단축종목번호
		'shtnIsuno' : 'char',
		# 운용지시번호
		'opdrtnno' : 'char',
		# 반대매매주문구분
		'cvrgordtp' : 'char',
		# 미체결수량(주문)
		'unercqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정수량
		'orgordmdfyqty' : 'long',
		# 원주문취소수량
		'orgordcancqty' : 'long',
		# 주문평균체결가격
		'ordavrexecprc' : 'long',
		# 주문금액
		'ordamt' : 'long',
		# 표준종목번호
		'stdIsuno' : 'char',
		# 전표준종목번호
		'bfstdIsuno' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 주문거래유형코드
		'ordtrdptncode' : 'char',
		# 신용거래코드
		'mgntrncode' : 'char',
		# 수수료합산코드
		'adduptp' : 'char',
		# 통신매체코드
		'commdacode' : 'char',
		# 대출일
		'Loandt' : 'char',
		# 회원/비회원사번호
		'mbrnmbrno' : 'long',
		# 주문계좌번호
		'ordacntno' : 'char',
		# 집계지점번호
		'agrgbrnno' : 'char',
		# 관리사원번호
		'mgempno' : 'char',
		# 선물연계지점번호
		'futsLnkbrnno' : 'char',
		# 선물연계계좌번호
		'futsLnkacntno' : 'char',
		# 선물시장구분
		'futsmkttp' : 'char',
		# 등록시장코드
		'regmktcode' : 'char',
		# 현금증거금률
		'mnymgnrat' : 'long',
		# 대용증거금률
		'substmgnrat' : 'long',
		# 현금체결금액
		'mnyexecamt' : 'long',
		# 대용체결금액
		'ubstexecamt' : 'long',
		# 수수료체결금액
		'cmsnamtexecamt' : 'long',
		# 신용담보체결금액
		'crdtpldgexecamt' : 'long',
		# 신용체결금액
		'crdtexecamt' : 'long',
		# 전일재사용체결금액
		'prdayruseexecval' : 'long',
		# 금일재사용체결금액
		'crdayruseexecval' : 'long',
		# 실물체결수량
		'spotexecqty' : 'long',
		# 공매도체결수량
		'stslexecqty' : 'long',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'long',
		# 포트폴리오번호
		'ptflno' : 'long',
		# 바스켓번호
		'bskno' : 'long',
		# 트렌치번호
		'trchno' : 'long',
		# 아이템번호
		'itemno' : 'long',
		# 주문자Id
		'orduserId' : 'char',
		# 차입관리여부
		'brwmgmtYn' : 'long',
		# 외국인고유번호
		'frgrunqno' : 'char',
		# 거래세징수구분
		'trtzxLevytp' : 'char',
		# 유동성공급자구분
		'lptp' : 'char',
		# 체결시각
		'exectime' : 'char',
		# 거래소수신체결시각
		'rcptexectime' : 'char',
		# 잔여대출금액
		'rmndLoanamt' : 'long',
		# 잔고수량
		'secbalqty' : 'long',
		# 실물가능수량
		'spotordableqty' : 'long',
		# 재사용가능수량(매도)
		'ordableruseqty' : 'long',
		# 변동수량
		'flctqty' : 'long',
		# 잔고수량(d2)
		'secbalqtyd2' : 'long',
		# 매도주문가능수량
		'sellableqty' : 'long',
		# 미체결매도주문수량
		'unercsellordqty' : 'long',
		# 평균매입가
		'avrpchsprc' : 'long',
		# 매입금액
		'pchsant' : 'long',
		# 예수금
		'deposit' : 'long',
		# 대용금
		'substamt' : 'long',
		# 위탁증거금현금
		'csgnmnymgn' : 'long',
		# 위탁증거금대용
		'csgnsubstmgn' : 'long',
		# 신용담보재사용금
		'crdtpldgruseamt' : 'long',
		# 주문가능현금
		'ordablemny' : 'long',
		# 주문가능대용
		'ordablesubstamt' : 'long',
		# 재사용가능금액
		'ruseableamt' : 'long'
	}
}

# 주식주문취소
db_outblock_subscription_SC3 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# 주문체결유형코드
		'ordxctptncode' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문유형코드
		'ordptncode' : 'char',
		# 관리지점번호
		'mgmtbrnno' : 'char',
		# 계좌번호
		'accno1' : 'char',
		# 계좌번호
		'accno2' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 종목번호
		'Isuno' : 'char',
		# 종목명
		'Isunm' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno' : 'long',
		# 체결번호
		'execno' : 'long',
		# 주문수량
		'ordqty' : 'long',
		# 주문가격
		'ordprc' : 'long',
		# 체결수량
		'execqty' : 'long',
		# 체결가격
		'execprc' : 'long',
		# 정정확인수량
		'mdfycnfqty' : 'long',
		# 정정확인가격
		'mdfycnfprc' : 'long',
		# 취소확인수량
		'canccnfqty' : 'long',
		# 거부수량
		'rjtqty' : 'long',
		# 주문처리유형코드
		'ordtrxptncode' : 'long',
		# 복수주문일련번호
		'mtiordseqno' : 'long',
		# 주문조건
		'ordcndi' : 'char',
		# 호가유형코드
		'ordprcptncode' : 'char',
		# 비저축체결수량
		'nsavtrdqty' : 'long',
		# 단축종목번호
		'shtnIsuno' : 'char',
		# 운용지시번호
		'opdrtnno' : 'char',
		# 반대매매주문구분
		'cvrgordtp' : 'char',
		# 미체결수량(주문)
		'unercqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정수량
		'orgordmdfyqty' : 'long',
		# 원주문취소수량
		'orgordcancqty' : 'long',
		# 주문평균체결가격
		'ordavrexecprc' : 'long',
		# 주문금액
		'ordamt' : 'long',
		# 표준종목번호
		'stdIsuno' : 'char',
		# 전표준종목번호
		'bfstdIsuno' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 주문거래유형코드
		'ordtrdptncode' : 'char',
		# 신용거래코드
		'mgntrncode' : 'char',
		# 수수료합산코드
		'adduptp' : 'char',
		# 통신매체코드
		'commdacode' : 'char',
		# 대출일
		'Loandt' : 'char',
		# 회원/비회원사번호
		'mbrnmbrno' : 'long',
		# 주문계좌번호
		'ordacntno' : 'char',
		# 집계지점번호
		'agrgbrnno' : 'char',
		# 관리사원번호
		'mgempno' : 'char',
		# 선물연계지점번호
		'futsLnkbrnno' : 'char',
		# 선물연계계좌번호
		'futsLnkacntno' : 'char',
		# 선물시장구분
		'futsmkttp' : 'char',
		# 등록시장코드
		'regmktcode' : 'char',
		# 현금증거금률
		'mnymgnrat' : 'long',
		# 대용증거금률
		'substmgnrat' : 'long',
		# 현금체결금액
		'mnyexecamt' : 'long',
		# 대용체결금액
		'ubstexecamt' : 'long',
		# 수수료체결금액
		'cmsnamtexecamt' : 'long',
		# 신용담보체결금액
		'crdtpldgexecamt' : 'long',
		# 신용체결금액
		'crdtexecamt' : 'long',
		# 전일재사용체결금액
		'prdayruseexecval' : 'long',
		# 금일재사용체결금액
		'crdayruseexecval' : 'long',
		# 실물체결수량
		'spotexecqty' : 'long',
		# 공매도체결수량
		'stslexecqty' : 'long',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'long',
		# 포트폴리오번호
		'ptflno' : 'long',
		# 바스켓번호
		'bskno' : 'long',
		# 트렌치번호
		'trchno' : 'long',
		# 아이템번호
		'itemno' : 'long',
		# 주문자Id
		'orduserId' : 'char',
		# 차입관리여부
		'brwmgmtYn' : 'long',
		# 외국인고유번호
		'frgrunqno' : 'char',
		# 거래세징수구분
		'trtzxLevytp' : 'char',
		# 유동성공급자구분
		'lptp' : 'char',
		# 체결시각
		'exectime' : 'char',
		# 거래소수신체결시각
		'rcptexectime' : 'char',
		# 잔여대출금액
		'rmndLoanamt' : 'long',
		# 잔고수량
		'secbalqty' : 'long',
		# 실물가능수량
		'spotordableqty' : 'long',
		# 재사용가능수량(매도)
		'ordableruseqty' : 'long',
		# 변동수량
		'flctqty' : 'long',
		# 잔고수량(d2)
		'secbalqtyd2' : 'long',
		# 매도주문가능수량
		'sellableqty' : 'long',
		# 미체결매도주문수량
		'unercsellordqty' : 'long',
		# 평균매입가
		'avrpchsprc' : 'long',
		# 매입금액
		'pchsant' : 'long',
		# 예수금
		'deposit' : 'long',
		# 대용금
		'substamt' : 'long',
		# 위탁증거금현금
		'csgnmnymgn' : 'long',
		# 위탁증거금대용
		'csgnsubstmgn' : 'long',
		# 신용담보재사용금
		'crdtpldgruseamt' : 'long',
		# 주문가능현금
		'ordablemny' : 'long',
		# 주문가능대용
		'ordablesubstamt' : 'long',
		# 재사용가능금액
		'ruseableamt' : 'long'
	}
}

# 주식주문거부
db_outblock_subscription_SC4 = {
	'OutBlock' : {
		# 라인일련번호
		'lineseq' : 'long',
		# 계좌번호
		'accno' : 'char',
		# 조작자ID
		'user' : 'char',
		# 헤더길이
		'len' : 'long',
		# 헤더구분
		'gubun' : 'char',
		# 압축구분
		'compress' : 'char',
		# 암호구분
		'encrypt' : 'char',
		# 공통시작지점
		'offset' : 'long',
		# TRCODE
		'trcode' : 'char',
		# 이용사번호
		'comid' : 'char',
		# 사용자ID
		'userid' : 'char',
		# 접속매체
		'media' : 'char',
		# I/F일련번호
		'ifid' : 'char',
		# 전문일련번호
		'seq' : 'char',
		# TR추적ID
		'trid' : 'char',
		# 공인IP
		'pubip' : 'char',
		# 사설IP
		'prvip' : 'char',
		# 처리지점번호
		'pcbpno' : 'char',
		# 지점번호
		'bpno' : 'char',
		# 단말번호
		'termno' : 'char',
		# 언어구분
		'lang' : 'char',
		# AP처리시간
		'proctm' : 'long',
		# 메세지코드
		'msgcode' : 'char',
		# 메세지출력구분
		'outgu' : 'char',
		# 압축요청구분
		'compreq' : 'char',
		# 기능키
		'funckey' : 'char',
		# 요청레코드개수
		'reqcnt' : 'long',
		# 예비영역
		'filler' : 'char',
		# 연속구분
		'cont' : 'char',
		# 연속키값
		'contkey' : 'char',
		# 가변시스템길이
		'varlen' : 'long',
		# 가변해더길이
		'varhdlen' : 'long',
		# 가변메시지길이
		'varmsglen' : 'long',
		# 조회발원지
		'trsrc' : 'char',
		# I/F이벤트ID
		'eventid' : 'char',
		# I/F정보
		'ifinfo' : 'char',
		# 예비영역
		'filler1' : 'char',
		# 주문체결유형코드
		'ordxctptncode' : 'char',
		# 주문시장코드
		'ordmktcode' : 'char',
		# 주문유형코드
		'ordptncode' : 'char',
		# 관리지점번호
		'mgmtbrnno' : 'char',
		# 계좌번호
		'accno1' : 'char',
		# 계좌번호
		'accno2' : 'char',
		# 계좌명
		'acntnm' : 'char',
		# 종목번호
		'Isuno' : 'char',
		# 종목명
		'Isunm' : 'char',
		# 주문번호
		'ordno' : 'long',
		# 원주문번호
		'orgordno' : 'long',
		# 체결번호
		'execno' : 'long',
		# 주문수량
		'ordqty' : 'long',
		# 주문가격
		'ordprc' : 'long',
		# 체결수량
		'execqty' : 'long',
		# 체결가격
		'execprc' : 'long',
		# 정정확인수량
		'mdfycnfqty' : 'long',
		# 정정확인가격
		'mdfycnfprc' : 'long',
		# 취소확인수량
		'canccnfqty' : 'long',
		# 거부수량
		'rjtqty' : 'long',
		# 주문처리유형코드
		'ordtrxptncode' : 'long',
		# 복수주문일련번호
		'mtiordseqno' : 'long',
		# 주문조건
		'ordcndi' : 'char',
		# 호가유형코드
		'ordprcptncode' : 'char',
		# 비저축체결수량
		'nsavtrdqty' : 'long',
		# 단축종목번호
		'shtnIsuno' : 'char',
		# 운용지시번호
		'opdrtnno' : 'char',
		# 반대매매주문구분
		'cvrgordtp' : 'char',
		# 미체결수량(주문)
		'unercqty' : 'long',
		# 원주문미체결수량
		'orgordunercqty' : 'long',
		# 원주문정정수량
		'orgordmdfyqty' : 'long',
		# 원주문취소수량
		'orgordcancqty' : 'long',
		# 주문평균체결가격
		'ordavrexecprc' : 'long',
		# 주문금액
		'ordamt' : 'long',
		# 표준종목번호
		'stdIsuno' : 'char',
		# 전표준종목번호
		'bfstdIsuno' : 'char',
		# 매매구분
		'bnstp' : 'char',
		# 주문거래유형코드
		'ordtrdptncode' : 'char',
		# 신용거래코드
		'mgntrncode' : 'char',
		# 수수료합산코드
		'adduptp' : 'char',
		# 통신매체코드
		'commdacode' : 'char',
		# 대출일
		'Loandt' : 'char',
		# 회원/비회원사번호
		'mbrnmbrno' : 'long',
		# 주문계좌번호
		'ordacntno' : 'char',
		# 집계지점번호
		'agrgbrnno' : 'char',
		# 관리사원번호
		'mgempno' : 'char',
		# 선물연계지점번호
		'futsLnkbrnno' : 'char',
		# 선물연계계좌번호
		'futsLnkacntno' : 'char',
		# 선물시장구분
		'futsmkttp' : 'char',
		# 등록시장코드
		'regmktcode' : 'char',
		# 현금증거금률
		'mnymgnrat' : 'long',
		# 대용증거금률
		'substmgnrat' : 'long',
		# 현금체결금액
		'mnyexecamt' : 'long',
		# 대용체결금액
		'ubstexecamt' : 'long',
		# 수수료체결금액
		'cmsnamtexecamt' : 'long',
		# 신용담보체결금액
		'crdtpldgexecamt' : 'long',
		# 신용체결금액
		'crdtexecamt' : 'long',
		# 전일재사용체결금액
		'prdayruseexecval' : 'long',
		# 금일재사용체결금액
		'crdayruseexecval' : 'long',
		# 실물체결수량
		'spotexecqty' : 'long',
		# 공매도체결수량
		'stslexecqty' : 'long',
		# 전략코드
		'strtgcode' : 'char',
		# 그룹Id
		'grpId' : 'char',
		# 주문회차
		'ordseqno' : 'long',
		# 포트폴리오번호
		'ptflno' : 'long',
		# 바스켓번호
		'bskno' : 'long',
		# 트렌치번호
		'trchno' : 'long',
		# 아이템번호
		'itemno' : 'long',
		# 주문자Id
		'orduserId' : 'char',
		# 차입관리여부
		'brwmgmtYn' : 'long',
		# 외국인고유번호
		'frgrunqno' : 'char',
		# 거래세징수구분
		'trtzxLevytp' : 'char',
		# 유동성공급자구분
		'lptp' : 'char',
		# 체결시각
		'exectime' : 'char',
		# 거래소수신체결시각
		'rcptexectime' : 'char',
		# 잔여대출금액
		'rmndLoanamt' : 'long',
		# 잔고수량
		'secbalqty' : 'long',
		# 실물가능수량
		'spotordableqty' : 'long',
		# 재사용가능수량(매도)
		'ordableruseqty' : 'long',
		# 변동수량
		'flctqty' : 'long',
		# 잔고수량(d2)
		'secbalqtyd2' : 'long',
		# 매도주문가능수량
		'sellableqty' : 'long',
		# 미체결매도주문수량
		'unercsellordqty' : 'long',
		# 평균매입가
		'avrpchsprc' : 'long',
		# 매입금액
		'pchsant' : 'long',
		# 예수금
		'deposit' : 'long',
		# 대용금
		'substamt' : 'long',
		# 위탁증거금현금
		'csgnmnymgn' : 'long',
		# 위탁증거금대용
		'csgnsubstmgn' : 'long',
		# 신용담보재사용금
		'crdtpldgruseamt' : 'long',
		# 주문가능현금
		'ordablemny' : 'long',
		# 주문가능대용
		'ordablesubstamt' : 'long',
		# 재사용가능금액
		'ruseableamt' : 'long'
	}
}

# 상/하한가근접진입(SHC)
db_outblock_subscription_SHC = {
	'OutBlock' : {
		# 거래소/코스닥구분
		'sijanggubun' : 'char',
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 누적거래량
		'volume' : 'long',
		# 거래증가율
		'volincrate' : 'float',
		# 상/하한가
		'updnlmtprice' : 'long',
		# 상/하한가대비율
		'updnlmtdrate' : 'float',
		# 전일거래량
		'jnilvolume' : 'long',
		# 단축코드
		'shcode' : 'char',
		# 관리구분
		'gwangubun' : 'char',
		# 이상급등구분
		'undergubun' : 'char',
		# 투자유의구분
		'tgubun' : 'char',
		# 우선주구분
		'wgubun' : 'char',
		# 불성실구분
		'dishonest' : 'char',
		# 증거금률
		'jkrate' : 'char',
		# 상한가/하한가연속일수
		'updnlmtdaycnt' : 'long'
	}
}

# 상/하한가근접이탈(SHD)
db_outblock_subscription_SHD = {
	'OutBlock' : {
		# 거래소/코스닥구분
		'sijanggubun' : 'char',
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 누적거래량
		'volume' : 'long',
		# 거래증가율
		'volincrate' : 'float',
		# 상/하한가
		'updnlmtprice' : 'long',
		# 상/하한가대비율
		'updnlmtdrate' : 'float',
		# 전일거래량
		'jnilvolume' : 'long',
		# 단축코드
		'shcode' : 'char',
		# 관리구분
		'gwangubun' : 'char',
		# 이상급등구분
		'undergubun' : 'char',
		# 투자유의구분
		'tgubun' : 'char',
		# 우선주구분
		'wgubun' : 'char',
		# 불성실구분
		'dishonest' : 'char',
		# 증거금률
		'jkrate' : 'char'
	}
}

# 상/하한가진입(SHI)
db_outblock_subscription_SHI = {
	'OutBlock' : {
		# 거래소/코스닥구분
		'sijanggubun' : 'char',
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 누적거래량
		'volume' : 'long',
		# 거래증가율
		'volincrate' : 'float',
		# 매도호가총수량
		'totofferrem' : 'long',
		# 매수호가총수량
		'totbidrem' : 'long',
		# 상한가/하한가최종진입시간
		'updnlmtstime' : 'char',
		# 상한가/하한가연속일수
		'updnlmtdaycnt' : 'long',
		# 전일거래량
		'jnilvolume' : 'long',
		# 단축코드
		'shcode' : 'char',
		# 관리구분
		'gwangubun' : 'char',
		# 이상급등구분
		'undergubun' : 'char',
		# 투자유의구분
		'tgubun' : 'char',
		# 우선주구분
		'wgubun' : 'char',
		# 불성실구분
		'dishonest' : 'char',
		# 증거금률
		'jkrate' : 'char'
	}
}

# 상/하한가이탈(SHO)
db_outblock_subscription_SHO = {
	'OutBlock' : {
		# 거래소/코스닥구분
		'sijanggubun' : 'char',
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'drate' : 'float',
		# 누적거래량
		'volume' : 'long',
		# 거래증가율
		'volincrate' : 'float',
		# 상/하한가
		'updnlmtprice' : 'long',
		# 상/하한가대비
		'updnlmtchange' : 'long',
		# 상/하한가대비율
		'updnlmtdrate' : 'float',
		# 전일거래량
		'jnilvolume' : 'long',
		# 단축코드
		'shcode' : 'char',
		# 관리구분
		'gwangubun' : 'char',
		# 이상급등구분
		'undergubun' : 'char',
		# 투자유의구분
		'tgubun' : 'char',
		# 우선주구분
		'wgubun' : 'char',
		# 불성실구분
		'dishonest' : 'char',
		# 증거금률
		'jkrate' : 'char'
	}
}

# 주식당일매매일지/수수료(t0150)
db_outblock_query_t0150 = {
	't0150OutBlock' : {
		# 매도수량
		'mdqty' : 'long',
		# 매도약정금액
		'mdamt' : 'long',
		# 매도수수료
		'mdfee' : 'long',
		# 매도거래세
		'mdtax' : 'long',
		# 매도농특세
		'mdargtax' : 'long',
		# 매도제비용합
		'tmdtax' : 'long',
		# 매도정산금액
		'mdadjamt' : 'long',
		# 매수수량
		'msqty' : 'long',
		# 매수약정금액
		'msamt' : 'long',
		# 매수수수료
		'msfee' : 'long',
		# 매수제비용합
		'tmstax' : 'long',
		# 매수정산금액
		'msadjamt' : 'long',
		# 합계수량
		'tqty' : 'long',
		# 합계약정금액
		'tamt' : 'long',
		# 합계수수료
		'tfee' : 'long',
		# 합계거래세
		'tottax' : 'long',
		# 합계농특세
		'targtax' : 'long',
		# 합계제비용합
		'ttax' : 'long',
		# 합계정산금액
		'tadjamt' : 'long',
		# CTS_매매구분
		'cts_medosu' : 'char',
		# CTS_종목번호
		'cts_expcode' : 'char',
		# CTS_단가
		'cts_price' : 'char',
		# CTS_매체
		'cts_middiv' : 'char'
	},
	't0150OutBlock1' : [
		{
			# 매매구분
			'medosu' : 'char',
			# 종목번호
			'expcode' : 'char',
			# 수량
			'qty' : 'long',
			# 단가
			'price' : 'long',
			# 약정금액
			'amt' : 'long',
			# 수수료
			'fee' : 'long',
			# 거래세
			'tax' : 'long',
			# 농특세
			'argtax' : 'long',
			# 정산금액
			'adjamt' : 'long',
			# 매체
			'middiv' : 'char'
		}
	]
}

# 주식당일매매일지/수수료(전일)(t0151)
db_outblock_query_t0151 = {
	't0151OutBlock' : {
		# 매도수량
		'mdqty' : 'long',
		# 매도약정금액
		'mdamt' : 'long',
		# 매도수수료
		'mdfee' : 'long',
		# 매도거래세
		'mdtax' : 'long',
		# 매도농특세
		'mdargtax' : 'long',
		# 매도제비용합
		'tmdtax' : 'long',
		# 매도정산금액
		'mdadjamt' : 'long',
		# 매수수량
		'msqty' : 'long',
		# 매수약정금액
		'msamt' : 'long',
		# 매수수수료
		'msfee' : 'long',
		# 매수제비용합
		'tmstax' : 'long',
		# 매수정산금액
		'msadjamt' : 'long',
		# 합계수량
		'tqty' : 'long',
		# 합계약정금액
		'tamt' : 'long',
		# 합계수수료
		'tfee' : 'long',
		# 합계거래세
		'tottax' : 'long',
		# 합계농특세
		'targtax' : 'long',
		# 합계제비용합
		'ttax' : 'long',
		# 합계정산금액
		'tadjamt' : 'long',
		# CTS_매매구분
		'cts_medosu' : 'char',
		# CTS_종목번호
		'cts_expcode' : 'char',
		# CTS_단가
		'cts_price' : 'char',
		# CTS_매체
		'cts_middiv' : 'char'
	},
	't0151OutBlock1' : [
		{
			# 매매구분
			'medosu' : 'char',
			# 종목번호
			'expcode' : 'char',
			# 수량
			'qty' : 'long',
			# 단가
			'price' : 'long',
			# 약정금액
			'amt' : 'long',
			# 수수료
			'fee' : 'long',
			# 거래세
			'tax' : 'long',
			# 농특세
			'argtax' : 'long',
			# 정산금액
			'adjamt' : 'long',
			# 매체
			'middiv' : 'char'
		}
	]
}

# 서버시간조회(t0167)
db_outblock_query_t0167 = {
	't0167OutBlock' : {
		# 일자(YYYYMMDD)
		'dt' : 'char',
		# 시간(HHMMSSssssss)
		'time' : 'char'
	}
}

# 주식잔고2(t0424)
db_outblock_query_t0424 = {
	't0424OutBlock' : {
		# 추정순자산
		'sunamt' : 'long',
		# 실현손익
		'dtsunik' : 'long',
		# 매입금액
		'mamt' : 'long',
		# 추정D2예수금
		'sunamt1' : 'long',
		# CTS_종목번호
		'cts_expcode' : 'char',
		# 평가금액
		'tappamt' : 'long',
		# 평가손익
		'tdtsunik' : 'long'
	},
	't0424OutBlock1' : [
		{
			# 종목번호
			'expcode' : 'char',
			# 잔고구분
			'jangb' : 'char',
			# 잔고수량
			'janqty' : 'long',
			# 매도가능수량
			'mdposqt' : 'long',
			# 평균단가
			'pamt' : 'long',
			# 매입금액
			'mamt' : 'long',
			# 대출금액
			'sinamt' : 'long',
			# 만기일자
			'lastdt' : 'char',
			# 당일매수금액
			'msat' : 'long',
			# 당일매수단가
			'mpms' : 'long',
			# 당일매도금액
			'mdat' : 'long',
			# 당일매도단가
			'mpmd' : 'long',
			# 전일매수금액
			'jsat' : 'long',
			# 전일매수단가
			'jpms' : 'long',
			# 전일매도금액
			'jdat' : 'long',
			# 전일매도단가
			'jpmd' : 'long',
			# 처리순번
			'sysprocseq' : 'long',
			# 대출일자
			'loandt' : 'char',
			# 종목명
			'hname' : 'char',
			# 시장구분
			'marketgb' : 'char',
			# 종목구분
			'jonggb' : 'char',
			# 보유비중
			'janrt' : 'float',
			# 현재가
			'price' : 'long',
			# 평가금액
			'appamt' : 'long',
			# 평가손익
			'dtsunik' : 'long',
			# 수익율
			'sunikrt' : 'float',
			# 수수료
			'fee' : 'long',
			# 제세금
			'tax' : 'long',
			# 신용이자
			'sininter' : 'long'
		}
	]
}

# 주식체결/미체결(t0425)
db_outblock_query_t0425 = {
	't0425OutBlock' : {
		# 총주문수량
		'tqty' : 'long',
		# 총체결수량
		'tcheqty' : 'long',
		# 총미체결수량
		'tordrem' : 'long',
		# 추정수수료
		'cmss' : 'long',
		# 총주문금액
		'tamt' : 'long',
		# 총매도체결금액
		'tmdamt' : 'long',
		# 총매수체결금액
		'tmsamt' : 'long',
		# 추정제세금
		'tax' : 'long',
		# 주문번호
		'cts_ordno' : 'char'
	},
	't0425OutBlock1' : [
		{
			# 주문번호
			'ordno' : 'long',
			# 종목번호
			'expcode' : 'char',
			# 구분
			'medosu' : 'char',
			# 주문수량
			'qty' : 'long',
			# 주문가격
			'price' : 'long',
			# 체결수량
			'cheqty' : 'long',
			# 체결가격
			'cheprice' : 'long',
			# 미체결잔량
			'ordrem' : 'long',
			# 확인수량
			'cfmqty' : 'long',
			# 상태
			'status' : 'char',
			# 원주문번호
			'orgordno' : 'long',
			# 유형
			'ordgb' : 'char',
			# 주문시간
			'ordtime' : 'char',
			# 주문매체
			'ordermtd' : 'char',
			# 처리순번
			'sysprocseq' : 'long',
			# 호가유형
			'hogagb' : 'char',
			# 현재가
			'price1' : 'long',
			# 주문구분
			'orggb' : 'char',
			# 신용구분
			'singb' : 'char',
			# 대출일자
			'loandt' : 'char'
		}
	]
}

# 선물/옵션체결/미체결(t0434)
db_outblock_query_t0434 = {
	't0434OutBlock' : {
		# CTS_주문번호
		'cts_ordno' : 'char'
	},
	't0434OutBlock1' : [
		{
			# 주문번호
			'ordno' : 'long',
			# 원주문번호
			'orgordno' : 'long',
			# 구분
			'medosu' : 'char',
			# 유형
			'ordgb' : 'char',
			# 주문수량
			'qty' : 'long',
			# 주문가격
			'price' : 'float',
			# 체결수량
			'cheqty' : 'long',
			# 체결가격
			'cheprice' : 'float',
			# 미체결잔량
			'ordrem' : 'long',
			# 상태
			'status' : 'char',
			# 주문시간
			'ordtime' : 'char',
			# 주문매체
			'ordermtd' : 'char',
			# 종목번호
			'expcode' : 'char',
			# 사유코드
			'rtcode' : 'char',
			# 처리순번
			'sysprocseq' : 'long',
			# 호가타입
			'hogatype' : 'char'
		}
	]
}

# 선물/옵션잔고평가(이동평균)(t0441)
db_outblock_query_t0441 = {
	't0441OutBlock' : {
		# 매매손익합계
		'tdtsunik' : 'long',
		# CTS_종목번호
		'cts_expcode' : 'char',
		# CTS_매매구분
		'cts_medocd' : 'char',
		# 평가금액
		'tappamt' : 'long',
		# 평가손익
		'tsunik' : 'long'
	},
	't0441OutBlock1' : [
		{
			# 종목번호
			'expcode' : 'char',
			# 구분
			'medosu' : 'char',
			# 잔고수량
			'jqty' : 'long',
			# 청산가능수량
			'cqty' : 'long',
			# 평균단가
			'pamt' : 'float',
			# 총매입금액
			'mamt' : 'long',
			# 매매구분
			'medocd' : 'char',
			# 매매손익
			'dtsunik' : 'long',
			# 처리순번
			'sysprocseq' : 'long',
			# 현재가
			'price' : 'float',
			# 평가금액
			'appamt' : 'long',
			# 평가손익
			'dtsunik1' : 'long',
			# 수익율
			'sunikrt' : 'float'
		}
	]
}

# 주식현재가호가조회(t1101)
db_outblock_query_t1101 = {
	't1101OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 누적거래량
		'volume' : 'long',
		# 전일종가
		'jnilclose' : 'long',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 직전매도대비수량1
		'preoffercha1' : 'long',
		# 직전매수대비수량1
		'prebidcha1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 직전매도대비수량2
		'preoffercha2' : 'long',
		# 직전매수대비수량2
		'prebidcha2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 직전매도대비수량3
		'preoffercha3' : 'long',
		# 직전매수대비수량3
		'prebidcha3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 직전매도대비수량4
		'preoffercha4' : 'long',
		# 직전매수대비수량4
		'prebidcha4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 직전매도대비수량5
		'preoffercha5' : 'long',
		# 직전매수대비수량5
		'prebidcha5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가수량6
		'offerrem6' : 'long',
		# 매수호가수량6
		'bidrem6' : 'long',
		# 직전매도대비수량6
		'preoffercha6' : 'long',
		# 직전매수대비수량6
		'prebidcha6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가수량7
		'offerrem7' : 'long',
		# 매수호가수량7
		'bidrem7' : 'long',
		# 직전매도대비수량7
		'preoffercha7' : 'long',
		# 직전매수대비수량7
		'prebidcha7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가수량8
		'offerrem8' : 'long',
		# 매수호가수량8
		'bidrem8' : 'long',
		# 직전매도대비수량8
		'preoffercha8' : 'long',
		# 직전매수대비수량8
		'prebidcha8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가수량9
		'offerrem9' : 'long',
		# 매수호가수량9
		'bidrem9' : 'long',
		# 직전매도대비수량9
		'preoffercha9' : 'long',
		# 직전매수대비수량9
		'prebidcha9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가수량10
		'offerrem10' : 'long',
		# 매수호가수량10
		'bidrem10' : 'long',
		# 직전매도대비수량10
		'preoffercha10' : 'long',
		# 직전매수대비수량10
		'prebidcha10' : 'long',
		# 매도호가수량합
		'offer' : 'long',
		# 매수호가수량합
		'bid' : 'long',
		# 직전매도대비수량합
		'preoffercha' : 'long',
		# 직전매수대비수량합
		'prebidcha' : 'long',
		# 수신시간
		'hotime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결수량
		'yevolume' : 'long',
		# 예상체결전일구분
		'yesign' : 'char',
		# 예상체결전일대비
		'yechange' : 'long',
		# 예상체결등락율
		'yediff' : 'float',
		# 시간외매도잔량
		'tmoffer' : 'long',
		# 시간외매수잔량
		'tmbid' : 'long',
		# 동시구분
		'ho_status' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 상한가
		'uplmtprice' : 'long',
		# 하한가
		'dnlmtprice' : 'long',
		# 시가
		'open' : 'long',
		# 고가
		'high' : 'long',
		# 저가
		'low' : 'long'
	}
}

# 주식현재가(시세)조회(t1102)
db_outblock_query_t1102 = {
	't1102OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 누적거래량
		'volume' : 'long',
		# 기준가
		'recprice' : 'long',
		# 가중평균
		'avg' : 'long',
		# 상한가
		'uplmtprice' : 'long',
		# 하한가
		'dnlmtprice' : 'long',
		# 전일거래량
		'jnilvolume' : 'long',
		# 거래량차
		'volumediff' : 'long',
		# 시가
		'open' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 고가
		'high' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 저가
		'low' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 52최고가
		'high52w' : 'long',
		# 52최고가일
		'high52wdate' : 'char',
		# 52최저가
		'low52w' : 'long',
		# 52최저가일
		'low52wdate' : 'char',
		# 소진율
		'exhratio' : 'float',
		# PER
		'per' : 'float',
		# PBRX
		'pbrx' : 'float',
		# 상장주식수(천)
		'listing' : 'long',
		# 증거금율
		'jkrate' : 'long',
		# 수량단위
		'memedan' : 'char',
		# 매도증권사코드1
		'offernocd1' : 'char',
		# 매수증권사코드1
		'bidnocd1' : 'char',
		# 매도증권사명1
		'offerno1' : 'char',
		# 매수증권사명1
		'bidno1' : 'char',
		# 총매도수량1
		'dvol1' : 'long',
		# 총매수수량1
		'svol1' : 'long',
		# 매도증감1
		'dcha1' : 'long',
		# 매수증감1
		'scha1' : 'long',
		# 매도비율1
		'ddiff1' : 'float',
		# 매수비율1
		'sdiff1' : 'float',
		# 매도증권사코드2
		'offernocd2' : 'char',
		# 매수증권사코드2
		'bidnocd2' : 'char',
		# 매도증권사명2
		'offerno2' : 'char',
		# 매수증권사명2
		'bidno2' : 'char',
		# 총매도수량2
		'dvol2' : 'long',
		# 총매수수량2
		'svol2' : 'long',
		# 매도증감2
		'dcha2' : 'long',
		# 매수증감2
		'scha2' : 'long',
		# 매도비율2
		'ddiff2' : 'float',
		# 매수비율2
		'sdiff2' : 'float',
		# 매도증권사코드3
		'offernocd3' : 'char',
		# 매수증권사코드3
		'bidnocd3' : 'char',
		# 매도증권사명3
		'offerno3' : 'char',
		# 매수증권사명3
		'bidno3' : 'char',
		# 총매도수량3
		'dvol3' : 'long',
		# 총매수수량3
		'svol3' : 'long',
		# 매도증감3
		'dcha3' : 'long',
		# 매수증감3
		'scha3' : 'long',
		# 매도비율3
		'ddiff3' : 'float',
		# 매수비율3
		'sdiff3' : 'float',
		# 매도증권사코드4
		'offernocd4' : 'char',
		# 매수증권사코드4
		'bidnocd4' : 'char',
		# 매도증권사명4
		'offerno4' : 'char',
		# 매수증권사명4
		'bidno4' : 'char',
		# 총매도수량4
		'dvol4' : 'long',
		# 총매수수량4
		'svol4' : 'long',
		# 매도증감4
		'dcha4' : 'long',
		# 매수증감4
		'scha4' : 'long',
		# 매도비율4
		'ddiff4' : 'float',
		# 매수비율4
		'sdiff4' : 'float',
		# 매도증권사코드5
		'offernocd5' : 'char',
		# 매수증권사코드5
		'bidnocd5' : 'char',
		# 매도증권사명5
		'offerno5' : 'char',
		# 매수증권사명5
		'bidno5' : 'char',
		# 총매도수량5
		'dvol5' : 'long',
		# 총매수수량5
		'svol5' : 'long',
		# 매도증감5
		'dcha5' : 'long',
		# 매수증감5
		'scha5' : 'long',
		# 매도비율5
		'ddiff5' : 'float',
		# 매수비율5
		'sdiff5' : 'float',
		# 외국계매도합계수량
		'fwdvl' : 'long',
		# 외국계매도직전대비
		'ftradmdcha' : 'long',
		# 외국계매도비율
		'ftradmddiff' : 'float',
		# 외국계매수합계수량
		'fwsvl' : 'long',
		# 외국계매수직전대비
		'ftradmscha' : 'long',
		# 외국계매수비율
		'ftradmsdiff' : 'float',
		# 회전율
		'vol' : 'float',
		# 단축코드
		'shcode' : 'char',
		# 누적거래대금
		'value' : 'long',
		# 전일동시간거래량
		'jvolume' : 'long',
		# 연중최고가
		'highyear' : 'long',
		# 연중최고일자
		'highyeardate' : 'char',
		# 연중최저가
		'lowyear' : 'long',
		# 연중최저일자
		'lowyeardate' : 'char',
		# 목표가
		'target' : 'long',
		# 자본금
		'capital' : 'long',
		# 유동주식수
		'abscnt' : 'long',
		# 액면가
		'parprice' : 'long',
		# 결산월
		'gsmm' : 'char',
		# 대용가
		'subprice' : 'long',
		# 시가총액
		'total' : 'long',
		# 상장일
		'listdate' : 'char',
		# 전분기명
		'name' : 'char',
		# 전분기매출액
		'bfsales' : 'long',
		# 전분기영업이익
		'bfoperatingincome' : 'long',
		# 전분기경상이익
		'bfordinaryincome' : 'long',
		# 전분기순이익
		'bfnetincome' : 'long',
		# 전분기EPS
		'bfeps' : 'float',
		# 전전분기명
		'name2' : 'char',
		# 전전분기매출액
		'bfsales2' : 'long',
		# 전전분기영업이익
		'bfoperatingincome2' : 'long',
		# 전전분기경상이익
		'bfordinaryincome2' : 'long',
		# 전전분기순이익
		'bfnetincome2' : 'long',
		# 전전분기EPS
		'bfeps2' : 'float',
		# 전년대비매출액
		'salert' : 'float',
		# 전년대비영업이익
		'opert' : 'float',
		# 전년대비경상이익
		'ordrt' : 'float',
		# 전년대비순이익
		'netrt' : 'float',
		# 전년대비EPS
		'epsrt' : 'float',
		# 락구분
		'info1' : 'char',
		# 관리/급등구분
		'info2' : 'char',
		# 정지/연장구분
		'info3' : 'char',
		# 투자/불성실구분
		'info4' : 'char',
		# 장구분
		'janginfo' : 'char',
		# T.PER
		't_per' : 'float',
		# 통화ISO코드
		'tonghwa' : 'char',
		# 총매도대금1
		'dval1' : 'long',
		# 총매수대금1
		'sval1' : 'long',
		# 총매도대금2
		'dval2' : 'long',
		# 총매수대금2
		'sval2' : 'long',
		# 총매도대금3
		'dval3' : 'long',
		# 총매수대금3
		'sval3' : 'long',
		# 총매도대금4
		'dval4' : 'long',
		# 총매수대금4
		'sval4' : 'long',
		# 총매도대금5
		'dval5' : 'long',
		# 총매수대금5
		'sval5' : 'long',
		# 총매도평단가1
		'davg1' : 'long',
		# 총매수평단가1
		'savg1' : 'long',
		# 총매도평단가2
		'davg2' : 'long',
		# 총매수평단가2
		'savg2' : 'long',
		# 총매도평단가3
		'davg3' : 'long',
		# 총매수평단가3
		'savg3' : 'long',
		# 총매도평단가4
		'davg4' : 'long',
		# 총매수평단가4
		'savg4' : 'long',
		# 총매도평단가5
		'davg5' : 'long',
		# 총매수평단가5
		'savg5' : 'long',
		# 외국계매도대금
		'ftradmdval' : 'long',
		# 외국계매수대금
		'ftradmsval' : 'long',
		# 외국계매도평단가
		'ftradmdvag' : 'long',
		# 외국계매수평단가
		'ftradmsvag' : 'long',
		# 투자주의환기
		'info5' : 'char',
		# 기업인수목적회사여부
		'spac_gubun' : 'char',
		# 발행가격
		'issueprice' : 'long',
		# 배분적용구분코드(1:배분발생2:배분해제그외:미발생)
		'alloc_gubun' : 'char',
		# 배분적용구분
		'alloc_text' : 'char',
		# 단기과열/VI발동
		'shterm_text' : 'char'
	}
}

# 주식현재가시세메모(t1104)
db_outblock_query_t1104 = {
	't1104OutBlock' : {
		# 출력건수
		'nrec' : 'char'
	},
	't1104OutBlock1' : [
		{
			# 인덱스
			'indx' : 'char',
			# 조건구분
			'gubn' : 'char',
			# 출력값
			'vals' : 'char'
		}
	]
}

# 주식피못/디마크조회(t1105)
db_outblock_query_t1105 = {
	't1105OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 피봇
		'pbot' : 'long',
		# 1차저항
		'offer1' : 'long',
		# 1차지지
		'supp1' : 'long',
		# 2차저항
		'offer2' : 'long',
		# 2차지지
		'supp2' : 'long',
		# 기준가격
		'stdprc' : 'long',
		# D저항
		'offerd' : 'long',
		# D지지
		'suppd' : 'long'
	}
}

# 주식시간대별체결조회(t1301)
db_outblock_query_t1301 = {
	't1301OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't1301OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도체결수량
			'mdvolume' : 'long',
			# 매도체결건수
			'mdchecnt' : 'long',
			# 매수체결수량
			'msvolume' : 'long',
			# 매수체결건수
			'mschecnt' : 'long',
			# 순체결량
			'revolume' : 'long',
			# 순체결건수
			'rechecnt' : 'long'
		}
	]
}

# 주식분별주가조회(t1302)
db_outblock_query_t1302 = {
	't1302OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't1302OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 체결강도
			'chdegree' : 'float',
			# 매도체결수량
			'mdvolume' : 'long',
			# 매수체결수량
			'msvolume' : 'long',
			# 순매수체결량
			'revolume' : 'long',
			# 매도체결건수
			'mdchecnt' : 'long',
			# 매수체결건수
			'mschecnt' : 'long',
			# 순체결건수
			'rechecnt' : 'long',
			# 거래량
			'volume' : 'long',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 체결량
			'cvolume' : 'long',
			# 매도체결건수(시간)
			'mdchecnttm' : 'long',
			# 매수체결건수(시간)
			'mschecnttm' : 'long',
			# 매도잔량
			'totofferrem' : 'long',
			# 매수잔량
			'totbidrem' : 'long',
			# 시간별매도체결량
			'mdvolumetm' : 'long',
			# 시간별매수체결량
			'msvolumetm' : 'long'
		}
	]
}

# 기간별주가(t1305)
db_outblock_query_t1305 = {
	't1305OutBlock' : {
		# CNT
		'cnt' : 'long',
		# 날짜
		'date' : 'char',
		# IDX
		'idx' : 'long'
	},
	't1305OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 체결강도
			'chdegree' : 'float',
			# 소진율
			'sojinrate' : 'float',
			# 회전율
			'changerate' : 'float',
			# 외인순매수
			'fpvolume' : 'long',
			# 기관순매수
			'covolume' : 'long',
			# 종목코드
			'shcode' : 'char',
			# 누적거래대금(단위:백만)
			'value' : 'long',
			# 개인순매수
			'ppvolume' : 'long',
			# 시가대비구분
			'o_sign' : 'char',
			# 시가대비
			'o_change' : 'long',
			# 시가기준등락율
			'o_diff' : 'float',
			# 고가대비구분
			'h_sign' : 'char',
			# 고가대비
			'h_change' : 'long',
			# 고가기준등락율
			'h_diff' : 'float',
			# 저가대비구분
			'l_sign' : 'char',
			# 저가대비
			'l_change' : 'long',
			# 저가기준등락율
			'l_diff' : 'float',
			# 시가총액(단위:백만)
			'marketcap' : 'long'
		}
	]
}

# 주식시간대별체결조회챠트(t1308)
db_outblock_query_t1308 = {
	't1308OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도(거래량)
			'chdegvol' : 'float',
			# 체결강도(건수)
			'chdegcnt' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도체결수량
			'mdvolume' : 'long',
			# 매도체결건수
			'mdchecnt' : 'long',
			# 매수체결수량
			'msvolume' : 'long',
			# 매수체결건수
			'mschecnt' : 'long',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long'
		}
	]
}

# 주식당일전일분틱조회(t1310)
db_outblock_query_t1310 = {
	't1310OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't1310OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도체결수량
			'mdvolume' : 'long',
			# 매도체결건수
			'mdchecnt' : 'long',
			# 매수체결수량
			'msvolume' : 'long',
			# 매수체결건수
			'mschecnt' : 'long',
			# 순체결량
			'revolume' : 'long',
			# 순체결건수
			'rechecnt' : 'long'
		}
	]
}

# 신규상장종목조회(t1403)
db_outblock_query_t1403 = {
	't1403OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1403OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 공모가
			'kmprice' : 'long',
			# 등록일
			'date' : 'char',
			# 등록일기준가
			'recprice' : 'long',
			# 기준가등락율
			'kmdiff' : 'float',
			# 등록일종가
			'close' : 'long',
			# 등록일등락율
			'recdiff' : 'float',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 관리/불성실/투자유의조회(t1404)
db_outblock_query_t1404 = {
	't1404OutBlock' : {
		# 종목코드_CTS
		'cts_shcode' : 'char'
	},
	't1404OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 지정일
			'date' : 'char',
			# 지정일주가
			'tprice' : 'long',
			# 지정일대비
			'tchange' : 'long',
			# 대비율
			'tdiff' : 'float',
			# 사유
			'reason' : 'char',
			# 종목코드
			'shcode' : 'char',
			# 해제일
			'edate' : 'char'
		}
	]
}

# 투자경고/매매정지/정리매매조회(t1405)
db_outblock_query_t1405 = {
	't1405OutBlock' : {
		# 종목코드_CTS
		'cts_shcode' : 'char'
	},
	't1405OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 지정일
			'date' : 'char',
			# 해제일
			'edate' : 'char',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 증거금율별종목조회(t1411)
db_outblock_query_t1411 = {
	't1411OutBlock' : {
		# 위탁증거금율
		'jkrate' : 'long',
		# 신용증거금율
		'sjkrate' : 'long',
		# IDX
		'idx' : 'long'
	},
	't1411OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 위탁증거금율
			'jkrate' : 'long',
			# 신용증거금율
			'sjkrate' : 'long',
			# 대용가
			'subprice' : 'long',
			# 전일종가
			'recprice' : 'long',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long'
		}
	]
}

# 상/하한(t1422)
db_outblock_query_t1422 = {
	't1422OutBlock' : {
		# CNT
		'cnt' : 'long',
		# IDX
		'idx' : 'long'
	},
	't1422OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 매도잔량
			'offerrem1' : 'long',
			# 매수잔량
			'bidrem1' : 'long',
			# 최종진입
			'last' : 'char',
			# 연속
			'lmtdaycnt' : 'long',
			# 전일거래량
			'jnilvolume' : 'long',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 상/하한가직전(t1427)
db_outblock_query_t1427 = {
	't1427OutBlock' : {
		# CNT
		'cnt' : 'long',
		# IDX
		'idx' : 'long'
	},
	't1427OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 상한가/하한가
			'lmtprice' : 'long',
			# 대비율
			'rate' : 'float',
			# 종목코드
			'shcode' : 'char',
			# 전일거래량
			'jnilvolume' : 'long',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 연속
			'lmtdaycnt' : 'long',
			# 거래대금
			'value' : 'long',
			# 시가총액
			'total' : 'long'
		}
	]
}

# 신고/신저가(t1442)
db_outblock_query_t1442 = {
	't1442OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1442OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 이전가
			'pastprice' : 'long',
			# 이전가대비구분
			'pastsign' : 'char',
			# 이전가대비
			'pastchange' : 'long',
			# 이전가대비율
			'pastdiff' : 'float'
		}
	]
}

# 시가총액상위(t1444)
db_outblock_query_t1444 = {
	't1444OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1444OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래비중
			'vol_rate' : 'float',
			# 시가총액
			'total' : 'long',
			# 비중
			'rate' : 'float',
			# 외인비중
			'for_rate' : 'float'
		}
	]
}

# 가격대별매매비중조회(t1449)
db_outblock_query_t1449 = {
	't1449OutBlock' : {
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 매수체결량
		'msvolume' : 'long',
		# 매도체결량
		'mdvolume' : 'long'
	},
	't1449OutBlock1' : [
		{
			# 체결가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'tickdiff' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 비중
			'diff' : 'float',
			# 매도체결량
			'mdvolume' : 'long',
			# 매수체결량
			'msvolume' : 'long',
			# 매수비율
			'msdiff' : 'float'
		}
	]
}

# 거래량상위(t1452)
db_outblock_query_t1452 = {
	't1452OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1452OutBlock1' : [
		{
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 회전율
			'vol' : 'float',
			# 전일거래량
			'jnilvolume' : 'long',
			# 전일비
			'bef_diff' : 'float',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 거래대금상위(t1463)
db_outblock_query_t1463 = {
	't1463OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1463OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 거래대금
			'value' : 'long',
			# 전일거래대금
			'jnilvalue' : 'long',
			# 전일비
			'bef_diff' : 'float',
			# 종목코드
			'shcode' : 'char',
			# filler
			'filler' : 'char',
			# 전일거래량
			'jnilvolume' : 'long'
		}
	]
}

# 시간대별호가잔량추이(t1471)
db_outblock_query_t1471 = {
	't1471OutBlock' : {
		# 시간CTS
		'time' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 누적거래량
		'volume' : 'long'
	},
	't1471OutBlock1' : [
		{
			# 체결시간
			'time' : 'char',
			# 메도증감
			'preoffercha1' : 'long',
			# 매도우선잔량
			'offerrem1' : 'long',
			# 매도우선호가
			'offerho1' : 'long',
			# 매수우선호가
			'bidho1' : 'long',
			# 매수우선잔량
			'bidrem1' : 'long',
			# 매수증감
			'prebidcha1' : 'long',
			# 총매도
			'totofferrem' : 'long',
			# 총매수
			'totbidrem' : 'long',
			# 순매수
			'totsun' : 'long',
			# 매수비율
			'msrate' : 'float',
			# 종가
			'close' : 'long'
		}
	]
}

# 체결강도추이(t1475)
db_outblock_query_t1475 = {
	't1475OutBlock' : {
		# 기준일자
		'date' : 'long',
		# 기준시간
		'time' : 'long',
		# 랭크카운터
		'rankcnt' : 'long'
	},
	't1475OutBlock1' : [
		{
			# 일자
			'datetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 당일VP
			'todayvp' : 'float',
			# 5일MAVP
			'ma5vp' : 'float',
			# 20일MAVP
			'ma20vp' : 'float',
			# 60일MAVP
			'ma60vp' : 'float'
		}
	]
}

# 예상지수(t1485)
db_outblock_query_t1485 = {
	't1485OutBlock' : {
		# 현재지수
		'pricejisu' : 'float',
		# 지수전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 거래량
		'volume' : 'long',
		# 상승종목수
		'yhighjo' : 'long',
		# 상한종목수
		'yupjo' : 'long',
		# 보합종목수
		'yunchgjo' : 'long',
		# 하락종목수
		'ylowjo' : 'long',
		# 하한종목수
		'ydownjo' : 'long',
		# 거래형성수
		'ytrajo' : 'long'
	},
	't1485OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 예상지수
			'jisu' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 예상체결량
			'volume' : 'long',
			# 예상체결량직전대비
			'volcha' : 'long'
		}
	]
}

# 시간별예상체결가(t1486)
db_outblock_query_t1486 = {
	't1486OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't1486OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 예상체결가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 예상체결량
			'cvolume' : 'long',
			# 매도호가
			'offerho1' : 'long',
			# 매수호가
			'bidho1' : 'long',
			# 매도잔량
			'offerrem1' : 'long',
			# 매수잔량
			'bidrem1' : 'long'
		}
	]
}

# 예상체결가등락율상위조회(t1488)
db_outblock_query_t1488 = {
	't1488OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1488OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 매도잔량
			'offerrem' : 'long',
			# 매도호가
			'offerho' : 'long',
			# 매수호가
			'bidho' : 'long',
			# 매수잔량
			'bidrem' : 'long',
			# 연속일수
			'cnt' : 'long',
			# 종목코드
			'shcode' : 'char',
			# 증거금율
			'jkrate' : 'char',
			# 전일거래량
			'jnilvolume' : 'long'
		}
	]
}

# 예상체결량상위조회(t1489)
db_outblock_query_t1489 = {
	't1489OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1489OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 예상거래량
			'volume' : 'long',
			# 매도호가
			'offerho' : 'long',
			# 매수호가
			'bidho' : 'long',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 업종현재가(t1511)
db_outblock_query_t1511 = {
	't1511OutBlock' : {
		# 업종구분
		'gubun' : 'char',
		# 업종명
		'hname' : 'char',
		# 현재지수
		'pricejisu' : 'float',
		# 전일지수
		'jniljisu' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 지수등락율
		'diffjisu' : 'float',
		# 전일거래량
		'jnilvolume' : 'long',
		# 당일거래량
		'volume' : 'long',
		# 거래량전일대비
		'volumechange' : 'long',
		# 거래량비율
		'volumerate' : 'float',
		# 전일거래대금
		'jnilvalue' : 'long',
		# 당일거래대금
		'value' : 'long',
		# 거래대금전일대비
		'valuechange' : 'long',
		# 거래대금비율
		'valuerate' : 'float',
		# 시가지수
		'openjisu' : 'float',
		# 시가등락율
		'opendiff' : 'float',
		# 시가시간
		'opentime' : 'char',
		# 고가지수
		'highjisu' : 'float',
		# 고가등락율
		'highdiff' : 'float',
		# 고가시간
		'hightime' : 'char',
		# 저가지수
		'lowjisu' : 'float',
		# 저가등락율
		'lowdiff' : 'float',
		# 저가시간
		'lowtime' : 'char',
		# 52주최고지수
		'whjisu' : 'float',
		# 52주최고현재가대비
		'whchange' : 'float',
		# 52주최고지수일자
		'whjday' : 'char',
		# 52주최저지수
		'wljisu' : 'float',
		# 52주최저현재가대비
		'wlchange' : 'float',
		# 52주최저지수일자
		'wljday' : 'char',
		# 연중최고지수
		'yhjisu' : 'float',
		# 연중최고현재가대비
		'yhchange' : 'float',
		# 연중최고지수일자
		'yhjday' : 'char',
		# 연중최저지수
		'yljisu' : 'float',
		# 연중최저현재가대비
		'ylchange' : 'float',
		# 연중최저지수일자
		'yljday' : 'char',
		# 첫번째지수코드
		'firstjcode' : 'char',
		# 첫번째지수명
		'firstjname' : 'char',
		# 첫번째지수
		'firstjisu' : 'float',
		# 첫번째대비구분
		'firsign' : 'char',
		# 첫번째전일대비
		'firchange' : 'float',
		# 첫번째등락율
		'firdiff' : 'float',
		# 두번째지수코드
		'secondjcode' : 'char',
		# 두번째지수명
		'secondjname' : 'char',
		# 두번째지수
		'secondjisu' : 'float',
		# 두번째대비구분
		'secsign' : 'char',
		# 두번째전일대비
		'secchange' : 'float',
		# 두번째등락율
		'secdiff' : 'float',
		# 세번째지수코드
		'thirdjcode' : 'char',
		# 세번째지수명
		'thirdjname' : 'char',
		# 세번째지수
		'thirdjisu' : 'float',
		# 세번째대비구분
		'thrsign' : 'char',
		# 세번째전일대비
		'thrchange' : 'float',
		# 세번째등락율
		'thrdiff' : 'float',
		# 네번째지수코드
		'fourthjcode' : 'char',
		# 네번째지수명
		'fourthjname' : 'char',
		# 네번째지수
		'fourthjisu' : 'float',
		# 네번째대비구분
		'forsign' : 'char',
		# 네번째전일대비
		'forchange' : 'float',
		# 네번째등락율
		'fordiff' : 'float',
		# 상승종목수
		'highjo' : 'long',
		# 상한종목수
		'upjo' : 'long',
		# 보합종목수
		'unchgjo' : 'long',
		# 하락종목수
		'lowjo' : 'long',
		# 하한종목수
		'downjo' : 'long'
	}
}

# 업종기간별추이(t1514)
db_outblock_query_t1514 = {
	't1514OutBlock' : {
		# CTS_일자
		'cts_date' : 'char'
	},
	't1514OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 지수
			'jisu' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 거래대금1
			'value1' : 'long',
			# 상승
			'high' : 'long',
			# 보합
			'unchg' : 'long',
			# 하락
			'low' : 'long',
			# 상승종목비율
			'uprate' : 'float',
			# 외인순매수
			'frgsvolume' : 'long',
			# 시가
			'openjisu' : 'float',
			# 고가
			'highjisu' : 'float',
			# 저가
			'lowjisu' : 'float',
			# 거래대금2
			'value2' : 'long',
			# 상한
			'up' : 'long',
			# 하한
			'down' : 'long',
			# 종목수
			'totjo' : 'long',
			# 기관순매수
			'orgsvolume' : 'long',
			# 업종코드
			'upcode' : 'char',
			# 거래비중
			'rate' : 'float',
			# 업종배당수익률
			'divrate' : 'float'
		}
	]
}

# 업종별종목시세(t1516)
db_outblock_query_t1516 = {
	't1516OutBlock' : {
		# 종목코드
		'shcode' : 'char',
		# 지수
		'pricejisu' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'jdiff' : 'float'
	},
	't1516OutBlock1' : [
		{
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 소진율
			'sojinrate' : 'float',
			# 베타계수
			'beta' : 'float',
			# PER
			'perx' : 'float',
			# 외인순매수
			'frgsvolume' : 'long',
			# 기관순매수
			'orgsvolume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 종목코드
			'shcode' : 'char',
			# 시가총액
			'total' : 'long',
			# 거래대금
			'value' : 'long'
		}
	]
}

# 테마별종목(t1531)
db_outblock_query_t1531 = {
	't1531OutBlock' : [
		{
			# 테마명
			'tmname' : 'char',
			# 평균등락율
			'avgdiff' : 'float',
			# 테마코드
			'tmcode' : 'char'
		}
	]
}

# 종목별테마(t1532)
db_outblock_query_t1532 = {
	't1532OutBlock' : [
		{
			# 테마명
			'tmname' : 'char',
			# 평균등락율
			'avgdiff' : 'float',
			# 테마코드
			'tmcode' : 'char'
		}
	]
}

# 특이테마(t1533)
db_outblock_query_t1533 = {
	't1533OutBlock' : [
		{
			# 테마명
			'tmname' : 'char',
			# 전체
			'totcnt' : 'long',
			# 상승
			'upcnt' : 'long',
			# 하락
			'dncnt' : 'long',
			# 상승비율
			'uprate' : 'float',
			# 거래증가율
			'diff_vol' : 'float',
			# 평균등락율
			'avgdiff' : 'float',
			# 대비등락율
			'chgdiff' : 'float',
			# 테마코드
			'tmcode' : 'char'
		}
	]
}

# 테마종목별시세조회(t1537)
db_outblock_query_t1537 = {
	't1537OutBlock' : {
		# 상승종목수
		'upcnt' : 'long',
		# 테마종목수
		'tmcnt' : 'long',
		# 상승종목비율
		'uprate' : 'long',
		# 테마명
		'tmname' : 'char'
	},
	't1537OutBlock1' : [
		{
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 전일동시간
			'jniltime' : 'float',
			# 종목코드
			'shcode' : 'char',
			# 예상체결가
			'yeprice' : 'long',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 누적거래대금(단위:백만)
			'value' : 'long',
			# 시가총액(단위:백만)
			'marketcap' : 'long'
		}
	]
}

# 투자자별종합(t1601)
db_outblock_query_t1601 = {
	't1601OutBlock1' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't1601OutBlock2' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't1601OutBlock3' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't1601OutBlock4' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't1601OutBlock5' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	}
}

# 시간대별투자자매매추이(t1602)
db_outblock_query_t1602 = {
	't1602OutBlock' : {
		# CTSTIME
		'cts_time' : 'char',
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 국가투자자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 사모펀드코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't1602OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# 개인순매수
			'sv_08' : 'long',
			# 외국인순매수
			'sv_17' : 'long',
			# 기관계순매수
			'sv_18' : 'long',
			# 증권순매수
			'sv_01' : 'long',
			# 투신순매수
			'sv_03' : 'long',
			# 은행순매수
			'sv_04' : 'long',
			# 보험순매수
			'sv_02' : 'long',
			# 종금순매수
			'sv_05' : 'long',
			# 기금순매수
			'sv_06' : 'long',
			# 기타순매수
			'sv_07' : 'long',
			# 국가순매수
			'sv_11' : 'long',
			# 사모펀드순매수
			'sv_00' : 'long'
		}
	]
}

# 시간대별투자자매매추이상세(t1603)
db_outblock_query_t1603 = {
	't1603OutBlock' : {
		# CTSIDX
		'cts_idx' : 'long',
		# CTSTIME
		'cts_time' : 'char'
	},
	't1603OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# 투자자구분
			'tjjcode' : 'char',
			# 매수수량
			'msvolume' : 'long',
			# 매도수량
			'mdvolume' : 'long',
			# 매수금액
			'msvalue' : 'long',
			# 매도금액
			'mdvalue' : 'long',
			# 순매수수량
			'svolume' : 'long',
			# 순매수금액
			'svalue' : 'long'
		}
	]
}

# 투자자매매종합1(t1615)
db_outblock_query_t1615 = {
	't1615OutBlock' : {
		# 위탁매도수량
		'dwvolume' : 'long',
		# 위탁매도금액
		'dwvalue' : 'long',
		# 자기매도수량
		'djvolume' : 'long',
		# 자기매도금액
		'djvalue' : 'long',
		# 합계수량
		'sum_volume' : 'long',
		# 합계금액
		'sum_value' : 'long'
	},
	't1615OutBlock1' : [
		{
			# 시장명
			'hname' : 'char',
			# 개인
			'sv_08' : 'long',
			# 외국인
			'sv_17' : 'long',
			# 기관계
			'sv_18' : 'long',
			# 증권
			'sv_07' : 'long'
		}
	]
}

# 투자자매매종합2(t1617)
db_outblock_query_t1617 = {
	't1617OutBlock' : {
		# CTSDATE
		'cts_date' : 'char',
		# CTSTIME
		'cts_time' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인순매수
		'sv_08' : 'long',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인순매수
		'sv_17' : 'long',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계순매수
		'sv_18' : 'long',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권순매수
		'sv_01' : 'long'
	},
	't1617OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 개인
			'sv_08' : 'long',
			# 외국인
			'sv_17' : 'long',
			# 기관계
			'sv_18' : 'long',
			# 증권
			'sv_01' : 'long'
		}
	]
}

# 업종별분별투자자매매동향(챠트용)
db_outblock_query_t1621 = {
	't1621OutBlock' : {
		# 개인투자자코드
		'indcode' : 'char',
		# 외국인투자자코드
		'forcode' : 'char',
		# 기관계투자자코드
		'syscode' : 'char',
		# 증권투자자코드
		'stocode' : 'char',
		# 투신투자자코드
		'invcode' : 'char',
		# 은행투자자코드
		'bancode' : 'char',
		# 보험투자자코드
		'inscode' : 'char',
		# 종금투자자코드
		'fincode' : 'char',
		# 기금투자자코드
		'moncode' : 'char',
		# 기타투자자코드
		'etccode' : 'char',
		# 국가투자자코드
		'natcode' : 'char',
		# 사모펀드투자자코드
		'pefcode' : 'char',
		# 기준지수코드
		'jisucd' : 'char',
		# 기준지수명
		'jisunm' : 'char'
	},
	't1621OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 일자시간
			'datetime' : 'char',
			# 개인순매수거래량
			'indmsvol' : 'long',
			# 개인순매수거래대금
			'indmsamt' : 'double',
			# 외국인순매수거래량
			'formsvol' : 'long',
			# 외국인순매수거래대금
			'formsamt' : 'double',
			# 기관계순매수거래량
			'sysmsvol' : 'long',
			# 기관계순매수거래대금
			'sysmsamt' : 'double',
			# 증권순매수거래량
			'stomsvol' : 'long',
			# 증권순매수거래대금
			'stomsamt' : 'double',
			# 투신순매수거래량
			'invmsvol' : 'long',
			# 투신순매수거래대금
			'invmsamt' : 'double',
			# 은행순매수거래량
			'banmsvol' : 'long',
			# 은행순매수거래대금
			'banmsamt' : 'double',
			# 보험순매수거래량
			'insmsvol' : 'long',
			# 보험순매수거래대금
			'insmsamt' : 'double',
			# 종금순매수거래량
			'finmsvol' : 'long',
			# 종금순매수거래대금
			'finmsamt' : 'double',
			# 기금순매수거래량
			'monmsvol' : 'long',
			# 기금순매수거래대금
			'monmsamt' : 'double',
			# 기타순매수거래량
			'etcmsvol' : 'long',
			# 기타순매수거래대금
			'etcmsamt' : 'double',
			# 국가순매수거래량
			'natmsvol' : 'long',
			# 국가순매수거래대금
			'natmsamt' : 'double',
			# 사모펀드순매수거래량
			'pefmsvol' : 'long',
			# 사모펀드순매수거래대금
			'pefmsamt' : 'double',
			# 기준지수
			'upclose' : 'float',
			# 기준체결거래량
			'upcvolume' : 'long',
			# 기준누적거래량
			'upvolume' : 'double',
			# 기준거래대금
			'upvalue' : 'double'
		}
	]
}

# 프로그램매매종합조회(t1631)
db_outblock_query_t1631 = {
	't1631OutBlock' : {
		# 매도차익미체결잔량
		'cdhrem' : 'long',
		# 매도비차익미체결잔량
		'bdhrem' : 'long',
		# 매도차익주문수량
		'tcdrem' : 'long',
		# 매도비차익주문수량
		'tbdrem' : 'long',
		# 매수차익미체결잔량
		'cshrem' : 'long',
		# 매수비차익미체결잔량
		'bshrem' : 'long',
		# 매수차익주문수량
		'tcsrem' : 'long',
		# 매수비차익주문수량
		'tbsrem' : 'long'
	},
	't1631OutBlock1' : [
		{
			# 매도수량
			'offervolume' : 'long',
			# 매도금액
			'offervalue' : 'long',
			# 매수수량
			'bidvolume' : 'long',
			# 매수금액
			'bidvalue' : 'long',
			# 순매수수량
			'volume' : 'long',
			# 순매수금액
			'value' : 'long'
		}
	]
}

# 시간대별프로그램매매추이(t1632)
db_outblock_query_t1632 = {
	't1632OutBlock' : {
		# 날짜CTS
		'date' : 'char',
		# 시간CTS
		'time' : 'char',
		# IDX
		'idx' : 'long'
	},
	't1632OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# KP200
			'k200jisu' : 'float',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'float',
			# BASIS
			'k200basis' : 'float',
			# 전체순매수
			'tot3' : 'long',
			# 전체매수
			'tot1' : 'long',
			# 전체매도
			'tot2' : 'long',
			# 차익순매수
			'cha3' : 'long',
			# 차익매수
			'cha1' : 'long',
			# 차익매도
			'cha2' : 'long',
			# 비차익순매수
			'bcha3' : 'long',
			# 비차익매수
			'bcha1' : 'long',
			# 비차익매도
			'bcha2' : 'long'
		}
	]
}

# 기간별프로그램매매추이(t1633)
db_outblock_query_t1633 = {
	't1633OutBlock' : {
		# 날짜
		'date' : 'char',
		# IDX
		'idx' : 'long'
	},
	't1633OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# KP200
			'jisu' : 'float',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'float',
			# 전체순매수
			'tot3' : 'long',
			# 전체매수
			'tot1' : 'long',
			# 전체매도
			'tot2' : 'long',
			# 차익순매수
			'cha3' : 'long',
			# 차익매수
			'cha1' : 'long',
			# 차익매도
			'cha2' : 'long',
			# 비차익순매수
			'bcha3' : 'long',
			# 비차익매수
			'bcha1' : 'long',
			# 비차익매도
			'bcha2' : 'long',
			# 거래량
			'volume' : 'long'
		}
	]
}

# 종목별프로그램매매동향(t1636)
db_outblock_query_t1636 = {
	't1636OutBlock' : {
		# IDXCTS
		'cts_idx' : 'long'
	},
	't1636OutBlock1' : [
		{
			# 순위
			'rank' : 'long',
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 순매수금액
			'svalue' : 'long',
			# 매도금액
			'offervalue' : 'long',
			# 매수금액
			'stksvalue' : 'long',
			# 순매수수량
			'svolume' : 'long',
			# 매도수량
			'offervolume' : 'long',
			# 매수수량
			'stksvolume' : 'long',
			# 시가총액
			'sgta' : 'long',
			# 비중
			'rate' : 'float',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 종목별프로그램매매추이(t1637)
db_outblock_query_t1637 = {
	't1637OutBlock' : {
		# IDXCTS
		'cts_idx' : 'long'
	},
	't1637OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 현재가
			'price' : 'long',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 순매수금액
			'svalue' : 'long',
			# 매도금액
			'offervalue' : 'long',
			# 매수금액
			'stksvalue' : 'long',
			# 순매수수량
			'svolume' : 'long',
			# 매도수량
			'offervolume' : 'long',
			# 매수수량
			'stksvolume' : 'long',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 종목별잔량/사전공시(t1638)
db_outblock_query_t1638 = {
	't1638OutBlock' : [
		{
			# 순위
			'rank' : 'long',
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 시총비중
			'sigatotrt' : 'float',
			# 순매수잔량
			'obuyvol' : 'long',
			# 매수잔량
			'buyrem' : 'long',
			# 매수공시수량
			'psgvolume' : 'long',
			# 매도잔량
			'sellrem' : 'long',
			# 매도공시수량
			'pdgvolume' : 'long',
			# 시가총액
			'sigatot' : 'long',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 프로그램매매종합조회(미니)(t1640)
db_outblock_query_t1640 = {
	't1640OutBlock' : {
		# 매도수량
		'offervolume' : 'long',
		# 매수수량
		'bidvolume' : 'long',
		# 순매수수량
		'volume' : 'long',
		# 매도증감
		'offerdiff' : 'long',
		# 매수증감
		'biddiff' : 'long',
		# 순매수증감
		'sundiff' : 'long',
		# 베이시스
		'basis' : 'float',
		# 매도금액
		'offervalue' : 'double',
		# 매수금액
		'bidvalue' : 'double',
		# 순매수금액
		'value' : 'double',
		# 매도금액증감
		'offervaldiff' : 'double',
		# 매수금액증감
		'bidvaldiff' : 'double',
		# 순매수증감
		'sunvaldiff' : 'double'
	}
}

# 시간대별프로그램매매추이(차트)(t1662)
db_outblock_query_t1662 = {
	't1662OutBlock' : [
		{
			# 시간
			'time' : 'char',
			# KP200
			'k200jisu' : 'float',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'float',
			# BASIS
			'k200basis' : 'float',
			# 전체순매수
			'tot3' : 'long',
			# 전체매수
			'tot1' : 'long',
			# 전체매도
			'tot2' : 'long',
			# 차익순매수
			'cha3' : 'long',
			# 차익매수
			'cha1' : 'long',
			# 차익매도
			'cha2' : 'long',
			# 비차익순매수
			'bcha3' : 'long',
			# 비차익매수
			'bcha1' : 'long',
			# 비차익매도
			'bcha2' : 'long',
			# 거래량
			'volume' : 'long'
		}
	]
}

# 투자자매매종합(챠트)
db_outblock_query_t1664 = {
	't1664OutBlock1' : [
		{
			# 일자시간
			'dt' : 'char',
			# 증권순매수
			'tjj01' : 'double',
			# 보험순매수
			'tjj02' : 'double',
			# 투신순매수
			'tjj03' : 'double',
			# 은행순매수
			'tjj04' : 'double',
			# 종금순매수
			'tjj05' : 'double',
			# 기금순매수
			'tjj06' : 'double',
			# 기타순매수
			'tjj07' : 'double',
			# 개인순매수
			'tjj08' : 'double',
			# 외국인순매수
			'tjj17' : 'double',
			# 기관순매수
			'tjj18' : 'double',
			# 차익순매수
			'cha' : 'double',
			# 비차익순매수
			'bicha' : 'double',
			# 종합순매수
			'totcha' : 'double',
			# 베이시스
			'basis' : 'float'
		}
	]
}

# 기간별투자자매매추이(챠트)
db_outblock_query_t1665 = {
	't1665OutBlock' : {
		# 시장코드
		'mcode' : 'char',
		# 시장명
		'mname' : 'char'
	},
	't1665OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 개인수량
			'sv_08' : 'long',
			# 외인계수량(등록+미등록)
			'sv_17' : 'long',
			# 기관계수량
			'sv_18' : 'long',
			# 증권수량
			'sv_01' : 'long',
			# 투신수량
			'sv_03' : 'long',
			# 은행수량
			'sv_04' : 'long',
			# 보험수량
			'sv_02' : 'long',
			# 종금수량
			'sv_05' : 'long',
			# 기금수량
			'sv_06' : 'long',
			# 기타수량
			'sv_07' : 'long',
			# 사모펀드수량
			'sv_00' : 'long',
			# 등록외국인수량
			'sv_09' : 'long',
			# 미등록외국인수량
			'sv_10' : 'long',
			# 국가수량
			'sv_11' : 'long',
			# 기타계수량(기타+국가)
			'sv_99' : 'long',
			# 개인금액
			'sa_08' : 'double',
			# 외인계금액(등록+미등록)
			'sa_17' : 'double',
			# 기관계금액
			'sa_18' : 'double',
			# 증권금액
			'sa_01' : 'double',
			# 투신금액
			'sa_03' : 'double',
			# 은행금액
			'sa_04' : 'double',
			# 보험금액
			'sa_02' : 'double',
			# 종금금액
			'sa_05' : 'double',
			# 기금금액
			'sa_06' : 'double',
			# 기타금액
			'sa_07' : 'double',
			# 사모펀드금액
			'sa_00' : 'double',
			# 등록외국인금액
			'sa_09' : 'double',
			# 미등록외국인금액
			'sa_10' : 'double',
			# 국가금액
			'sa_11' : 'double',
			# 기타계금액(기타+국가)
			'sa_99' : 'double',
			# 시장지수
			'jisu' : 'float'
		}
	]
}

# 외인기관종목별동향(t1701)
db_outblock_query_t1701 = {
	't1701OutBlock' : [
		{
			# 일자
			'date' : 'char',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 개인
			'psnvolume' : 'long',
			# 기관
			'orgvolume' : 'long',
			# 외국인
			'frgvolume' : 'long',
			# 외국계
			'frgvolumesum' : 'long',
			# 프로그램
			'pgmvolume' : 'long',
			# 보유주식수
			'listing' : 'long',
			# 발행증감
			'listupdn' : 'long',
			# 소진율
			'sjrate' : 'float'
		}
	]
}

# 외인기관종목별동향(t1702)
db_outblock_query_t1702 = {
	't1702OutBlock' : {
		# CTSIDX
		'cts_idx' : 'long',
		# CTSDATE
		'cts_date' : 'char'
	},
	't1702OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 사모펀드
			'amt0000' : 'long',
			# 증권
			'amt0001' : 'long',
			# 보험
			'amt0002' : 'long',
			# 투신
			'amt0003' : 'long',
			# 은행
			'amt0004' : 'long',
			# 종금
			'amt0005' : 'long',
			# 기금
			'amt0006' : 'long',
			# 기타법인
			'amt0007' : 'long',
			# 개인
			'amt0008' : 'long',
			# 등록외국인
			'amt0009' : 'long',
			# 미등록외국인
			'amt0010' : 'long',
			# 국가외
			'amt0011' : 'long',
			# 기관
			'amt0018' : 'long',
			# 외인계(등록+미등록)
			'amt0088' : 'long',
			# 기타계(기타+국가)
			'amt0099' : 'long'
		}
	]
}

# 외인기관종목별동향(t1717)
db_outblock_query_t1717 = {
	't1717OutBlock' : [
		{
			# 일자
			'date' : 'char',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 사모펀드(순매수량)
			'tjj0000_vol' : 'long',
			# 증권(순매수량)
			'tjj0001_vol' : 'long',
			# 보험(순매수량)
			'tjj0002_vol' : 'long',
			# 투신(순매수량)
			'tjj0003_vol' : 'long',
			# 은행(순매수량)
			'tjj0004_vol' : 'long',
			# 종금(순매수량)
			'tjj0005_vol' : 'long',
			# 기금(순매수량)
			'tjj0006_vol' : 'long',
			# 기타법인(순매수량)
			'tjj0007_vol' : 'long',
			# 개인(순매수량)
			'tjj0008_vol' : 'long',
			# 등록외국인(순매수량)
			'tjj0009_vol' : 'long',
			# 미등록외국인(순매수량)
			'tjj0010_vol' : 'long',
			# 국가외(순매수량)
			'tjj0011_vol' : 'long',
			# 기관(순매수량)
			'tjj0018_vol' : 'long',
			# 외인계(순매수량)(등록+미등록)
			'tjj0016_vol' : 'long',
			# 기타계(순매수량)(기타+국가)
			'tjj0017_vol' : 'long',
			# 사모펀드(단가)
			'tjj0000_dan' : 'long',
			# 증권(단가)
			'tjj0001_dan' : 'long',
			# 보험(단가)
			'tjj0002_dan' : 'long',
			# 투신(단가)
			'tjj0003_dan' : 'long',
			# 은행(단가)
			'tjj0004_dan' : 'long',
			# 종금(단가)
			'tjj0005_dan' : 'long',
			# 기금(단가)
			'tjj0006_dan' : 'long',
			# 기타법인(단가)
			'tjj0007_dan' : 'long',
			# 개인(단가)
			'tjj0008_dan' : 'long',
			# 등록외국인(단가)
			'tjj0009_dan' : 'long',
			# 미등록외국인(단가)
			'tjj0010_dan' : 'long',
			# 국가외(단가)
			'tjj0011_dan' : 'long',
			# 기관(단가)
			'tjj0018_dan' : 'long',
			# 외인계(단가)(등록+미등록)
			'tjj0016_dan' : 'long',
			# 기타계(단가)(기타+국가)
			'tjj0017_dan' : 'long'
		}
	]
}

# 종목별상위회원사(t1752)
db_outblock_query_t1752 = {
	't1752OutBlock' : {
		# 외국계매도
		'fwdvl' : 'long',
		# 외국계매수
		'fwsvl' : 'long',
		# CTSIDX
		'cts_idx' : 'long'
	},
	't1752OutBlock1' : [
		{
			# 회원사
			'tradname' : 'char',
			# 매도수량
			'tradmdvol' : 'long',
			# 매수수량
			'tradmsvol' : 'long',
			# 순매수
			'tradmssvol' : 'long',
			# 창구거래
			'wintrd' : 'long',
			# 비중
			'winrat' : 'float',
			# 회원사코드
			'tradno' : 'char',
			# 외국계여부
			'wgubun' : 'char',
			# 순비중
			'swinrat' : 'float'
		}
	]
}

# 회원사리스트(t1764)
db_outblock_query_t1764 = {
	't1764OutBlock' : [
		{
			# 순위
			'rank' : 'long',
			# 거래원번호
			'tradno' : 'char',
			# 거래원이름
			'tradname' : 'char'
		}
	]
}

# 종목별회원사추이(t1771)
db_outblock_query_t1771 = {
	't1771OutBlock' : {
		# CTSIDX
		'cts_idx' : 'long'
	},
	't1771OutBlock2' : [
		{
			# 날짜
			'traddate' : 'char',
			# 시간
			'tradtime' : 'char',
			# 현재가
			'price' : 'long',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도
			'tradmdcha' : 'long',
			# 매수
			'tradmscha' : 'long',
			# 매도대금
			'tradmdval' : 'long',
			# 매수대금
			'tradmsval' : 'long',
			# 순매수
			'tradmsscha' : 'long',
			# 누적순매수
			'tradmttvolume' : 'long',
			# 평균단가
			'tradavg' : 'long',
			# 누적평균단가
			'tradmttavg' : 'long'
		}
	]
}

# 신호조회(t1809)
db_outblock_query_t1809 = {
	't1809OutBlock' : {
		# NEXTKEY
		'cts' : 'char'
	},
	't1809OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 신호ID
			'signal_id' : 'char',
			# 신호명
			'signal_desc' : 'char',
			# 신호강도
			'point' : 'char',
			# 뉴스신호키워드
			'keyword' : 'char',
			# 신호별구분
			'seq' : 'char',
			# 신호구분
			'gubun' : 'char',
			# 신호종목
			'jmcode' : 'char',
			# 종목가격
			'price' : 'long',
			# 종목등락부호
			'sign' : 'char',
			# 대비등락율
			'chgrate' : 'float',
			# 거래량
			'volume' : 'long',
			# 신호일시
			'datetime' : 'char'
		}
	]
}

# 종목Q클릭검색(씽큐스마트)(t1825)
db_outblock_query_t1825 = {
	't1825OutBlock' : {
		# 검색종목수
		'JongCnt' : 'long'
	},
	't1825OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 전일대비구분
			'sign' : 'char',
			# 연속봉수
			'signcnt' : 'long',
			# 현재가
			'close' : 'long',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래량전일대비율
			'volumerate' : 'float'
		}
	]
}

# 종목Q클릭검색리스트조회(씽큐스마트)(t1826)
db_outblock_query_t1826 = {
	't1826OutBlock' : [
		{
			# 검색코드
			'search_cd' : 'char',
			# 검색명
			'search_nm' : 'char'
		}
	]
}

# 종목검색(씽API용)(t1833)
db_outblock_query_t1833 = {
	't1833OutBlock' : {
		# 검색종목수
		'JongCnt' : 'long'
	},
	't1833OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 전일대비구분
			'sign' : 'char',
			# 연속봉수
			'signcnt' : 'long',
			# 현재가
			'close' : 'long',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long'
		}
	]
}

# ETF현재가(시세)조회(t1901)
db_outblock_query_t1901 = {
	't1901OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 누적거래량
		'volume' : 'float',
		# 기준가
		'recprice' : 'long',
		# 가중평균
		'avg' : 'long',
		# 상한가
		'uplmtprice' : 'long',
		# 하한가
		'dnlmtprice' : 'long',
		# 전일거래량
		'jnilvolume' : 'float',
		# 거래량차
		'volumediff' : 'long',
		# 시가
		'open' : 'long',
		# 시가시간
		'opentime' : 'char',
		# 고가
		'high' : 'long',
		# 고가시간
		'hightime' : 'char',
		# 저가
		'low' : 'long',
		# 저가시간
		'lowtime' : 'char',
		# 52최고가
		'high52w' : 'long',
		# 52최고가일
		'high52wdate' : 'char',
		# 52최저가
		'low52w' : 'long',
		# 52최저가일
		'low52wdate' : 'char',
		# 소진율
		'exhratio' : 'float',
		# 외국인보유수량
		'flmtvol' : 'float',
		# PER
		'per' : 'float',
		# 상장주식수(천)
		'listing' : 'long',
		# 증거금율
		'jkrate' : 'long',
		# 회전율
		'vol' : 'float',
		# 단축코드
		'shcode' : 'char',
		# 누적거래대금
		'value' : 'long',
		# 연중최고가
		'highyear' : 'long',
		# 연중최고일자
		'highyeardate' : 'char',
		# 연중최저가
		'lowyear' : 'long',
		# 연중최저일자
		'lowyeardate' : 'char',
		# 업종명
		'upname' : 'char',
		# 업종코드
		'upcode' : 'char',
		# 업종현재가
		'upprice' : 'float',
		# 업종전일비구분
		'upsign' : 'char',
		# 업종전일대비
		'upchange' : 'float',
		# 업종등락율
		'updiff' : 'float',
		# 선물최근월물명
		'futname' : 'char',
		# 선물최근월물코드
		'futcode' : 'char',
		# 선물현재가
		'futprice' : 'float',
		# 선물전일비구분
		'futsign' : 'char',
		# 선물전일대비
		'futchange' : 'float',
		# 선물등락율
		'futdiff' : 'float',
		# NAV
		'nav' : 'float',
		# NAV전일대비구분
		'navsign' : 'char',
		# NAV전일대비
		'navchange' : 'float',
		# NAV등락율
		'navdiff' : 'float',
		# 추적오차율
		'cocrate' : 'float',
		# 괴리율
		'kasis' : 'float',
		# 대용가
		'subprice' : 'long',
		# 매도증권사코드1
		'offerno1' : 'char',
		# 매수증권사코드1
		'bidno1' : 'char',
		# 총매도수량1
		'dvol1' : 'long',
		# 총매수수량1
		'svol1' : 'long',
		# 매도증감1
		'dcha1' : 'long',
		# 매수증감1
		'scha1' : 'long',
		# 매도비율1
		'ddiff1' : 'float',
		# 매수비율1
		'sdiff1' : 'float',
		# 매도증권사코드2
		'offerno2' : 'char',
		# 매수증권사코드2
		'bidno2' : 'char',
		# 총매도수량2
		'dvol2' : 'long',
		# 총매수수량2
		'svol2' : 'long',
		# 매도증감2
		'dcha2' : 'long',
		# 매수증감2
		'scha2' : 'long',
		# 매도비율2
		'ddiff2' : 'float',
		# 매수비율2
		'sdiff2' : 'float',
		# 매도증권사코드3
		'offerno3' : 'char',
		# 매수증권사코드3
		'bidno3' : 'char',
		# 총매도수량3
		'dvol3' : 'long',
		# 총매수수량3
		'svol3' : 'long',
		# 매도증감3
		'dcha3' : 'long',
		# 매수증감3
		'scha3' : 'long',
		# 매도비율3
		'ddiff3' : 'float',
		# 매수비율3
		'sdiff3' : 'float',
		# 매도증권사코드4
		'offerno4' : 'char',
		# 매수증권사코드4
		'bidno4' : 'char',
		# 총매도수량4
		'dvol4' : 'long',
		# 총매수수량4
		'svol4' : 'long',
		# 매도증감4
		'dcha4' : 'long',
		# 매수증감4
		'scha4' : 'long',
		# 매도비율4
		'ddiff4' : 'float',
		# 매수비율4
		'sdiff4' : 'float',
		# 매도증권사코드5
		'offerno5' : 'char',
		# 매수증권사코드5
		'bidno5' : 'char',
		# 총매도수량5
		'dvol5' : 'long',
		# 총매수수량5
		'svol5' : 'long',
		# 매도증감5
		'dcha5' : 'long',
		# 매수증감5
		'scha5' : 'long',
		# 매도비율5
		'ddiff5' : 'float',
		# 매수비율5
		'sdiff5' : 'float',
		# 외국계매도합계수량
		'fwdvl' : 'long',
		# 외국계매도직전대비
		'ftradmdcha' : 'long',
		# 외국계매도비율
		'ftradmddiff' : 'float',
		# 외국계매수합계수량
		'fwsvl' : 'long',
		# 외국계매수직전대비
		'ftradmscha' : 'long',
		# 외국계매수비율
		'ftradmsdiff' : 'float',
		# 참고지수명
		'upname2' : 'char',
		# 참고지수코드
		'upcode2' : 'char',
		# 참고지수현재가
		'upprice2' : 'float',
		# 전일NAV
		'jnilnav' : 'float',
		# 전일NAV전일대비구분
		'jnilnavsign' : 'char',
		# 전일NAV전일대비
		'jnilnavchange' : 'float',
		# 전일NAV등락율
		'jnilnavdiff' : 'float',
		# 순자산총액(억원)
		'etftotcap' : 'long',
		# 스프레드
		'spread' : 'float',
		# 레버리지
		'leverage' : 'long',
		# 과세구분
		'taxgubun' : 'char',
		# 운용사
		'opcom_nmk' : 'char',
		# LP1
		'lp_nm1' : 'char',
		# LP2
		'lp_nm2' : 'char',
		# LP3
		'lp_nm3' : 'char',
		# LP4
		'lp_nm4' : 'char',
		# LP5
		'lp_nm5' : 'char',
		# 복제방법
		'etf_cp' : 'char',
		# 상품유형
		'etf_kind' : 'char',
		# VI발동해제
		'vi_gubun' : 'char'
	}
}

# ETF시간별추이(t1902)
db_outblock_query_t1902 = {
	't1902OutBlock' : {
		# 시간
		'time' : 'char',
		# 종목명
		'hname' : 'char',
		# 업종지수명
		'upname' : 'char'
	},
	't1902OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 누적거래량
			'volume' : 'float',
			# NAV대비
			'navdiff' : 'float',
			# NAV
			'nav' : 'float',
			# 전일대비
			'navchange' : 'float',
			# 추적오차
			'crate' : 'float',
			# 괴리
			'grate' : 'float',
			# 지수
			'jisu' : 'float',
			# 전일대비
			'jichange' : 'float',
			# 전일대비율
			'jirate' : 'float'
		}
	]
}

# ETF일별추이(t1903)
db_outblock_query_t1903 = {
	't1903OutBlock' : {
		# 일자
		'date' : 'char',
		# 종목명
		'hname' : 'char',
		# 업종지수명
		'upname' : 'char'
	},
	't1903OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 누적거래량
			'volume' : 'float',
			# NAV대비
			'navdiff' : 'float',
			# NAV
			'nav' : 'float',
			# 전일대비
			'navchange' : 'float',
			# 추적오차
			'crate' : 'float',
			# 괴리
			'grate' : 'float',
			# 지수
			'jisu' : 'float',
			# 전일대비
			'jichange' : 'float',
			# 전일대비율
			'jirate' : 'float'
		}
	]
}

# ETF구성종목조회(t1904)
db_outblock_query_t1904 = {
	't1904OutBlock' : {
		# 당일구분
		'chk_tday' : 'char',
		# PDF적용일자
		'date' : 'char',
		# ETF현재가
		'price' : 'long',
		# ETF전일대비구분
		'sign' : 'char',
		# ETF전일대비
		'change' : 'long',
		# ETF등락율
		'diff' : 'float',
		# ETF누적거래량
		'volume' : 'long',
		# NAV
		'nav' : 'float',
		# NAV전일대비구분
		'navsign' : 'char',
		# NAV전일대비
		'navchange' : 'float',
		# NAV등락율
		'navdiff' : 'float',
		# 전일NAV
		'jnilnav' : 'float',
		# 전일NAV전일대비구분
		'jnilnavsign' : 'char',
		# 전일NAV전일대비
		'jnilnavchange' : 'float',
		# 전일NAV등락율
		'jnilnavdiff' : 'float',
		# 업종명
		'upname' : 'char',
		# 업종코드
		'upcode' : 'char',
		# 업종현재가
		'upprice' : 'float',
		# 업종전일비구분
		'upsign' : 'char',
		# 업종전일대비
		'upchange' : 'float',
		# 업종등락율
		'updiff' : 'float',
		# 선물최근월물명
		'futname' : 'char',
		# 선물최근월물코드
		'futcode' : 'char',
		# 선물현재가
		'futprice' : 'float',
		# 선물전일비구분
		'futsign' : 'char',
		# 선물전일대비
		'futchange' : 'float',
		# 선물등락율
		'futdiff' : 'float',
		# 참고지수명
		'upname2' : 'char',
		# 참고지수코드
		'upcode2' : 'char',
		# 참고지수현재가
		'upprice2' : 'float',
		# 순자산총액(단위:억)
		'etftotcap' : 'long',
		# 구성종목수
		'etfnum' : 'long',
		# CU주식수
		'etfcunum' : 'long',
		# 현금
		'cash' : 'long',
		# 운용사명
		'opcom_nmk' : 'char',
		# 전종목평가금액합
		'tot_pval' : 'long',
		# 전종목구성시가총액합
		'tot_sigatval' : 'long'
	},
	't1904OutBlock1' : [
		{
			# 단축코드
			'shcode' : 'char',
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 거래대금(백만)
			'value' : 'long',
			# 단위증권수(계약수/원화현금/USD현금/창고증권)
			'icux' : 'long',
			# 액면금액/설정현금액
			'parprice' : 'long',
			# 평가금액
			'pvalue' : 'long',
			# 구성시가총액
			'sigatvalue' : 'long',
			# PDF적용일자
			'profitdate' : 'char',
			# 비중(평가금액)
			'weight' : 'float',
			# ETF종목과등락차
			'diff2' : 'float'
		}
	]
}

# ETFLP호가(t1906)
db_outblock_query_t1906 = {
	't1906OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 누적거래량
		'volume' : 'long',
		# LP매도호가수량1
		'lp_offerrem1' : 'long',
		# LP매수호가수량1
		'lp_bidrem1' : 'long',
		# LP매도호가수량2
		'lp_offerrem2' : 'long',
		# LP매수호가수량2
		'lp_bidrem2' : 'long',
		# LP매도호가수량3
		'lp_offerrem3' : 'long',
		# LP매수호가수량3
		'lp_bidrem3' : 'long',
		# LP매도호가수량4
		'lp_offerrem4' : 'long',
		# LP매수호가수량4
		'lp_bidrem4' : 'lnog',
		# LP매도호가수량5
		'lp_offerrem5' : 'long',
		# LP매수호가수량5
		'lp_bidrem5' : 'long',
		# LP매도호가수량6
		'lp_offerrem6' : 'long',
		# LP매수호가수량6
		'lp_bidrem6' : 'long',
		# LP매도호가수량7
		'lp_offerrem7' : 'long',
		# LP매수호가수량7
		'lp_bidrem7' : 'long',
		# LP매도호가수량8
		'lp_offerrem8' : 'long',
		# LP매수호가수량8
		'lp_bidrem8' : 'long',
		# LP매도호가수량9
		'lp_offerrem9' : 'long',
		# LP매수호가수량9
		'lp_bidrem9' : 'long',
		# LP매도호가수량10
		'lp_offerrem10' : 'long',
		# LP매수호가수량10
		'lp_bidrem10' : 'long',
		# 전일종가
		'jnilclose' : 'long',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 직전매도대비수량1
		'preoffercha1' : 'long',
		# 직전매수대비수량1
		'prebidcha1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 직전매도대비수량2
		'preoffercha2' : 'long',
		# 직전매수대비수량2
		'prebidcha2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 직전매도대비수량3
		'preoffercha3' : 'long',
		# 직전매수대비수량3
		'prebidcha3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 직전매도대비수량4
		'preoffercha4' : 'long',
		# 직전매수대비수량4
		'prebidcha4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 직전매도대비수량5
		'preoffercha5' : 'long',
		# 직전매수대비수량5
		'prebidcha5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가수량6
		'offerrem6' : 'long',
		# 매수호가수량6
		'bidrem6' : 'long',
		# 직전매도대비수량6
		'preoffercha6' : 'long',
		# 직전매수대비수량6
		'prebidcha6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가수량7
		'offerrem7' : 'long',
		# 매수호가수량7
		'bidrem7' : 'long',
		# 직전매도대비수량7
		'preoffercha7' : 'long',
		# 직전매수대비수량7
		'prebidcha7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가수량8
		'offerrem8' : 'long',
		# 매수호가수량8
		'bidrem8' : 'long',
		# 직전매도대비수량8
		'preoffercha8' : 'long',
		# 직전매수대비수량8
		'prebidcha8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가수량9
		'offerrem9' : 'long',
		# 매수호가수량9
		'bidrem9' : 'long',
		# 직전매도대비수량9
		'preoffercha9' : 'long',
		# 직전매수대비수량9
		'prebidcha9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가수량10
		'offerrem10' : 'long',
		# 매수호가수량10
		'bidrem10' : 'long',
		# 직전매도대비수량10
		'preoffercha10' : 'long',
		# 직전매수대비수량10
		'prebidcha10' : 'long',
		# 매도호가수량합
		'offer' : 'long',
		# 매수호가수량합
		'bid' : 'long',
		# 직전매도대비수량합
		'preoffercha' : 'long',
		# 직전매수대비수량합
		'prebidcha' : 'long',
		# 수신시간
		'hotime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결수량
		'yevolume' : 'long',
		# 예상체결전일구분
		'yesign' : 'char',
		# 예상체결전일대비
		'yechange' : 'long',
		# 예상체결등락율
		'yediff' : 'float',
		# 시간외매도잔량
		'tmoffer' : 'long',
		# 시간외매수잔량
		'tmbid' : 'long',
		# 동시구분
		'ho_status' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 상한가
		'uplmtprice' : 'long',
		# 하한가
		'dnlmtprice' : 'long',
		# 시가
		'open' : 'long',
		# 고가
		'high' : 'long',
		# 저가
		'low' : 'long'
	}
}

# 신용거래동향(t1921)
db_outblock_query_t1921 = {
	't1921OutBlock' : {
		# CNT
		'cnt' : 'long',
		# 날짜
		'date' : 'char',
		# IDX
		'idx' : 'long'
	},
	't1921OutBlock1' : [
		{
			# 날짜
			'mmdate' : 'char',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'jchange' : 'long',
			# 등락율
			'diff' : 'float',
			# 신규
			'nvolume' : 'long',
			# 상환
			'svolume' : 'long',
			# 잔고
			'jvolume' : 'long',
			# 금액
			'price' : 'long',
			# 대비
			'change' : 'long',
			# 공여율
			'gyrate' : 'float',
			# 잔고율
			'jkrate' : 'float',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# 종목별신용정보(t1926)
db_outblock_query_t1926 = {
	't1926OutBlock' : {
		# 융자신규수량
		'ynvolume' : 'long',
		# 융자상환수량
		'ysvolume' : 'long',
		# 융자잔고수량
		'yjvolume' : 'long',
		# 융자수량대비
		'yvchange' : 'long',
		# 융자공여율
		'ygrate' : 'float',
		# 융자잔고율
		'yjrate' : 'float',
		# 융자신규금액
		'ynprice' : 'long',
		# 융자상환금액
		'ysprice' : 'long',
		# 융자잔고금액
		'yjprice' : 'long',
		# 융자금액대비
		'yachange' : 'long',
		# 대주신규수량
		'dnvolume' : 'long',
		# 대주상환수량
		'dsvolume' : 'long',
		# 대주잔고수량
		'djvolume' : 'long',
		# 대주수량대비
		'dvchange' : 'long',
		# 대주공여율
		'dgrate' : 'float',
		# 대주잔고율
		'djrate' : 'float',
		# 대주신규금액
		'dnprice' : 'long',
		# 대주상환금액
		'dsprice' : 'long',
		# 대주잔고금액
		'djprice' : 'long',
		# 대주금액대비
		'dachange' : 'long',
		# 결제일
		'mmdate' : 'char',
		# 결제일종가
		'close' : 'long',
		# 결제일거래량
		'volume' : 'long',
		# 결제일거래대금
		'value' : 'long',
		# 주가5일증가율
		'pr5days' : 'float',
		# 주가20일증가율
		'pr20days' : 'float',
		# 융자5일증가율
		'yj5days' : 'float',
		# 융자20일증가율
		'yj20days' : 'float',
		# 대주5일증가율
		'dj5days' : 'float',
		# 대주20일증가율
		'dj20days' : 'float'
	}
}

# 공매도일별추이(t1927)
db_outblock_query_t1927 = {
	't1927OutBlock' : {
		# 일자CTS
		'date' : 'char'
	},
	't1927OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래대금
			'value' : 'long',
			# 공매도수량
			'gm_vo' : 'long',
			# 공매도대금
			'gm_va' : 'long',
			# 공매도거래비중
			'gm_per' : 'float',
			# 평균공매도단가
			'gm_avg' : 'long',
			# 누적공매도수량
			'gm_vo_sum' : 'long'
		}
	]
}

# 종목별대차거래일간추이(t1941)
db_outblock_query_t1941 = {
	't1941OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 종가
			'price' : 'long',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 당일체결
			'upvolume' : 'long',
			# 당일상환
			'dnvolume' : 'long',
			# 당일잔고
			'tovolume' : 'long',
			# 잔고금액
			'tovalue' : 'long',
			# 종목코드
			'shcode' : 'char'
		}
	]
}

# ELW현재가(시세)조회(t1950)
db_outblock_query_t1950 = {
	't1950OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 체결시간
		'chetime' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'float',
		# 기준가
		'recprice' : 'long',
		# 가중평균
		'avg' : 'long',
		# 전일거래량
		'jnilvolume' : 'float',
		# 전일동시간거래량
		'jvolume' : 'float',
		# 전일종가
		'jnilclose' : 'long',
		# 거래량차
		'volumechg' : 'float',
		# 거래량차등락율
		'volumediff' : 'float',
		# 시가
		'open' : 'long',
		# 시가등락율
		'odiff' : 'float',
		# 시가시간
		'opentime' : 'char',
		# 고가
		'high' : 'long',
		# 고가등락율
		'hdiff' : 'float',
		# 고가시간
		'hightime' : 'char',
		# 저가
		'low' : 'long',
		# 저가등락율
		'ldiff' : 'float',
		# 저가시간
		'lowtime' : 'char',
		# 52최고가
		'high52w' : 'long',
		# 52최고가등락율
		'high52wdiff' : 'float',
		# 52최고가일
		'high52wdate' : 'char',
		# 52최저가
		'low52w' : 'long',
		# 52최저가등락율
		'low52wdiff' : 'float',
		# 52최저가일
		'low52wdate' : 'char',
		# 소진율
		'exhratio' : 'float',
		# 상장주식수(천)
		'listing' : 'float',
		# 수량단위
		'memedan' : 'char',
		# 회전율
		'vol' : 'float',
		# 패리티
		'parity' : 'float',
		# 손익분기
		'berate' : 'float',
		# 기어링
		'gearing' : 'float',
		# 행사가
		'elwexec' : 'float',
		# 발행가
		'issueprice' : 'long',
		# 전환비율
		'convrate' : 'float',
		# 최종거래일
		'lastdate' : 'char',
		# 자본지지
		'capt' : 'float',
		# e.기어링
		'egearing' : 'float',
		# 프리미엄
		'premium' : 'float',
		# 스프레드
		'spread' : 'float',
		# 최대스프레드
		'espread' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 상태
		'moneyness' : 'char',
		# 델타
		'delt' : 'float',
		# 감마
		'gama' : 'float',
		# 베가
		'vega' : 'float',
		# 쎄타
		'ceta' : 'float',
		# 로
		'rhox' : 'float',
		# 잔존일수
		'bjandatecnt' : 'long',
		# 행사개시일
		'mmsdate' : 'char',
		# 행사종료일
		'mmedate' : 'char',
		# 지급일
		'payday' : 'char',
		# 발행일
		'listdate' : 'char',
		# LP회원사
		'lpmem' : 'char',
		# LP보유수량
		'lp_holdvol' : 'float',
		# 기초자산코드
		'bcode' : 'char',
		# 기초자산구분
		'bgubun' : 'char',
		# 기초자산현재가
		'bprice' : 'long',
		# 기초자산전일비구분
		'bsign' : 'char',
		# 기초자산전일비
		'bchange' : 'long',
		# 기초자산등락율
		'bdiff' : 'float',
		# 기초자산거래량
		'bvolume' : 'float',
		# 락구분
		'info1' : 'char',
		# 관리/급등구분
		'info2' : 'char',
		# 정지/연장구분
		'info3' : 'char',
		# 투자/불성실구분
		'info4' : 'char',
		# 장구분
		'janginfo' : 'char',
		# 바스켓구분
		'basketgb' : 'char',
		# 바스켓갯수
		'basketcnt' : 'long',
		# ELW권리행사방식
		'elwtype' : 'char',
		# ELW결제방법
		'settletype' : 'char',
		# LP사주문가능여부
		'lpord' : 'char',
		# 권리내용
		'elwdetail' : 'char',
		# 만기평가가격방식
		'valuation' : 'char'
	},
	't1950OutBlock1' : [
		{
			# 기초자산코드
			'bskcode' : 'char',
			# 기초자산비율
			'bskbno' : 'long',
			# 기초자산현재가
			'bskprice' : 'long',
			# 기초자산전일비구분
			'bsksign' : 'char',
			# 기초자산전일비
			'bskchange' : 'long',
			# 기초자산등락율
			'bskdiff' : 'float',
			# 기초자산거래량
			'bskvolume' : 'float',
			# 기초자산전일종가
			'bskjnilclose' : 'long'
		}
	]
}

# ELW시간대별체결조회(t1951)
db_outblock_query_t1951 = {
	't1951OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't1951OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도체결수량
			'mdvolume' : 'long',
			# 매도체결건수
			'mdchecnt' : 'long',
			# 매수체결수량
			'msvolume' : 'long',
			# 매수체결건수
			'mschecnt' : 'long',
			# 순체결량
			'revolume' : 'long',
			# 순체결건수
			'rechecnt' : 'long'
		}
	]
}

# ELW일별주가(t1954)
db_outblock_query_t1954 = {
	't1954OutBlock' : {
		# 날짜
		'date' : 'char',
		# 기초자산구분
		'bsjgubun' : 'char',
		# 기초자산코드(현물)
		'bscode' : 'char',
		# 기초자산코드(지수)
		'bjcode' : 'char'
	},
	't1954OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'float',
			# 기초자산(현물)
			'bsprice' : 'long',
			# 기초자산(지수)
			'bjprice' : 'float',
			# 전일대비구분
			'bsign' : 'char',
			# 전일대비(현물)
			'bschange' : 'long',
			# 전일대비(지수)
			'bjchange' : 'float',
			# 등락율
			'bdiff' : 'float',
			# 기초자산거래량
			'bvolume' : 'float',
			# 패리티
			'parity' : 'float',
			# e.기어링
			'egearing' : 'float',
			# 프리미엄
			'premium' : 'float',
			# 손익분기
			'berate' : 'float',
			# 자본지지
			'capt' : 'float',
			# 기어링
			'gearing' : 'float',
			# Moneyness
			'mness' : 'char'
		}
	]
}

# ELW지표검색(t1955)
db_outblock_query_t1955 = {
	't1955OutBlock' : {
		# 종목갯수
		'cnt' : 'long'
	},
	't1955OutBlock1' : [
		{
			# 종목명
			'hname' : 'char',
			# 종목코드
			'shcode' : 'char',
			# 발행사
			'issuernmk' : 'char',
			# 기초자산코드
			'itemcode' : 'char',
			# 콜/풋구분
			'cpgubun' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'float',
			# 전일거래량
			'jnilvolume' : 'float',
			# 행사가
			'elwexec' : 'float',
			# 기초자산명
			'item' : 'char',
			# 기초자산가
			'bprice' : 'float',
			# 기초전일대비구분
			'bsign' : 'char',
			# 기초전일대비
			'bchange' : 'float',
			# 기초등락율
			'bdiff' : 'float',
			# 프리미엄
			'premium' : 'float',
			# 패리티
			'parity' : 'float',
			# 손익분기
			'berate' : 'float',
			# 자본지지
			'capt' : 'float',
			# e.기어링
			'egearing' : 'float',
			# 기어링
			'gearing' : 'float',
			# 최종거래일
			'lastdate' : 'char',
			# 델타
			'delta' : 'float',
			# 쎄타
			'theta' : 'float'
		}
	]
}

# ELW현재가(확정지급액)조회(t1956)
db_outblock_query_t1956 = {
	't1956OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 체결시간
		'chetime' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'float',
		# 기준가
		'recprice' : 'long',
		# 가중평균
		'avg' : 'long',
		# 전일거래량
		'jnilvolume' : 'float',
		# 전일동시간거래량
		'jvolume' : 'float',
		# 전일종가
		'jnilclose' : 'long',
		# 거래량차
		'volumechg' : 'float',
		# 거래량차등락율
		'volumediff' : 'float',
		# 시가
		'open' : 'long',
		# 시가등락율
		'odiff' : 'float',
		# 시가시간
		'opentime' : 'char',
		# 고가
		'high' : 'long',
		# 고가등락율
		'hdiff' : 'float',
		# 고가시간
		'hightime' : 'char',
		# 저가
		'low' : 'long',
		# 저가등락율
		'ldiff' : 'float',
		# 저가시간
		'lowtime' : 'char',
		# 52최고가
		'high52w' : 'long',
		# 52최고가등락율
		'high52wdiff' : 'float',
		# 52최고가일
		'high52wdate' : 'char',
		# 52최저가
		'low52w' : 'long',
		# 52최저가등락율
		'low52wdiff' : 'float',
		# 52최저가일
		'low52wdate' : 'char',
		# 소진율
		'exhratio' : 'float',
		# 상장주식수(천)
		'listing' : 'float',
		# 수량단위
		'memedan' : 'char',
		# 회전율
		'vol' : 'float',
		# 패리티
		'parity' : 'float',
		# 손익분기
		'berate' : 'float',
		# 기어링
		'gearing' : 'float',
		# 행사가
		'elwexec' : 'float',
		# 발행가
		'issueprice' : 'long',
		# 전환비율
		'convrate' : 'float',
		# 최종거래일
		'lastdate' : 'char',
		# 자본지지
		'capt' : 'float',
		# e.기어링
		'egearing' : 'float',
		# 프리미엄
		'premium' : 'float',
		# 스프레드
		'spread' : 'float',
		# 최대스프레드
		'espread' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 상태
		'moneyness' : 'char',
		# 델타
		'delt' : 'float',
		# 감마
		'gama' : 'float',
		# 베가
		'vega' : 'float',
		# 쎄타
		'ceta' : 'float',
		# 로
		'rhox' : 'float',
		# 잔존일수
		'bjandatecnt' : 'long',
		# 행사개시일
		'mmsdate' : 'char',
		# 행사종료일
		'mmedate' : 'char',
		# 지급일
		'payday' : 'char',
		# 발행일
		'listdate' : 'char',
		# LP회원사
		'lpmem' : 'char',
		# LP보유수량
		'lp_holdvol' : 'float',
		# 기초자산코드
		'bcode' : 'char',
		# 기초자산구분
		'bgubun' : 'char',
		# 기초자산현재가
		'bprice' : 'long',
		# 기초자산전일비구분
		'bsign' : 'char',
		# 기초자산전일비
		'bchange' : 'long',
		# 기초자산등락율
		'bdiff' : 'float',
		# 기초자산거래량
		'bvolume' : 'float',
		# 락구분
		'info1' : 'char',
		# 관리/급등구분
		'info2' : 'char',
		# 정지/연장구분
		'info3' : 'char',
		# 투자/불성실구분
		'info4' : 'char',
		# 장구분
		'janginfo' : 'char',
		# 바스켓구분
		'basketgb' : 'char',
		# 바스켓갯수
		'basketcnt' : 'long',
		# ELW권리행사방식
		'elwtype' : 'char',
		# ELW결제방법
		'settletype' : 'char',
		# LP사주문가능여부
		'lpord' : 'char',
		# 권리내용
		'elwdetail' : 'char',
		# 만기평가가격방식
		'valuation' : 'char',
		# 확정지급액
		'givemoney' : 'float'
	},
	't1956OutBlock1' : [
		{
			# 기초자산코드
			'bskcode' : 'char',
			# 기초자산비율
			'bskbno' : 'long',
			# 기초자산현재가
			'bskprice' : 'long',
			# 기초자산전일비구분
			'bsksign' : 'char',
			# 기초자산전일비
			'bskchange' : 'long',
			# 기초자산등락율
			'bskdiff' : 'float',
			# 기초자산거래량
			'bskvolume' : 'float',
			# 기초자산전일종가
			'bskjnilclose' : 'long'
		}
	]
}

# ELW종목비교(t1958)
db_outblock_query_t1958 = {
	't1958OutBlock' : {
		# 종목명
		'hname' : 'char',
		# 기초자산
		'item1' : 'char',
		# 발행사
		'issuernmk' : 'char',
		# 콜풋구분
		'elwopt' : 'char',
		# 행사방식
		'elwtype' : 'char',
		# 결제방법
		'settletype' : 'char',
		# 행사가
		'elwexec' : 'float',
		# 전환비율
		'convrate' : 'float',
		# 발행수량
		'listing' : 'float',
		# 행사개시일
		'mmsdate' : 'char',
		# 최종거래일
		'lastdate' : 'char',
		# 거래잔존일수
		'nofdays' : 'long',
		# 지급일
		'payday' : 'char',
		# 패리티
		'parity' : 'float',
		# 프리미엄
		'premium' : 'float',
		# 손익분기
		'berate' : 'float',
		# 자본지지
		'capt' : 'float',
		# 기어링
		'gearing' : 'float',
		# e.기어링
		'egearing' : 'float',
		# 가격
		'price' : 'long',
		# 거래량
		'volume' : 'float',
		# 등락율
		'diff' : 'float'
	},
	't1958OutBlock1' : {
		# 종목명
		'hname' : 'char',
		# 기초자산
		'item1' : 'char',
		# 발행사
		'issuernmk' : 'char',
		# 콜풋구분
		'elwopt' : 'char',
		# 행사방식
		'elwtype' : 'char',
		# 결제방법
		'settletype' : 'char',
		# 행사가
		'elwexec' : 'float',
		# 전환비율
		'convrate' : 'float',
		# 발행수량
		'listing' : 'float',
		# 행사개시일
		'mmsdate' : 'char',
		# 최종거래일
		'lastdate' : 'char',
		# 거래잔존일수
		'nofdays' : 'long',
		# 지급일
		'payday' : 'char',
		# 패리티
		'parity' : 'float',
		# 프리미엄
		'premium' : 'float',
		# 손익분기
		'berate' : 'float',
		# 자본지지
		'capt' : 'float',
		# 기어링
		'gearing' : 'float',
		# e.기어링
		'egearing' : 'float',
		# 가격
		'price' : 'long',
		# 거래량
		'volume' : 'float',
		# 등락율
		'diff' : 'float'
	},
	't1958OutBlock2' : {
		# 종목명비교
		'hnamecmp' : 'char',
		# 기초자산비교
		'item1cmp' : 'char',
		# 발행사비교
		'issuernmkcmp' : 'char',
		# 콜풋구분비교
		'elwoptcmp' : 'char',
		# 행사방식비교
		'elwtypecmp' : 'char',
		# 결제방법비교
		'settlecmp' : 'char',
		# 행사가비교
		'elwexeccmp' : 'float',
		# 전환비율비교
		'convcmp' : 'float',
		# 발행수량비교
		'listingcmp' : 'float',
		# 행사개시일비교
		'mmsdatecmp' : 'char',
		# 최종거래일비교
		'lastdatecmp' : 'char',
		# 거래잔존일수비교
		'nofdayscmp' : 'char',
		# 지급일비교
		'paydaycmp' : 'char',
		# 패리티비교
		'paritycmp' : 'float',
		# 프리미엄비교
		'premiumcmp' : 'float',
		# 손익분기비교
		'beratecmp' : 'float',
		# 자본지지비교
		'captcmp' : 'float',
		# 기어링비교
		'gearingcmp' : 'float',
		# e.기어링비교
		'egearingcmp' : 'float',
		# 가격비교
		'pricecmp' : 'long',
		# 거래량비교
		'volumecmp' : 'float',
		# 등락율비교
		'diffcmp' : 'float'
	}
}

# LP대상종목정보조회(t1959)
db_outblock_query_t1959 = {
	't1959OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'char',
			# 부호
			'sign' : 'char',
			# 대비
			'change' : 'char',
			# 등락율
			'rate' : 'float',
			# 누적거래량
			'volume' : 'char',
			# 누적거래대금
			'value' : 'char',
			# LP주문가능여부
			'lp_gb' : 'char',
			# LP회원사명1
			'lp_mem_nm1' : 'char',
			# LP회원사명2
			'lp_mem_nm2' : 'char',
			# LP회원사명3
			'lp_mem_nm3' : 'char',
			# LP회원사명4
			'lp_mem_nm4' : 'char',
			# LP회원사명5
			'lp_mem_nm5' : 'char',
			# LP최소호가수량
			'lp_min_qty' : 'char',
			# LP시작일
			'lp_st_date' : 'char',
			# LP종료일
			'lp_end_date' : 'char',
			# LP스프레드
			'lp_spread' : 'float'
		}
	]
}

# ELW등락율상위(t1960)
db_outblock_query_t1960 = {
	't1960OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1960OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'double',
			# 행사가
			'elwexec' : 'double',
			# 전환비율
			'convrate' : 'double',
			# 만기일
			'lastdate' : 'char',
			# 기초자산종목코드
			'itemcode' : 'char',
			# 기초자산단축코드
			'itemshcode' : 'char',
			# 기초자산종목명
			'itemname' : 'char',
			# 기초자산현재가
			'itemprice' : 'char',
			# 기초자산대비구분
			'itemsign' : 'char',
			# 기초자산전일대비
			'itemchange' : 'char',
			# 기초자산등락율
			'itemdiff' : 'double',
			# ELW종목코드
			'elwshcode' : 'char',
			# 손익분기점
			'bepoint' : 'double'
		}
	]
}

# ELW거래량상위(t1961)
db_outblock_query_t1961 = {
	't1961OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1961OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'double',
			# 전일거래량
			'jnilvolume' : 'double',
			# 행사가
			'elwexec' : 'double',
			# 전환비율
			'convrate' : 'double',
			# 만기일
			'lastdate' : 'char',
			# 기초자산종목코드
			'itemcode' : 'char',
			# 기초자산단축코드
			'itemshcode' : 'char',
			# 기초자산종목명
			'itemname' : 'char',
			# 기초자산현재가
			'itemprice' : 'char',
			# 기초자산대비구분
			'itemsign' : 'char',
			# 기초자산전일대비
			'itemchange' : 'char',
			# 기초자산등락율
			'itemdiff' : 'double',
			# ELW종목코드
			'elwshcode' : 'char'
		}
	]
}

# ELW전광판(t1964)
db_outblock_query_t1964 = {
	't1964OutBlock1' : [
		{
			# ELW코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 기초자산코드
			'item1' : 'char',
			# 기초자산명
			'itemnm' : 'char',
			# 발행사
			'issuernmk' : 'char',
			# 콜풋구분
			'elwopt' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 행사가
			'elwexec' : 'float',
			# 잔존일수
			'jandatecnt' : 'long',
			# 전환비율
			'convrate' : 'float',
			# 최종거래일
			'lastdate' : 'char',
			# 행사개시일
			'mmsdate' : 'char',
			# 지급일
			'payday' : 'char',
			# 발행수량
			'listing' : 'long',
			# 머니구분
			'atmgbnm' : 'char',
			# 패리티
			'parity' : 'float',
			# 프리미엄
			'preminum' : 'float',
			# 스프래드
			'spread' : 'float',
			# 손익분기율
			'berate' : 'float',
			# 자본지지율
			'capt' : 'float',
			# 기어링
			'gearing' : 'float',
			# e기어링
			'egearing' : 'float',
			# 기초자산현재가
			'itemprice' : 'long',
			# 기초자산전일대비구분
			'itemsign' : 'char',
			# 기초자산전일대비
			'itemchange' : 'long',
			# 기초자산등락율
			'itemdiff' : 'float',
			# 기초자산거래량
			'itemvolume' : 'long',
			# 전일거래량
			'jnilvolume' : 'long',
			# 이론가
			'theoryprice' : 'float',
			# LP보유비율
			'lp_rate' : 'float',
			# 내재변동성
			'impv' : 'float',
			# 델타
			'delta' : 'float',
			# 쎄타
			'theta' : 'float'
		}
	]
}

# ELW거래대금상위(t1966)
db_outblock_query_t1966 = {
	't1966OutBlock' : {
		# IDX
		'idx' : 'long'
	},
	't1966OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래대금
			'value' : 'double',
			# 전일거래대금
			'jnilvalue' : 'double',
			# 행사가
			'elwexec' : 'double',
			# 전환비율
			'convrate' : 'double',
			# 만기일
			'lastdate' : 'char',
			# 기초자산종목코드
			'itemcode' : 'char',
			# 기초자산단축코드
			'itemshcode' : 'char',
			# 기초자산종목명
			'itemname' : 'char',
			# 기초자산현재가
			'itemprice' : 'char',
			# 기초자산대비구분
			'itemsign' : 'char',
			# 기초자산전일대비
			'itemchange' : 'char',
			# 기초자산등락율
			'itemdiff' : 'double',
			# ELW종목코드
			'elwshcode' : 'char'
		}
	]
}

# ELW현재가호가조회(t1971)
db_outblock_query_t1971 = {
	't1971OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 누적거래량
		'volume' : 'float',
		# 전일종가
		'jnilclose' : 'long',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가수량1
		'offerrem1' : 'long',
		# LP매도호가수량1
		'lp_offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# LP매수호가수량1
		'lp_bidrem1' : 'long',
		# 직전매도대비수량1
		'preoffercha1' : 'long',
		# 직전매수대비수량1
		'prebidcha1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가수량2
		'offerrem2' : 'long',
		# LP매도호가수량2
		'lp_offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# LP매수호가수량2
		'lp_bidrem2' : 'long',
		# 직전매도대비수량2
		'preoffercha2' : 'long',
		# 직전매수대비수량2
		'prebidcha2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가수량3
		'offerrem3' : 'long',
		# LP매도호가수량3
		'lp_offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# LP매수호가수량3
		'lp_bidrem3' : 'long',
		# 직전매도대비수량3
		'preoffercha3' : 'long',
		# 직전매수대비수량3
		'prebidcha3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가수량4
		'offerrem4' : 'long',
		# LP매도호가수량4
		'lp_offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# LP매수호가수량4
		'lp_bidrem4' : 'long',
		# 직전매도대비수량4
		'preoffercha4' : 'long',
		# 직전매수대비수량4
		'prebidcha4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가수량5
		'offerrem5' : 'long',
		# LP매도호가수량5
		'lp_offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# LP매수호가수량5
		'lp_bidrem5' : 'long',
		# 직전매도대비수량5
		'preoffercha5' : 'long',
		# 직전매수대비수량5
		'prebidcha5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가수량6
		'offerrem6' : 'long',
		# LP매도호가수량6
		'lp_offerrem6' : 'long',
		# 매수호가수량6
		'bidrem6' : 'long',
		# LP매수호가수량6
		'lp_bidrem6' : 'long',
		# 직전매도대비수량6
		'preoffercha6' : 'long',
		# 직전매수대비수량6
		'prebidcha6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가수량7
		'offerrem7' : 'long',
		# LP매도호가수량7
		'lp_offerrem7' : 'long',
		# 매수호가수량7
		'bidrem7' : 'long',
		# LP매수호가수량7
		'lp_bidrem7' : 'long',
		# 직전매도대비수량7
		'preoffercha7' : 'long',
		# 직전매수대비수량7
		'prebidcha7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가수량8
		'offerrem8' : 'long',
		# LP매도호가수량8
		'lp_offerrem8' : 'long',
		# 매수호가수량8
		'bidrem8' : 'long',
		# LP매수호가수량8
		'lp_bidrem8' : 'long',
		# 직전매도대비수량8
		'preoffercha8' : 'long',
		# 직전매수대비수량8
		'prebidcha8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가수량9
		'offerrem9' : 'long',
		# LP매도호가수량9
		'lp_offerrem9' : 'long',
		# 매수호가수량9
		'bidrem9' : 'long',
		# LP매수호가수량9
		'lp_bidrem9' : 'long',
		# 직전매도대비수량9
		'preoffercha9' : 'long',
		# 직전매수대비수량9
		'prebidcha9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가수량10
		'offerrem10' : 'long',
		# LP매도호가수량10
		'lp_offerrem10' : 'long',
		# 매수호가수량10
		'bidrem10' : 'long',
		# LP매수호가수량10
		'lp_bidrem10' : 'long',
		# 직전매도대비수량10
		'preoffercha10' : 'long',
		# 직전매수대비수량10
		'prebidcha10' : 'long',
		# 매도호가수량합
		'offer' : 'long',
		# 매수호가수량합
		'bid' : 'long',
		# 직전매도대비수량합
		'preoffercha' : 'long',
		# 직전매수대비수량합
		'prebidcha' : 'long',
		# 수신시간
		'hotime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결수량
		'yevolume' : 'float',
		# 예상체결전일구분
		'yesign' : 'char',
		# 예상체결전일대비
		'yechange' : 'long',
		# 예상체결등락율
		'yediff' : 'float',
		# 시간외매도잔량
		'tmoffer' : 'long',
		# 시간외매수잔량
		'tmbid' : 'long',
		# 동시구분
		'ho_status' : 'char',
		# 시가
		'open' : 'long',
		# 고가
		'high' : 'long',
		# 저가
		'low' : 'long',
		# ELW권리형태(1:표준2:디지털3:조기종료)
		'invidx' : 'char',
		# KO베리어
		'koba_stdprc' : 'float',
		# KO접근도
		'koba_acc_rt' : 'float',
		# KO발생여부(Y/N)
		'koba_yn' : 'char'
	}
}

# ELW현재가(거래원)조회(t1972)
db_outblock_query_t1972 = {
	't1972OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 표준코드
		'expcode' : 'char',
		# 단축코드
		'shcode' : 'char',
		# 매도증권사코드1
		'offerno1' : 'char',
		# 매수증권사코드1
		'bidno1' : 'char',
		# 총매도수량1
		'dvol1' : 'long',
		# 총매수수량1
		'svol1' : 'long',
		# 매도증감1
		'dcha1' : 'long',
		# 매수증감1
		'scha1' : 'long',
		# 매도비율1
		'ddiff1' : 'float',
		# 매수비율1
		'sdiff1' : 'float',
		# 매도증권사코드2
		'offerno2' : 'char',
		# 매수증권사코드2
		'bidno2' : 'char',
		# 총매도수량2
		'dvol2' : 'long',
		# 총매수수량2
		'svol2' : 'long',
		# 매도증감2
		'dcha2' : 'long',
		# 매수증감2
		'scha2' : 'long',
		# 매도비율2
		'ddiff2' : 'float',
		# 매수비율2
		'sdiff2' : 'float',
		# 매도증권사코드3
		'offerno3' : 'char',
		# 매수증권사코드3
		'bidno3' : 'char',
		# 총매도수량3
		'dvol3' : 'long',
		# 총매수수량3
		'svol3' : 'long',
		# 매도증감3
		'dcha3' : 'long',
		# 매수증감3
		'scha3' : 'long',
		# 매도비율3
		'ddiff3' : 'float',
		# 매수비율3
		'sdiff3' : 'float',
		# 매도증권사코드4
		'offerno4' : 'char',
		# 매수증권사코드4
		'bidno4' : 'char',
		# 총매도수량4
		'dvol4' : 'long',
		# 총매수수량4
		'svol4' : 'long',
		# 매도증감4
		'dcha4' : 'long',
		# 매수증감4
		'scha4' : 'long',
		# 매도비율4
		'ddiff4' : 'float',
		# 매수비율4
		'sdiff4' : 'float',
		# 매도증권사코드5
		'offerno5' : 'char',
		# 매수증권사코드5
		'bidno5' : 'char',
		# 총매도수량5
		'dvol5' : 'long',
		# 총매수수량5
		'svol5' : 'long',
		# 매도증감5
		'dcha5' : 'long',
		# 매수증감5
		'scha5' : 'long',
		# 매도비율5
		'ddiff5' : 'float',
		# 매수비율5
		'sdiff5' : 'float',
		# 외국계매도합계수량
		'fwdvl' : 'long',
		# 외국계매수합계수량
		'fwsvl' : 'long',
		# 외국계매도직전대비
		'ftradmdcha' : 'long',
		# 외국계매수직전대비
		'ftradmscha' : 'long',
		# 외국계매도합계비율
		'fwddiff' : 'float',
		# 외국계매수합계비율
		'fwsdiff' : 'float'
	}
}

# ELW시간대별예상체결조회(t1973)
db_outblock_query_t1973 = {
	't1973OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't1973OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 예상체결가격
			'yeprice' : 'long',
			# 예상체결구분
			'yegubun' : 'char',
			# 전일종가대비구분
			'jnilysign' : 'char',
			# 전일종가대비
			'jnilychange' : 'long',
			# 예상체결등락율
			'yediff' : 'float',
			# 예상체결량
			'yevolume' : 'long',
			# 예상매도체결량
			'ymdvolume' : 'long',
			# 예상매수체결량
			'ymsvolume' : 'long'
		}
	]
}

# ELW기초자산동일종목(t1974)
db_outblock_query_t1974 = {
	't1974OutBlock' : {
		# 종목갯수
		'cnt' : 'long'
	},
	't1974OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 콜/풋구분
			'cpgubun' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'float'
		}
	]
}

# 기초자산리스트조회(t1981)
db_outblock_query_t1981 = {
	't1981OutBlock' : {
		# 코스피종목건수
		'ksp_cnt' : 'char',
		# 코스닥종목건수
		'ksd_cnt' : 'char'
	},
	't1981OutBlock1' : [
		{
			# 단축코드
			'shcode' : 'char',
			# 표준코드
			'expcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'char',
			# 부호
			'sign' : 'char',
			# 대비
			'change' : 'char',
			# 등락율
			'rate' : 'float',
			# 누적거래량(주)
			'volume' : 'char',
			# 누적거래대금(백만)
			'value' : 'char',
			# 시장구분
			'mkt_gb' : 'char'
		}
	]
}

# 선물/옵션현재가(시세)조회(t2101)
db_outblock_query_t2101 = {
	't2101OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 전일종가
		'jnilclose' : 'float',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래대금
		'value' : 'long',
		# 미결제량
		'mgjv' : 'long',
		# 미결제증감
		'mgjvdiff' : 'long',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 상한가
		'uplmtprice' : 'float',
		# 하한가
		'dnlmtprice' : 'float',
		# 52최고가
		'high52w' : 'float',
		# 52최저가
		'low52w' : 'float',
		# 베이시스
		'basis' : 'float',
		# 기준가
		'recprice' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 괴리율
		'glyl' : 'float',
		# CB상한가
		'cbhprice' : 'float',
		# CB하한가
		'cblprice' : 'float',
		# 만기일
		'lastmonth' : 'char',
		# 잔여일
		'jandatecnt' : 'long',
		# 종합지수
		'pricejisu' : 'float',
		# 종합지수전일대비구분
		'jisusign' : 'char',
		# 종합지수전일대비
		'jisuchange' : 'float',
		# 종합지수등락율
		'jisudiff' : 'float',
		# KOSPI200지수
		'kospijisu' : 'float',
		# KOSPI200전일대비구분
		'kospisign' : 'char',
		# KOSPI200전일대비
		'kospichange' : 'float',
		# KOSPI200등락율
		'kospidiff' : 'float',
		# 상장최고가
		'listhprice' : 'float',
		# 상장최저가
		'listlprice' : 'float',
		# 델타
		'delt' : 'float',
		# 감마
		'gama' : 'float',
		# 세타
		'ceta' : 'float',
		# 베가
		'vega' : 'float',
		# 로우
		'rhox' : 'float',
		# 근월물현재가
		'gmprice' : 'float',
		# 근월물전일대비구분
		'gmsign' : 'char',
		# 근월물전일대비
		'gmchange' : 'float',
		# 근월물등락율
		'gmdiff' : 'float',
		# 이론가
		'theorypriceg' : 'float',
		# 역사적변동성
		'histimpv' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 시장BASIS
		'sbasis' : 'float',
		# 이론BASIS
		'ibasis' : 'float',
		# 근월물종목코드
		'gmfutcode' : 'char',
		# 행사가
		'actprice' : 'float',
		# 거래소민감도수신시간
		'greeks_time' : 'char',
		# 거래소민감도확정여부
		'greeks_confirm' : 'char',
		# 단일가호가여부
		'danhochk' : 'char',
		# 예상체결가
		'yeprice' : 'float',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilychange' : 'float',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 배분구분(1:배분개시2:배분해제0:미발생)
		'alloc_gubun' : 'char',
		# 잔여일(영업일)
		'bjandatecnt' : 'long',
		# 종목코드
		'focode' : 'char',
		# 실시간가격제한여부(0:대상아님1:적용중2:미적용중3:일시해제)
		'dy_gubun' : 'char',
		# 실시간상한가
		'dy_uplmtprice' : 'float',
		# 실시간하한가
		'dy_dnlmtprice' : 'float'
	}
}

# 선물/옵션현재가호가조회(t2105)
db_outblock_query_t2105 = {
	't2105OutBlock' : {
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래량전일동시간비율
		'stimeqrt' : 'float',
		# 전일종가
		'jnilclose' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'dcnt1' : 'long',
		# 매수호가건수1
		'scnt1' : 'long',
		# 매도호가2
		'offerho2' : 'float',
		# 매수호가2
		'bidho2' : 'float',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'dcnt2' : 'long',
		# 매수호가건수2
		'scnt2' : 'long',
		# 매도호가3
		'offerho3' : 'float',
		# 매수호가3
		'bidho3' : 'float',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'dcnt3' : 'long',
		# 매수호가건수3
		'scnt3' : 'long',
		# 매도호가4
		'offerho4' : 'float',
		# 매수호가4
		'bidho4' : 'float',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'dcnt4' : 'long',
		# 매수호가건수4
		'scnt4' : 'long',
		# 매도호가5
		'offerho5' : 'float',
		# 매수호가5
		'bidho5' : 'float',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'dcnt5' : 'long',
		# 매수호가건수5
		'scnt5' : 'long',
		# 매도호가총수량
		'dvol' : 'long',
		# 매수호가총수량
		'svol' : 'long',
		# 총매도호가건수
		'toffernum' : 'long',
		# 총매수호가건수
		'tbidnum' : 'long',
		# 수신시간
		'time' : 'char',
		# 단축코드
		'shcode' : 'char'
	}
}

# 선물/옵션현재가시세메모(t2106)
db_outblock_query_t2106 = {
	't2106OutBlock' : {
		# 출력건수
		'nrec' : 'char'
	},
	't2106OutBlock1' : [
		{
			# 인덱스
			'indx' : 'char',
			# 조건구분
			'gubn' : 'char',
			# 출력값
			'vals' : 'char'
		}
	]
}

# 선물옵션시간대별체결조회(t2201)
db_outblock_query_t2201 = {
	't2201OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't2201OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 매도호가
			'offerho' : 'float',
			# 매수호가
			'bidho' : 'float',
			# 거래량
			'volume' : 'double',
			# 미결수량
			'openyak' : 'long',
			# 미결전일증감
			'jnilopenupdn' : 'long',
			# 이론BASIS
			'ibasis' : 'float',
			# 시장BASIS
			'sbasis' : 'float',
			# 괴리율
			'kasis' : 'float',
			# 거래대금
			'value' : 'double',
			# 미결직전증감
			'j_openupdn' : 'long',
			# 누적매수체결량
			'n_msvolume' : 'double',
			# 누적매도체결량
			'n_mdvolume' : 'double',
			# 누적순매수체결량
			's_msvolume' : 'double',
			# 누적매수체결건수
			'n_mschecnt' : 'long',
			# 누적매도체결건수
			'n_mdchecnt' : 'long',
			# 누적순매수체결건수
			's_mschecnt' : 'long'
		}
	]
}

# 기간별주가(t2203)
db_outblock_query_t2203 = {
	't2203OutBlock' : {
		# 날짜
		'date' : 'char',
		# CTS종목코드
		'cts_code' : 'char',
		# 전종목만기일
		'lastdate' : 'char',
		# 최근월선물여부
		'nowfutyn' : 'char'
	},
	't2203OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openyakupdn' : 'long',
			# 거래대금
			'value' : 'float'
		}
	]
}

# 선물옵션틱분별체결조회챠트(t2209)
db_outblock_query_t2209 = {
	't2209OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 거래량
			'volume' : 'double',
			# 거래대금
			'value' : 'double',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openupdn' : 'long',
			# 체결수량
			'cvolume' : 'long',
			# 매수순간체결건수
			's_mschecnt' : 'long',
			# 매도순간체결건수
			's_mdchecnt' : 'long',
			# 순매수순간체결건수
			'ss_mschecnt' : 'long',
			# 매수순간체결량
			's_mschevol' : 'double',
			# 매도순간체결량
			's_mdchevol' : 'double',
			# 순매수순간체결량
			'ss_mschevol' : 'double',
			# 체결강도(거래량)
			'chdegvol' : 'float',
			# 체결강도(건수)
			'chdegcnt' : 'float'
		}
	]
}

# 선물옵션시간대별체결조회(단일출력용)
db_outblock_query_t2210 = {
	't2210OutBlock' : {
		# 매도체결수량
		'mdvolume' : 'long',
		# 매도체결건수
		'mdchecnt' : 'long',
		# 매수체결수량
		'msvolume' : 'long',
		# 매수체결건수
		'mschecnt' : 'long'
	}
}

# 옵션전광판(t2301)
db_outblock_query_t2301 = {
	't2301OutBlock' : {
		# 역사적변동성
		'histimpv' : 'long',
		# 옵션잔존일
		'jandatecnt' : 'long',
		# 콜옵션대표IV
		'cimpv' : 'float',
		# 풋옵션대표IV
		'pimpv' : 'float',
		# 근월물현재가
		'gmprice' : 'float',
		# 근월물전일대비구분
		'gmsign' : 'char',
		# 근월물전일대비
		'gmchange' : 'float',
		# 근월물등락율
		'gmdiff' : 'float',
		# 근월물거래량
		'gmvolume' : 'long',
		# 근월물선물코드
		'gmshcode' : 'char'
	},
	't2301OutBlock1' : [
		{
			# 행사가
			'actprice' : 'float',
			# 콜옵션코드
			'optcode' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# IV
			'iv' : 'float',
			# 미결제약정
			'mgjv' : 'long',
			# 미결제약정증감
			'mgjvupdn' : 'long',
			# 매도호가
			'offerho1' : 'float',
			# 매수호가
			'bidho1' : 'float',
			# 체결량
			'cvolume' : 'long',
			# 델타
			'delt' : 'float',
			# 감마
			'gama' : 'float',
			# 베가
			'vega' : 'float',
			# 쎄타
			'ceta' : 'float',
			# 로우
			'rhox' : 'float',
			# 이론가
			'theoryprice' : 'float',
			# 내재가치
			'impv' : 'float',
			# 시간가치
			'timevl' : 'float',
			# 잔고수량
			'jvolume' : 'long',
			# 평가손익
			'parpl' : 'long',
			# 청산가능수량
			'jngo' : 'long',
			# 매도잔량
			'offerrem1' : 'long',
			# 매수잔량
			'bidrem1' : 'long',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# ATM구분
			'atmgubun' : 'char',
			# 지수환산
			'jisuconv' : 'float',
			# 거래대금
			'value' : 'float'
		}
	],
	't2301OutBlock2' : [
		{
			# 행사가
			'actprice' : 'float',
			# 풋옵션코드
			'optcode' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# IV
			'iv' : 'float',
			# 미결제약정
			'mgjv' : 'long',
			# 미결제약정증감
			'mgjvupdn' : 'long',
			# 매도호가
			'offerho1' : 'float',
			# 매수호가
			'bidho1' : 'float',
			# 체결량
			'cvolume' : 'long',
			# 델타
			'delt' : 'float',
			# 감마
			'gama' : 'float',
			# 베가
			'vega' : 'float',
			# 쎄타
			'ceta' : 'float',
			# 로우
			'rhox' : 'float',
			# 이론가
			'theoryprice' : 'float',
			# 내재가치
			'impv' : 'float',
			# 시간가치
			'timevl' : 'float',
			# 잔고수량
			'jvolume' : 'long',
			# 평가손익
			'parpl' : 'long',
			# 청산가능수량
			'jngo' : 'long',
			# 매도잔량
			'offerrem1' : 'long',
			# 매수잔량
			'bidrem1' : 'long',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# ATM구분
			'atmgubun' : 'char',
			# 지수환산
			'jisuconv' : 'float',
			# 거래대금
			'value' : 'float'
		}
	]
}

# 선물옵션호가잔량비율챠트(t2405)
db_outblock_query_t2405 = {
	't2405OutBlock' : {
		# 매도체결수량
		'mdvolume' : 'double',
		# 매도체결건수
		'mdchecnt' : 'long',
		# 매수체결수량
		'msvolume' : 'double',
		# 매수체결건수
		'mschecnt' : 'long',
		# 시간CTS
		'cts_time' : 'char'
	},
	't2405OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 누적거래량
			'volume' : 'double',
			# 체결수량
			'cvolume' : 'long',
			# 매도1호가
			'offerho1' : 'float',
			# 매수1호가
			'bidho1' : 'float',
			# 매도수량
			'offerrem' : 'long',
			# 매수수량
			'bidrem' : 'long',
			# 매도건수
			'offercnt' : 'long',
			# 매수건수
			'bidcnt' : 'long',
			# 매도증감수량
			'c_offerrem' : 'long',
			# 매수증감수량
			'c_bidrem' : 'long',
			# 매도증감건수
			'c_offercnt' : 'long',
			# 매수증감건수
			'c_bidcnt' : 'long',
			# 매수수량비율
			'r_bidrem' : 'float',
			# 매수건수비율
			'r_bidcnt' : 'float',
			# 매수비율구분
			'r_sign' : 'char',
			# 일자
			'date' : 'date'
		}
	]
}

# 미결제약정추이(t2421)
db_outblock_query_t2421 = {
	't2421OutBlock' : {
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'diff' : 'float',
		# 체결수량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'double',
		# 미결제수량
		'openyak' : 'long'
	},
	't2421OutBlock1' : [
		{
			# 일자시간
			'dt' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 미결제시량
			'openopenyak' : 'long',
			# 미결제고량
			'highopenyak' : 'long',
			# 미결제저량
			'lowopenyak' : 'long',
			# 미결제종량
			'closeopenyak' : 'long',
			# 미결증감
			'openupdn' : 'long'
		}
	]
}

# 상품선물투자자매매동향(실시간)(t2541)
db_outblock_query_t2541 = {
	't2541OutBlock' : {
		# 상품ID
		'eitem' : 'char',
		# 시장구분
		'sgubun' : 'char',
		# CTSTIME
		'cts_time' : 'char',
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 국가투자자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 사모펀드코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't2541OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# 개인순매수
			'sv_08' : 'long',
			# 외국인순매수
			'sv_17' : 'long',
			# 기관계순매수
			'sv_18' : 'long',
			# 증권순매수
			'sv_01' : 'long',
			# 투신순매수
			'sv_03' : 'long',
			# 은행순매수
			'sv_04' : 'long',
			# 보험순매수
			'sv_02' : 'long',
			# 종금순매수
			'sv_05' : 'long',
			# 기금순매수
			'sv_06' : 'long',
			# 기타순매수
			'sv_07' : 'long',
			# 국가순매수
			'sv_11' : 'long',
			# 사모펀드순매수
			'sv_00' : 'long'
		}
	]
}

# 상품선물투자자매매동향(챠트용)
db_outblock_query_t2545 = {
	't2545OutBlock' : {
		# 상품ID
		'eitem' : 'char',
		# 시장구분
		'sgubun' : 'char',
		# 개인투자자코드
		'indcode' : 'char',
		# 외국인투자자코드
		'forcode' : 'char',
		# 기관계투자자코드
		'syscode' : 'char',
		# 증권투자자코드
		'stocode' : 'char',
		# 투신투자자코드
		'invcode' : 'char',
		# 은행투자자코드
		'bancode' : 'char',
		# 보험투자자코드
		'inscode' : 'char',
		# 종금투자자코드
		'fincode' : 'char',
		# 기금투자자코드
		'moncode' : 'char',
		# 기타투자자코드
		'etccode' : 'char',
		# 국가투자자코드
		'natcode' : 'char',
		# 사모펀드투자자코드
		'pefcode' : 'char',
		# 기준지수코드
		'jisucd' : 'char',
		# 기준지수명
		'jisunm' : 'char'
	},
	't2545OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 일자시간
			'datetime' : 'char',
			# 개인순매수거래량
			'indmsvol' : 'long',
			# 개인순매수거래대금
			'indmsamt' : 'double',
			# 외국인순매수거래량
			'formsvol' : 'long',
			# 외국인순매수거래대금
			'formsamt' : 'double',
			# 기관계순매수거래량
			'sysmsvol' : 'long',
			# 기관계순매수거래대금
			'sysmsamt' : 'double',
			# 증권순매수거래량
			'stomsvol' : 'long',
			# 증권순매수거래대금
			'stomsamt' : 'double',
			# 투신순매수거래량
			'invmsvol' : 'long',
			# 투신순매수거래대금
			'invmsamt' : 'double',
			# 은행순매수거래량
			'banmsvol' : 'long',
			# 은행순매수거래대금
			'banmsamt' : 'double',
			# 보험순매수거래량
			'insmsvol' : 'long',
			# 보험순매수거래대금
			'insmsamt' : 'double',
			# 종금순매수거래량
			'finmsvol' : 'long',
			# 종금순매수거래대금
			'finmsamt' : 'double',
			# 기금순매수거래량
			'monmsvol' : 'long',
			# 기금순매수거래대금
			'monmsamt' : 'double',
			# 기타순매수거래량
			'etcmsvol' : 'long',
			# 기타순매수거래대금
			'etcmsamt' : 'double',
			# 국가순매수거래량
			'natmsvol' : 'long',
			# 국가순매수거래대금
			'natmsamt' : 'double',
			# 사모펀드순매수거래량
			'pefmsvol' : 'long',
			# 사모펀드순매수거래대금
			'pefmsamt' : 'double',
			# 기준지수
			'upclose' : 'float',
			# 기준체결거래량
			'upcvolume' : 'long',
			# 기준누적거래량
			'upvolume' : 'double',
			# 기준거래대금
			'upvalue' : 'double'
		}
	]
}

# CME야간선물현재가조회(t2801)
db_outblock_query_t2801 = {
	't2801OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 전일종가
		'jnilclose' : 'float',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래대금
		'value' : 'long',
		# 미결제량
		'mgjv' : 'long',
		# 미결제증감
		'mgjvdiff' : 'long',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 상한가
		'uplmtprice' : 'float',
		# 하한가
		'dnlmtprice' : 'float',
		# 52최고가
		'high52w' : 'float',
		# 52최저가
		'low52w' : 'float',
		# 베이시스
		'basis' : 'float',
		# 기준가
		'recprice' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 괴리율
		'glyl' : 'float',
		# CB상한가
		'cbhprice' : 'float',
		# CB하한가
		'cblprice' : 'float',
		# 만기일
		'lastmonth' : 'char',
		# 잔여일
		'jandatecnt' : 'long',
		# 종합지수
		'pricejisu' : 'float',
		# 종합지수전일대비구분
		'jisusign' : 'char',
		# 종합지수전일대비
		'jisuchange' : 'float',
		# 종합지수등락율
		'jisudiff' : 'float',
		# KOSPI200지수
		'kospijisu' : 'float',
		# KOSPI200전일대비구분
		'kospisign' : 'char',
		# KOSPI200전일대비
		'kospichange' : 'float',
		# KOSPI200등락율
		'kospidiff' : 'float',
		# 상장최고가
		'listhprice' : 'float',
		# 상장최저가
		'listlprice' : 'float',
		# 시장BASIS
		'sbasis' : 'float',
		# 이론BASIS
		'ibasis' : 'float',
		# 전일거래량
		'jnilvolume' : 'long',
		# 전일거래대금
		'jnilvalue' : 'long'
	}
}

# CME야간선물호가조회(t2802)
db_outblock_query_t2802 = {
	't2802OutBlock' : {
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래량전일동시간비율
		'stimeqrt' : 'float',
		# 전일종가
		'jnilclose' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'dcnt1' : 'long',
		# 매수호가건수1
		'scnt1' : 'long',
		# 매도호가2
		'offerho2' : 'float',
		# 매수호가2
		'bidho2' : 'float',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'dcnt2' : 'long',
		# 매수호가건수2
		'scnt2' : 'long',
		# 매도호가3
		'offerho3' : 'float',
		# 매수호가3
		'bidho3' : 'float',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'dcnt3' : 'long',
		# 매수호가건수3
		'scnt3' : 'long',
		# 매도호가4
		'offerho4' : 'float',
		# 매수호가4
		'bidho4' : 'float',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'dcnt4' : 'long',
		# 매수호가건수4
		'scnt4' : 'long',
		# 매도호가5
		'offerho5' : 'float',
		# 매수호가5
		'bidho5' : 'float',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'dcnt5' : 'long',
		# 매수호가건수5
		'scnt5' : 'long',
		# 매도호가총수량
		'dvol' : 'long',
		# 매수호가총수량
		'svol' : 'long',
		# 총매도호가건수
		'toffernum' : 'long',
		# 총매수호가건수
		'tbidnum' : 'long',
		# 수신시간
		'time' : 'char',
		# 단축코드
		'shcode' : 'char'
	}
}

# CME야간선물시간대별체결조회(t2804)
db_outblock_query_t2804 = {
	't2804OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't2804OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 시간24
			'chetime24' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 매도호가
			'offerho' : 'float',
			# 매수호가
			'bidho' : 'float',
			# 거래량
			'volume' : 'double',
			# 미결수량
			'openyak' : 'long',
			# 미결전일증감
			'jnilopenupdn' : 'long',
			# 이론BASIS
			'ibasis' : 'float',
			# 시장BASIS
			'sbasis' : 'float',
			# 괴리율
			'kasis' : 'float',
			# 거래대금
			'value' : 'double',
			# 미결직전증감
			'j_openupdn' : 'long',
			# 누적매수체결량
			'n_msvolume' : 'double',
			# 누적매도체결량
			'n_mdvolume' : 'double',
			# 누적순매수체결량
			's_msvolume' : 'double',
			# 누적매수체결건수
			'n_mschecnt' : 'long',
			# 누적매도체결건수
			'n_mdchecnt' : 'long',
			# 누적순매수체결건수
			's_mschecnt' : 'long'
		}
	]
}

# CME야간선물기간별주가(t2805)
db_outblock_query_t2805 = {
	't2805OutBlock' : {
		# 날짜
		'date' : 'char',
		# CTS종목코드
		'cts_code' : 'char',
		# 전종목만기일
		'lastdate' : 'char',
		# 최근월선물여부
		'nowfutyn' : 'char'
	},
	't2805OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openyakupdn' : 'long',
			# 거래대금
			'value' : 'float'
		}
	]
}

# CME야간선물시간대별투자자매매추이(t2813)
db_outblock_query_t2813 = {
	't2813OutBlock' : {
		# CTSTIME
		'cts_time' : 'char',
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 국가투자자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 사모펀드코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't2813OutBlock1' : [
		{
			# 시간
			'time' : 'char',
			# 개인순매수
			'sv_08' : 'long',
			# 외국인순매수
			'sv_17' : 'long',
			# 기관계순매수
			'sv_18' : 'long',
			# 증권순매수
			'sv_01' : 'long',
			# 투신순매수
			'sv_03' : 'long',
			# 은행순매수
			'sv_04' : 'long',
			# 보험순매수
			'sv_02' : 'long',
			# 종금순매수
			'sv_05' : 'long',
			# 기금순매수
			'sv_06' : 'long',
			# 기타순매수
			'sv_07' : 'long',
			# 국가순매수
			'sv_11' : 'long',
			# 사모펀드순매수
			'sv_00' : 'long'
		}
	]
}

# CME야간선물기간별투자자매매추이(챠트)
db_outblock_query_t2814 = {
	't2814OutBlock' : {
		# 시장코드
		'mcode' : 'char',
		# 시장명
		'mname' : 'char'
	},
	't2814OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 개인수량
			'sv_08' : 'long',
			# 외인계수량(등록+미등록)
			'sv_17' : 'long',
			# 기관계수량
			'sv_18' : 'long',
			# 증권수량
			'sv_01' : 'long',
			# 투신수량
			'sv_03' : 'long',
			# 은행수량
			'sv_04' : 'long',
			# 보험수량
			'sv_02' : 'long',
			# 종금수량
			'sv_05' : 'long',
			# 기금수량
			'sv_06' : 'long',
			# 기타수량
			'sv_07' : 'long',
			# 사모펀드수량
			'sv_00' : 'long',
			# 등록외국인수량
			'sv_09' : 'long',
			# 미등록외국인수량
			'sv_10' : 'long',
			# 국가수량
			'sv_11' : 'long',
			# 기타계수량(기타+국가)
			'sv_99' : 'long',
			# 개인금액
			'sa_08' : 'double',
			# 외인계금액(등록+미등록)
			'sa_17' : 'double',
			# 기관계금액
			'sa_18' : 'double',
			# 증권금액
			'sa_01' : 'double',
			# 투신금액
			'sa_03' : 'double',
			# 은행금액
			'sa_04' : 'double',
			# 보험금액
			'sa_02' : 'double',
			# 종금금액
			'sa_05' : 'double',
			# 기금금액
			'sa_06' : 'double',
			# 기타금액
			'sa_07' : 'double',
			# 사모펀드금액
			'sa_00' : 'double',
			# 등록외국인금액
			'sa_09' : 'double',
			# 미등록외국인금액
			'sa_10' : 'double',
			# 국가금액
			'sa_11' : 'double',
			# 기타계금액(기타+국가)
			'sa_99' : 'double',
			# 시장지수
			'jisu' : 'float'
		}
	]
}

# CME야간선물투자자별종합(t2816)
db_outblock_query_t2816 = {
	't2816OutBlock1' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	},
	't2816OutBlock2' : {
		# 개인투자자코드
		'tjjcode_08' : 'char',
		# 개인매수
		'ms_08' : 'long',
		# 개인매도
		'md_08' : 'long',
		# 개인증감
		'rate_08' : 'long',
		# 개인순매수
		'svolume_08' : 'long',
		# 외국인투자자코드
		'jjcode_17' : 'char',
		# 외국인매수
		'ms_17' : 'long',
		# 외국인매도
		'md_17' : 'long',
		# 외국인증감
		'rate_17' : 'long',
		# 외국인순매수
		'svolume_17' : 'long',
		# 기관계투자자코드
		'jjcode_18' : 'char',
		# 기관계매수
		'ms_18' : 'long',
		# 기관계매도
		'md_18' : 'long',
		# 기관계증감
		'rate_18' : 'long',
		# 기관계순매수
		'svolume_18' : 'long',
		# 증권투자자코드
		'jjcode_01' : 'char',
		# 증권매수
		'ms_01' : 'long',
		# 증권매도
		'md_01' : 'long',
		# 증권증감
		'rate_01' : 'long',
		# 증권순매수
		'svolume_01' : 'long',
		# 투신투자자코드
		'jjcode_03' : 'char',
		# 투신매수
		'ms_03' : 'long',
		# 투신매도
		'md_03' : 'long',
		# 투신증감
		'rate_03' : 'long',
		# 투신순매수
		'svolume_03' : 'long',
		# 은행투자자코드
		'jjcode_04' : 'char',
		# 은행매수
		'ms_04' : 'long',
		# 은행매도
		'md_04' : 'long',
		# 은행증감
		'rate_04' : 'long',
		# 은행순매수
		'svolume_04' : 'long',
		# 보험투자자코드
		'jjcode_02' : 'char',
		# 보험매수
		'ms_02' : 'long',
		# 보험매도
		'md_02' : 'long',
		# 보험증감
		'rate_02' : 'long',
		# 보험순매수
		'svolume_02' : 'long',
		# 종금투자자코드
		'jjcode_05' : 'char',
		# 종금매수
		'ms_05' : 'long',
		# 종금매도
		'md_05' : 'long',
		# 종금증감
		'rate_05' : 'long',
		# 종금순매수
		'svolume_05' : 'long',
		# 기금투자자코드
		'jjcode_06' : 'char',
		# 기금매수
		'ms_06' : 'long',
		# 기금매도
		'md_06' : 'long',
		# 기금증감
		'rate_06' : 'long',
		# 기금순매수
		'svolume_06' : 'long',
		# 국가투자코드
		'jjcode_11' : 'char',
		# 국가매수
		'ms_11' : 'long',
		# 국가매도
		'md_11' : 'long',
		# 국가증감
		'rate_11' : 'long',
		# 국가순매수
		'svolume_11' : 'long',
		# 기타투자자코드
		'jjcode_07' : 'char',
		# 기타매수
		'ms_07' : 'long',
		# 기타매도
		'md_07' : 'long',
		# 기타증감
		'rate_07' : 'long',
		# 기타순매수
		'svolume_07' : 'long',
		# 사모펀드투자자코드
		'jjcode_00' : 'char',
		# 사모펀드매수
		'ms_00' : 'long',
		# 사모펀드매도
		'md_00' : 'long',
		# 사모펀드증감
		'rate_00' : 'long',
		# 사모펀드순매수
		'svolume_00' : 'long'
	}
}

# EUREXKOSPI200옵션선물현재가(시세)조회(t2830)
db_outblock_query_t2830 = {
	't2830OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 전일종가
		'jnilclose' : 'float',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래대금
		'value' : 'long',
		# 시가
		'open' : 'float',
		# 고가
		'high' : 'float',
		# 저가
		'low' : 'float',
		# 기준가
		'recprice' : 'float',
		# 이론가
		'theoryprice' : 'float',
		# 행사가
		'actprice' : 'float',
		# 내재가치
		'impv' : 'float',
		# 시간가치
		'timevl' : 'float',
		# KOSPI200지수
		'kospijisu' : 'float',
		# KOSPI200전일대비구분
		'kospisign' : 'char',
		# KOSPI200전일대비
		'kospichange' : 'float',
		# KOSPI200등락율
		'kospidiff' : 'float',
		# CME야간선물현재가
		'cmeprice' : 'float',
		# CME야간선물전일대비구분
		'cmesign' : 'char',
		# CME야간선물전일대비
		'cmechange' : 'float',
		# CME야간선물등락율
		'cmediff' : 'float',
		# CME야간선물종목코드
		'cmefocode' : 'char',
		# 정규장상한가
		'uplmtprice' : 'float',
		# 정규장하한가
		'dnlmtprice' : 'float',
		# 단축코드
		'focode' : 'char',
		# 예상체결가
		'yeprice' : 'float',
		# 전일대비구분
		'ysign' : 'char',
		# 전일대비
		'ychange' : 'float',
		# 등락율
		'ydiff' : 'float',
		# 단일가호가여부
		'danhochk' : 'char'
	}
}

# EUREXKOSPI200옵션선물호가조회(t2831)
db_outblock_query_t2831 = {
	't2831OutBlock' : {
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 전일종가
		'jnilclose' : 'float',
		# 매도호가1
		'offerho1' : 'float',
		# 매수호가1
		'bidho1' : 'float',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'dcnt1' : 'long',
		# 매수호가건수1
		'scnt1' : 'long',
		# 매도호가2
		'offerho2' : 'float',
		# 매수호가2
		'bidho2' : 'float',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'dcnt2' : 'long',
		# 매수호가건수2
		'scnt2' : 'long',
		# 매도호가3
		'offerho3' : 'float',
		# 매수호가3
		'bidho3' : 'float',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'dcnt3' : 'long',
		# 매수호가건수3
		'scnt3' : 'long',
		# 매도호가4
		'offerho4' : 'float',
		# 매수호가4
		'bidho4' : 'float',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'dcnt4' : 'long',
		# 매수호가건수4
		'scnt4' : 'long',
		# 매도호가5
		'offerho5' : 'float',
		# 매수호가5
		'bidho5' : 'float',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'dcnt5' : 'long',
		# 매수호가건수5
		'scnt5' : 'long',
		# 매도호가총수량
		'dvol' : 'long',
		# 매수호가총수량
		'svol' : 'long',
		# 총매도호가건수
		'toffernum' : 'long',
		# 총매수호가건수
		'tbidnum' : 'long',
		# 수신시간
		'time' : 'char',
		# 단축코드
		'shcode' : 'char'
	}
}

# EUREX야간옵션선물시간대별체결조회(t2832)
db_outblock_query_t2832 = {
	't2832OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't2832OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 매도호가
			'offerho' : 'float',
			# 매수호가
			'bidho' : 'float',
			# 거래량
			'volume' : 'double',
			# 누적매수체결량
			'n_msvolume' : 'double',
			# 누적매도체결량
			'n_mdvolume' : 'double',
			# 누적순매수체결량
			's_msvolume' : 'double',
			# 누적매수체결건수
			'n_mschecnt' : 'long',
			# 누적매도체결건수
			'n_mdchecnt' : 'long',
			# 누적순매수체결건수
			's_mschecnt' : 'long'
		}
	]
}

# EUREX야간옵션선물기간별추이(t2833)
db_outblock_query_t2833 = {
	't2833OutBlock' : {
		# 날짜
		'date' : 'char',
		# CTS종목코드
		'cts_code' : 'char',
		# 전종목만기일
		'lastdate' : 'char',
		# 최근월선물여부
		'nowfutyn' : 'char'
	},
	't2833OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float'
		}
	]
}

# EUREX옵션선물시세전광판(t2835)
db_outblock_query_t2835 = {
	't2835OutBlock' : {
		# 근월물현재가
		'gmprice' : 'float',
		# 근월물전일대비구분
		'gmsign' : 'char',
		# 근월물전일대비
		'gmchange' : 'float',
		# 근월물등락율
		'gmdiff' : 'float',
		# 근월물거래량
		'gmvolume' : 'long',
		# 근월물선물코드
		'gmshcode' : 'char'
	},
	't2835OutBlock1' : [
		{
			# 행사가
			'actprice' : 'float',
			# 콜옵션코드
			'optcode' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도호가
			'offerho1' : 'float',
			# 매수호가
			'bidho1' : 'float',
			# 체결량
			'cvolume' : 'long',
			# 내재가치
			'impv' : 'float',
			# 시간가치
			'timevl' : 'float',
			# 매도잔량
			'offerrem1' : 'long',
			# 매수잔량
			'bidrem1' : 'long',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# ATM구분
			'atmgubun' : 'char',
			# 지수환산
			'jisuconv' : 'float'
		}
	],
	't2835OutBlock2' : [
		{
			# 행사가
			'actprice' : 'float',
			# 풋옵션코드
			'optcode' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 매도호가
			'offerho1' : 'float',
			# 매수호가
			'bidho1' : 'float',
			# 체결량
			'cvolume' : 'long',
			# 내재가치
			'impv' : 'float',
			# 시간가치
			'timevl' : 'float',
			# 매도잔량
			'offerrem1' : 'long',
			# 매수잔량
			'bidrem1' : 'long',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# ATM구분
			'atmgubun' : 'char',
			# 지수환산
			'jisuconv' : 'float'
		}
	]
}

# 뉴스본문(t3102)
db_outblock_query_t3102 = {
	't3102OutBlock' : [
		{
			# 뉴스종목
			'sJongcode' : 'char'
		}
	],
	't3102OutBlock1' : [
		{
			# 뉴스본문
			'sBody' : 'char'
		}
	],
	't3102OutBlock2' : {
		# 뉴스타이틀
		'sTitle' : 'char'
	}
}

# 종목별증시일정(t3202)
db_outblock_query_t3202 = {
	't3202OutBlock' : [
		{
			# 기준일
			'recdt' : 'char',
			# 테이블아이디
			'tableid' : 'char',
			# 업무구분
			'upgu' : 'char',
			# 발행체번호
			'custno' : 'char',
			# 발행회사명
			'custnm' : 'char',
			# 종목코드
			'shcode' : 'char',
			# 업무명
			'upunm' : 'char'
		}
	]
}

# FNG_요약(t3320)
db_outblock_query_t3320 = {
	't3320OutBlock' : {
		# 업종구분명
		'upgubunnm' : 'char',
		# 시장구분
		'sijangcd' : 'char',
		# 시장구분명
		'marketnm' : 'char',
		# 한글기업명
		'company' : 'char',
		# 본사주소
		'baddress' : 'char',
		# 본사전화번호
		'btelno' : 'char',
		# 최근결산년도
		'gsyyyy' : 'char',
		# 결산월
		'gsmm' : 'char',
		# 최근결산년월
		'gsym' : 'char',
		# 주당액면가
		'lstprice' : 'long',
		# 주식수
		'gstock' : 'long',
		# Homepage
		'homeurl' : 'char',
		# 그룹명
		'grdnm' : 'char',
		# 외국인
		'foreignratio' : 'float',
		# 주담전화
		'irtel' : 'char',
		# 자본금
		'capital' : 'float',
		# 시가총액
		'sigavalue' : 'float',
		# 배당금
		'cashsis' : 'float',
		# 배당수익율
		'cashrate' : 'float',
		# 현재가
		'price' : 'long',
		# 전일종가
		'jnilclose' : 'long'
	},
	't3320OutBlock1' : {
		# 기업코드
		'gicode' : 'char',
		# 결산년월
		'gsym' : 'char',
		# 결산구분
		'gsgb' : 'char',
		# PER
		'per' : 'float',
		# EPS
		'eps' : 'float',
		# PBR
		'pbr' : 'float',
		# ROA
		'roa' : 'float',
		# ROE
		'roe' : 'float',
		# EBITDA
		'ebitda' : 'float',
		# EVEBITDA
		'evebitda' : 'float',
		# 액면가
		'par' : 'float',
		# SPS
		'sps' : 'float',
		# CPS
		'cps' : 'float',
		# BPS
		'bps' : 'float',
		# T.PER
		't_per' : 'float',
		# T.EPS
		't_eps' : 'float',
		# PEG
		'peg' : 'float',
		# T.PEG
		't_peg' : 'float',
		# 최근분기년도
		't_gsym' : 'char'
	}
}

# 재무순위종합(t3341)
db_outblock_query_t3341 = {
	't3341OutBlock' : {
		# CNT
		'cnt' : 'long',
		# IDX
		'idx' : 'long'
	},
	't3341OutBlock1' : [
		{
			# 순위
			'rank' : 'long',
			# 기업명
			'hname' : 'char',
			# 매출액증가율
			'salesgrowth' : 'long',
			# 영업이익증가율
			'operatingincomegrowt' : 'long',
			# 경상이익증가율
			'ordinaryincomegrowth' : 'long',
			# 부채비율
			'liabilitytoequity' : 'long',
			# 유보율
			'enterpriseratio' : 'long',
			# EPS
			'eps' : 'long',
			# BPS
			'bps' : 'long',
			# ROE
			'roe' : 'long',
			# 종목코드
			'shcode' : 'char',
			# PER
			'per' : 'float',
			# PBR
			'pbr' : 'float',
			# PEG
			'peg' : 'float'
		}
	]
}

# 투자의견(t3401)
db_outblock_query_t3401 = {
	't3401OutBlock' : {
		# IDXDATE
		'cts_date' : 'char',
		# 현재가
		'price' : 'long',
		# 대비속성
		'sign' : 'char',
		# 대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래대금
		'value' : 'long'
	},
	't3401OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 회원사코드
			'tradno' : 'char',
			# 의견일자
			'date' : 'char',
			# 회원사명
			'tradname' : 'char',
			# 투자의견변경후
			'bopn' : 'char',
			# 투자의견변경전
			'nopn' : 'char',
			# 목표가변경전
			'boga' : 'long',
			# 목표가변경후
			'noga' : 'long',
			# 의견일종가
			'close' : 'long'
		}
	]
}

# 해외실시간지수(t3518)
db_outblock_query_t3518 = {
	't3518OutBlock' : {
		# CTS_DATE
		'cts_date' : 'char',
		# CTS_TIME
		'cts_time' : 'char'
	},
	't3518OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'double',
			# 고가
			'high' : 'double',
			# 저가
			'low' : 'double',
			# 현재가
			'price' : 'double',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'double',
			# 등락율
			'uprate' : 'double',
			# 누적거래량
			'volume' : 'double',
			# 매수호가
			'bidho' : 'double',
			# 매도호가
			'offerho' : 'double',
			# 매수잔량
			'bidrem' : 'double',
			# 매도잔량
			'offerrem' : 'double',
			# 종목종류
			'kind' : 'char',
			# SYMBOL
			'symbol' : 'char',
			# EXID
			'exid' : 'char',
			# 한국일자
			'kodate' : 'char',
			# 한국시간
			'kotime' : 'char'
		}
	]
}

# 해외지수조회(API용)(t3521)
db_outblock_query_t3521 = {
	't3521OutBlock' : {
		# 심벌
		'symbol' : 'char',
		# 지수명
		'hname' : 'char',
		# 지수
		'close' : 'float',
		# 대비구분
		'sign' : 'char',
		# 대비
		'change' : 'float',
		# 등락율
		'diff' : 'float',
		# 일자
		'date' : 'char'
	}
}

# 주식챠트(종합)(t4201)
db_outblock_query_t4201 = {
	't4201OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'long',
		# 전일고가
		'jihigh' : 'long',
		# 전일저가
		'jilow' : 'long',
		# 전일종가
		'jiclose' : 'long',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'long',
		# 당일고가
		'dihigh' : 'long',
		# 당일저가
		'dilow' : 'long',
		# 당일종가
		'diclose' : 'long',
		# 상한가
		'highend' : 'long',
		# 하한가
		'lowend' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 연속당일구분
		'cts_daygb' : 'char'
	},
	't4201OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long',
			# 수정구분
			'jongchk' : 'long',
			# 수정비율
			'rate' : 'double',
			# 수정주가반영항목
			'pricechk' : 'long',
			# 수정비율반영거래대금
			'ratevalue' : 'long'
		}
	]
}

# 업종챠트(종합)(t4203)
db_outblock_query_t4203 = {
	't4203OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 당일거래대금
		'disvalue' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 연속당일구분
		'cts_daygb' : 'char'
	},
	't4203OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long'
		}
	]
}

# 주식선물마스터조회(API용)(t8401)
db_outblock_query_t8401 = {
	't8401OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char'
		}
	]
}

# 주식선물현재가조회(API용)(t8402)
db_outblock_query_t8402 = {
	't8402OutBlock' : {
		# 한글명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 전일종가
		'jnilclose' : 'long',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래량전일동시간비율
		'stimeqrt' : 'double',
		# 거래대금
		'value' : 'long',
		# 미결제량
		'mgjv' : 'long',
		# 미결제증감
		'mgjvdiff' : 'long',
		# 시가
		'open' : 'long',
		# 고가
		'high' : 'long',
		# 저가
		'low' : 'long',
		# 상한가
		'uplmtprice' : 'long',
		# 하한가
		'dnlmtprice' : 'long',
		# 52최고가
		'high52w' : 'long',
		# 52최저가
		'low52w' : 'long',
		# 베이시스
		'basis' : 'float',
		# 기준가
		'recprice' : 'long',
		# 이론가
		'theoryprice' : 'long',
		# 괴리율
		'glyl' : 'float',
		# 만기일
		'lastmonth' : 'char',
		# 잔여일
		'jandatecnt' : 'long',
		# 종합지수
		'pricejisu' : 'float',
		# 종합지수전일대비구분
		'jisusign' : 'char',
		# 종합지수전일대비
		'jisuchange' : 'float',
		# 종합지수등락율
		'jisudiff' : 'float',
		# KOSPI200지수
		'kospijisu' : 'float',
		# KOSPI200전일대비구분
		'kospisign' : 'char',
		# KOSPI200전일대비
		'kospichange' : 'float',
		# KOSPI200등락율
		'kospidiff' : 'float',
		# 상장최고가
		'listhprice' : 'long',
		# 상장최저가
		'listlprice' : 'long',
		# 델타
		'delt' : 'float',
		# 감마
		'gama' : 'float',
		# 세타
		'ceta' : 'float',
		# 베가
		'vega' : 'float',
		# 로우
		'rhox' : 'float',
		# 근월물현재가
		'gmprice' : 'long',
		# 근월물전일대비구분
		'gmsign' : 'char',
		# 근월물전일대비
		'gmchange' : 'long',
		# 근월물등락율
		'gmdiff' : 'float',
		# 이론가
		'theorypriceg' : 'long',
		# 역사적변동성
		'histimpv' : 'float',
		# 내재변동성
		'impv' : 'float',
		# 시장BASIS
		'sbasis' : 'long',
		# 이론BASIS
		'ibasis' : 'long',
		# 근월물종목코드
		'gmfutcode' : 'char',
		# 행사가
		'actprice' : 'long',
		# 기초자산단축코드
		'shcode' : 'char',
		# 기초자산한글명
		'basehname' : 'char',
		# 기초자산현재가
		'baseprice' : 'long',
		# 기초자산현재가대비구분
		'basesign' : 'char',
		# 기초자산현재가전일대비
		'basechange' : 'long',
		# 기초자산등락률
		'basediff' : 'float',
		# 기초자산거래량
		'basevol' : 'long',
		# 기초자산전일거래량
		'baseprevol' : 'long',
		# 기초자산매수호가
		'basebidprc' : 'long',
		# 기초자산매도호가
		'baseaskprc' : 'long',
		# 기초자산외국계회원사순매수
		'basefornetbid' : 'long',
		# 상품군
		'prodgrp' : 'char',
		# 승수
		'mulcnt' : 'float',
		# 단일가호가여부
		'danhochk' : 'char',
		# 예상체결가
		'yeprice' : 'long',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilychange' : 'long',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float'
	}
}

# 주식선물호가조회(API용)(t8403)
db_outblock_query_t8403 = {
	't8403OutBlock' : {
		# 종목명
		'hname' : 'char',
		# 현재가
		'price' : 'long',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'long',
		# 등락율
		'diff' : 'float',
		# 거래량
		'volume' : 'long',
		# 거래량전일동시간비율
		'stimeqrt' : 'float',
		# 전일종가
		'jnilclose' : 'long',
		# 매도호가1
		'offerho1' : 'long',
		# 매수호가1
		'bidho1' : 'long',
		# 매도호가수량1
		'offerrem1' : 'long',
		# 매수호가수량1
		'bidrem1' : 'long',
		# 매도호가건수1
		'dcnt1' : 'long',
		# 매수호가건수1
		'scnt1' : 'long',
		# 매도호가2
		'offerho2' : 'long',
		# 매수호가2
		'bidho2' : 'long',
		# 매도호가수량2
		'offerrem2' : 'long',
		# 매수호가수량2
		'bidrem2' : 'long',
		# 매도호가건수2
		'dcnt2' : 'long',
		# 매수호가건수2
		'scnt2' : 'long',
		# 매도호가3
		'offerho3' : 'long',
		# 매수호가3
		'bidho3' : 'long',
		# 매도호가수량3
		'offerrem3' : 'long',
		# 매수호가수량3
		'bidrem3' : 'long',
		# 매도호가건수3
		'dcnt3' : 'long',
		# 매수호가건수3
		'scnt3' : 'long',
		# 매도호가4
		'offerho4' : 'long',
		# 매수호가4
		'bidho4' : 'long',
		# 매도호가수량4
		'offerrem4' : 'long',
		# 매수호가수량4
		'bidrem4' : 'long',
		# 매도호가건수4
		'dcnt4' : 'long',
		# 매수호가건수4
		'scnt4' : 'long',
		# 매도호가5
		'offerho5' : 'long',
		# 매수호가5
		'bidho5' : 'long',
		# 매도호가수량5
		'offerrem5' : 'long',
		# 매수호가수량5
		'bidrem5' : 'long',
		# 매도호가건수5
		'dcnt5' : 'long',
		# 매수호가건수5
		'scnt5' : 'long',
		# 매도호가6
		'offerho6' : 'long',
		# 매수호가6
		'bidho6' : 'long',
		# 매도호가수량6
		'offerrem6' : 'long',
		# 매수호가수량6
		'bidrem6' : 'long',
		# 매도호가건수6
		'dcnt6' : 'long',
		# 매수호가건수6
		'scnt6' : 'long',
		# 매도호가7
		'offerho7' : 'long',
		# 매수호가7
		'bidho7' : 'long',
		# 매도호가수량7
		'offerrem7' : 'long',
		# 매수호가수량7
		'bidrem7' : 'long',
		# 매도호가건수7
		'dcnt7' : 'long',
		# 매수호가건수7
		'scnt7' : 'long',
		# 매도호가8
		'offerho8' : 'long',
		# 매수호가8
		'bidho8' : 'long',
		# 매도호가수량8
		'offerrem8' : 'long',
		# 매수호가수량8
		'bidrem8' : 'long',
		# 매도호가건수8
		'dcnt8' : 'long',
		# 매수호가건수8
		'scnt8' : 'long',
		# 매도호가9
		'offerho9' : 'long',
		# 매수호가9
		'bidho9' : 'long',
		# 매도호가수량9
		'offerrem9' : 'long',
		# 매수호가수량9
		'bidrem9' : 'long',
		# 매도호가건수9
		'dcnt9' : 'long',
		# 매수호가건수9
		'scnt9' : 'long',
		# 매도호가10
		'offerho10' : 'long',
		# 매수호가10
		'bidho10' : 'long',
		# 매도호가수량10
		'offerrem10' : 'long',
		# 매수호가수량10
		'bidrem10' : 'long',
		# 매도호가건수10
		'dcnt10' : 'long',
		# 매수호가건수10
		'scnt10' : 'long',
		# 매도호가총수량
		'dvol' : 'long',
		# 매수호가총수량
		'svol' : 'long',
		# 총매도호가건수
		'toffernum' : 'long',
		# 총매수호가건수
		'tbidnum' : 'long',
		# 수신시간
		'time' : 'char',
		# 단축코드
		'shcode' : 'char'
	}
}

# 주식선물시간대별체결조회(API용)(t8404)
db_outblock_query_t8404 = {
	't8404OutBlock' : {
		# 시간CTS
		'cts_time' : 'char'
	},
	't8404OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 매도호가
			'offerho' : 'long',
			# 매수호가
			'bidho' : 'long',
			# 거래량
			'volume' : 'double',
			# 미결수량
			'openyak' : 'long',
			# 미결전일증감
			'jnilopenupdn' : 'long',
			# 이론BASIS
			'ibasis' : 'long',
			# 시장BASIS
			'sbasis' : 'long',
			# 괴리율
			'kasis' : 'float',
			# 거래대금
			'value' : 'double',
			# 미결직전증감
			'j_openupdn' : 'long',
			# 누적매수체결량
			'n_msvolume' : 'double',
			# 누적매도체결량
			'n_mdvolume' : 'double',
			# 누적순매수체결량
			's_msvolume' : 'double',
			# 누적매수체결건수
			'n_mschecnt' : 'long',
			# 누적매도체결건수
			'n_mdchecnt' : 'long',
			# 누적순매수체결건수
			's_mschecnt' : 'long'
		}
	]
}

# 주식선물기간별주가(API용)(t8405)
db_outblock_query_t8405 = {
	't8405OutBlock' : {
		# 날짜
		'date' : 'char',
		# CTS종목코드
		'cts_code' : 'char',
		# 전종목만기일
		'lastdate' : 'char',
		# 최근월선물여부
		'nowfutyn' : 'char'
	},
	't8405OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openyakupdn' : 'long',
			# 거래대금
			'value' : 'float'
		}
	]
}

# 주식선물틱분별체결조회(API용)(t8406)
db_outblock_query_t8406 = {
	't8406OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 거래량
			'volume' : 'double',
			# 거래대금
			'value' : 'double',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openupdn' : 'long',
			# 체결수량
			'cvolume' : 'long',
			# 매수순간체결건수
			's_mschecnt' : 'long',
			# 매도순간체결건수
			's_mdchecnt' : 'long',
			# 순매수순간체결건수
			'ss_mschecnt' : 'long',
			# 매수순간체결량
			's_mschevol' : 'double',
			# 매도순간체결량
			's_mdchevol' : 'double',
			# 순매수순간체결량
			'ss_mschevol' : 'double',
			# 체결강도(거래량)
			'chdegvol' : 'float',
			# 체결강도(건수)
			'chdegcnt' : 'float'
		}
	]
}

# API용주식멀티현재가조회(t8407)
db_outblock_query_t8407 = {
	't8407OutBlock1' : [
		{
			# 종목코드
			'shcode' : 'char',
			# 종목명
			'hname' : 'char',
			# 현재가
			'price' : 'long',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'long',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 매도호가
			'offerho' : 'long',
			# 매수호가
			'bidho' : 'long',
			# 체결수량
			'cvolume' : 'long',
			# 체결강도
			'chdegree' : 'float',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 거래대금(백만)
			'value' : 'long',
			# 우선매도잔량
			'offerrem' : 'long',
			# 우선매수잔량
			'bidrem' : 'long',
			# 총매도잔량
			'totofferrem' : 'long',
			# 총매수잔량
			'totbidrem' : 'long',
			# 전일종가
			'jnilclose' : 'long',
			# 상한가
			'uplmtprice' : 'long',
			# 하한가
			'dnlmtprice' : 'long'
		}
	]
}

# CME야간선물틱분별체결조회(API용)(t8408)
db_outblock_query_t8408 = {
	't8408OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 거래량
			'volume' : 'double',
			# 거래대금
			'value' : 'double',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openupdn' : 'long',
			# 체결수량
			'cvolume' : 'long',
			# 매수순간체결건수
			's_mschecnt' : 'long',
			# 매도순간체결건수
			's_mdchecnt' : 'long',
			# 순매수순간체결건수
			'ss_mschecnt' : 'long',
			# 매수순간체결량
			's_mschevol' : 'double',
			# 매도순간체결량
			's_mdchevol' : 'double',
			# 순매수순간체결량
			'ss_mschevol' : 'double',
			# 체결강도(거래량)
			'chdegvol' : 'float',
			# 체결강도(건수)
			'chdegcnt' : 'float'
		}
	]
}

# CME야간선물미결제약정추이(API용)(t8409)
db_outblock_query_t8409 = {
	't8409OutBlock' : {
		# 현재가
		'price' : 'float',
		# 전일대비구분
		'sign' : 'char',
		# 전일대비
		'change' : 'float',
		# 등락율
		'diff' : 'float',
		# 체결수량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'double',
		# 미결제수량
		'openyak' : 'long'
	},
	't8409OutBlock1' : [
		{
			# 일자시간
			'dt' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 미결제시량
			'openopenyak' : 'long',
			# 미결제고량
			'highopenyak' : 'long',
			# 미결제저량
			'lowopenyak' : 'long',
			# 미결제종량
			'closeopenyak' : 'long',
			# 미결증감
			'openupdn' : 'long'
		}
	]
}

# 주식챠트(틱/n틱)(t8411)
db_outblock_query_t8411 = {
	't8411OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'long',
		# 전일고가
		'jihigh' : 'long',
		# 전일저가
		'jilow' : 'long',
		# 전일종가
		'jiclose' : 'long',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'long',
		# 당일고가
		'dihigh' : 'long',
		# 당일저가
		'dilow' : 'long',
		# 당일종가
		'diclose' : 'long',
		# 상한가
		'highend' : 'long',
		# 하한가
		'lowend' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8411OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 거래량
			'jdiff_vol' : 'long',
			# 수정구분
			'jongchk' : 'long',
			# 수정비율
			'rate' : 'double',
			# 수정주가반영항목
			'pricechk' : 'long'
		}
	]
}

# 주식챠트(N분)(t8412)
db_outblock_query_t8412 = {
	't8412OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'long',
		# 전일고가
		'jihigh' : 'long',
		# 전일저가
		'jilow' : 'long',
		# 전일종가
		'jiclose' : 'long',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'long',
		# 당일고가
		'dihigh' : 'long',
		# 당일저가
		'dilow' : 'long',
		# 당일종가
		'diclose' : 'long',
		# 상한가
		'highend' : 'long',
		# 하한가
		'lowend' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8412OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long',
			# 수정구분
			'jongchk' : 'long',
			# 수정비율
			'rate' : 'double',
			# 종가등락구분(1:상한2:상승3:보합4:하한5:하락)
			'sign' : 'char'
		}
	]
}

# 주식챠트(일주월)(t8413)
db_outblock_query_t8413 = {
	't8413OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'long',
		# 전일고가
		'jihigh' : 'long',
		# 전일저가
		'jilow' : 'long',
		# 전일종가
		'jiclose' : 'long',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'long',
		# 당일고가
		'dihigh' : 'long',
		# 당일저가
		'dilow' : 'long',
		# 당일종가
		'diclose' : 'long',
		# 상한가
		'highend' : 'long',
		# 하한가
		'lowend' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8413OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'long',
			# 고가
			'high' : 'long',
			# 저가
			'low' : 'long',
			# 종가
			'close' : 'long',
			# 거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long',
			# 수정구분
			'jongchk' : 'long',
			# 수정비율
			'rate' : 'double',
			# 수정주가반영항목
			'pricechk' : 'long',
			# 수정비율반영거래대금
			'ratevalue' : 'long',
			# 종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)
			'sign' : 'char'
		}
	]
}

# 선물옵션차트(틱/n틱)(t8414)
db_outblock_query_t8414 = {
	't8414OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 상한가
		'highend' : 'float',
		# 하한가
		'lowend' : 'float',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8414OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'jdiff_vol' : 'long',
			# 미결제약정
			'openyak' : 'long'
		}
	]
}

# 선물/옵션챠트(N분)(t8415)
db_outblock_query_t8415 = {
	't8415OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 상한가
		'highend' : 'float',
		# 하한가
		'lowend' : 'float',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8415OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 누적거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long',
			# 미결제약정
			'openyak' : 'long'
		}
	]
}

# 선물/옵션챠트(일주월)(t8416)
db_outblock_query_t8416 = {
	't8416OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 상한가
		'highend' : 'float',
		# 하한가
		'lowend' : 'float',
		# 연속일자
		'cts_date' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8416OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 누적거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long',
			# 미결제약정
			'openyak' : 'long'
		}
	]
}

# 업종차트(틱/n틱)(t8417)
db_outblock_query_t8417 = {
	't8417OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 장시작시간(HHMMSS)
		's_time' : 'char',
		# 장종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8417OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'jdiff_vol' : 'long'
		}
	]
}

# 업종챠트(N분)(t8418)
db_outblock_query_t8418 = {
	't8418OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 당일거래대금
		'disvalue' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 연속시간
		'cts_time' : 'char',
		# 업종시작시간(HHMMSS)
		's_time' : 'char',
		# 업종종료시간(HHMMSS)
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8418OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long'
		}
	]
}

# 업종챠트(일주월)(t8419)
db_outblock_query_t8419 = {
	't8419OutBlock' : {
		# 단축코드
		'shcode' : 'char',
		# 전일시가
		'jisiga' : 'float',
		# 전일고가
		'jihigh' : 'float',
		# 전일저가
		'jilow' : 'float',
		# 전일종가
		'jiclose' : 'float',
		# 전일거래량
		'jivolume' : 'long',
		# 당일시가
		'disiga' : 'float',
		# 당일고가
		'dihigh' : 'float',
		# 당일저가
		'dilow' : 'float',
		# 당일종가
		'diclose' : 'float',
		# 당일거래대금
		'disvalue' : 'long',
		# 연속일자
		'cts_date' : 'char',
		# 업종시작시간
		's_time' : 'char',
		# 업종종료시간
		'e_time' : 'char',
		# 동시호가처리시간(MM:분)
		'dshmin' : 'char',
		# 레코드카운트
		'rec_count' : 'long'
	},
	't8419OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 거래량
			'jdiff_vol' : 'long',
			# 거래대금
			'value' : 'long'
		}
	]
}

# 전체업종(t8424)
db_outblock_query_t8424 = {
	't8424OutBlock' : [
		{
			# 업종명
			'hname' : 'char',
			# 업종코드
			'upcode' : 'char'
		}
	]
}

# 전체테마(t8425)
db_outblock_query_t8425 = {
	't8425OutBlock' : [
		{
			# 테마명
			'tmname' : 'char',
			# 테마코드
			'tmcode' : 'char'
		}
	]
}

# 상품선물마스터조회(API용)(t8426)
db_outblock_query_t8426 = {
	't8426OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char'
		}
	]
}

# 과거데이터시간대별조회(t8427)
db_outblock_query_t8427 = {
	't8427OutBlock' : {
		# 선물옵션코드
		'focode' : 'char',
		# 날짜
		'date' : 'char',
		# 시간
		'time' : 'char'
	},
	't8427OutBlock1' : [
		{
			# 날짜
			'date' : 'char',
			# 시간
			'time' : 'char',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 종가
			'close' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 거래증가율
			'diff_vol' : 'float',
			# 미결수량
			'openyak' : 'long',
			# 미결증감
			'openyakupdn' : 'long',
			# 거래대금
			'value' : 'float'
		}
	]
}

# 증시주변자금추이(t8428)
db_outblock_query_t8428 = {
	't8428OutBlock' : {
		# 날짜CTS
		'date' : 'char',
		# IDX
		'idx' : 'long'
	},
	't8428OutBlock1' : [
		{
			# 일자
			'date' : 'char',
			# 지수
			'jisu' : 'float',
			# 대비구분
			'sign' : 'char',
			# 대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 거래량
			'volume' : 'long',
			# 고객예탁금_억원
			'custmoney' : 'long',
			# 예탁증감_억원
			'yecha' : 'long',
			# 회전율
			'vol' : 'float',
			# 미수금_억원
			'outmoney' : 'long',
			# 신용잔고_억원
			'trjango' : 'long',
			# 선물예수금_억원
			'futymoney' : 'long',
			# 주식형_억원
			'stkmoney' : 'long',
			# 혼합형_억원(주식)
			'mstkmoney' : 'long',
			# 혼합형_억원(채권)
			'mbndmoney' : 'long',
			# 채권형_억원
			'bndmoney' : 'long',
			# 필러(구.단기채권)
			'bndsmoney' : 'long',
			# MMF_억원(주식)
			'mmfmoney' : 'long'
		}
	]
}

# EUREX야간옵션선물틱분별체결조회챠트(t8429)
db_outblock_query_t8429 = {
	't8429OutBlock1' : [
		{
			# 시간
			'chetime' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 시가
			'open' : 'float',
			# 고가
			'high' : 'float',
			# 저가
			'low' : 'float',
			# 거래량
			'volume' : 'double',
			# 체결수량
			'cvolume' : 'long',
			# 매수순간체결건수
			's_mschecnt' : 'long',
			# 매도순간체결건수
			's_mdchecnt' : 'long',
			# 순매수순간체결건수
			'ss_mschecnt' : 'long',
			# 매수순간체결량
			's_mschevol' : 'double',
			# 매도순간체결량
			's_mdchevol' : 'double',
			# 순매수순간체결량
			'ss_mschevol' : 'double',
			# 체결강도(거래량)
			'chdegvol' : 'float',
			# 체결강도(건수)
			'chdegcnt' : 'float'
		}
	]
}

# 주식종목조회(t8430)
db_outblock_query_t8430 = {
	't8430OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char',
			# ETF구분(1:ETF)
			'etfgubun' : 'char',
			# 상한가
			'uplmtprice' : 'long',
			# 하한가
			'dnlmtprice' : 'long',
			# 전일가
			'jnilclose' : 'long',
			# 주문수량단위
			'memedan' : 'char',
			# 기준가
			'recprice' : 'long',
			# 구분(1:코스피2:코스닥)
			'gubun' : 'char'
		}
	]
}

# ELW종목조회(t8431)
db_outblock_query_t8431 = {
	't8431OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char',
			# 상한가
			'uplmtprice' : 'long',
			# 하한가
			'dnlmtprice' : 'long',
			# 전일종가
			'jnilclose' : 'long',
			# 기준가
			'recprice' : 'long'
		}
	]
}

# 지수선물마스터조회API용(t8432)
db_outblock_query_t8432 = {
	't8432OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char',
			# 상한가
			'uplmtprice' : 'float',
			# 하한가
			'dnlmtprice' : 'float',
			# 전일종가
			'jnilclose' : 'float',
			# 전일고가
			'jnilhigh' : 'float',
			# 전일저가
			'jnillow' : 'float',
			# 기준가
			'recprice' : 'float'
		}
	]
}

# 지수옵션마스터조회API용(t8433)
db_outblock_query_t8433 = {
	't8433OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char',
			# 상한가
			'hprice' : 'float',
			# 하한가
			'lprice' : 'float',
			# 전일종가
			'jnilclose' : 'float',
			# 전일고가
			'jnilhigh' : 'float',
			# 전일저가
			'jnillow' : 'float',
			# 기준가
			'recprice' : 'float'
		}
	]
}

# 선물/옵션멀티현재가조회(t8434)
db_outblock_query_t8434 = {
	't8434OutBlock1' : [
		{
			# 한글명
			'hname' : 'char',
			# 현재가
			'price' : 'float',
			# 전일대비구분
			'sign' : 'char',
			# 전일대비
			'change' : 'float',
			# 등락율
			'diff' : 'float',
			# 누적거래량
			'volume' : 'long',
			# 체결건수
			'checnt' : 'long',
			# 단축코드
			'focode' : 'char'
		}
	]
}

# 기초자산리스트조회(t9905)
db_outblock_query_t9905 = {
	't9905OutBlock1' : [
		{
			# 단축코드
			'shcode' : 'char',
			# 표준코드
			'expcode' : 'char',
			# 종목명
			'hname' : 'char'
		}
	]
}

# 만기월조회(t9907)
db_outblock_query_t9907 = {
	't9907OutBlock1' : [
		{
			# 만기월
			'lastym' : 'char',
			# 만기월명
			'lastnm' : 'char'
		}
	]
}

# ELW마스터조회API용(t9942)
db_outblock_query_t9942 = {
	't9942OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char'
		}
	]
}

# 지수선물마스터조회API용(t9943)
db_outblock_query_t9943 = {
	't9943OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char'
		}
	]
}

# 지수옵션마스터조회API용(t9944)
db_outblock_query_t9944 = {
	't9944OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char'
		}
	]
}

# 주식마스터조회API용-종목명40bytes(t9945)
db_outblock_query_t9945 = {
	't9945OutBlock' : [
		{
			# 종목명
			'hname' : 'char',
			# 단축코드
			'shcode' : 'char',
			# 확장코드
			'expcode' : 'char',
			# ETF구분
			'etfchk' : 'char',
			# filler
			'filler' : 'char'
		}
	]
}

# VI발동해제(VI_)
db_outblock_subscription_VI_ = {
	'OutBlock' : {
		# 구분
		'vi_gubun' : 'char',
		# VI발동기준가격
		'vi_recprice' : 'long',
		# VI발동가격
		'vi_trgprice' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# 상품선물예상체결(YC3)
db_outblock_subscription_YC3 = {
	'OutBlock' : {
		# 예상체결시간
		'ychetime' : 'char',
		# 예상체결가격
		'yeprice' : 'float',
		# 예상체결수량
		'yevolume' : 'long',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'float',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 단축코드
		'shcode' : 'char'
	}
}

# 지수선물예상체결(YFC)
db_outblock_subscription_YFC = {
	'OutBlock' : {
		# 예상체결시간
		'ychetime' : 'char',
		# 예상체결가격
		'yeprice' : 'float',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'float',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 단축코드
		'futcode' : 'char'
	}
}

# 주식선물예상체결(YJC)
db_outblock_subscription_YJC = {
	'OutBlock' : {
		# 예상체결시간
		'ychetime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'long',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 단축코드
		'futcode' : 'char'
	}
}

# 예상지수(YJ)
db_outblock_subscription_YJ_ = {
	'OutBlock' : {
		# 시간
		'time' : 'char',
		# 예상지수
		'jisu' : 'float',
		# 예상전일대비구분
		'sign' : 'char',
		# 예상전일비
		'change' : 'float',
		# 예상등락율
		'drate' : 'float',
		# 예상체결량
		'cvolume' : 'long',
		# 누적거래량
		'volume' : 'long',
		# 예상거래대금
		'value' : 'long',
		# 업종코드
		'upcode' : 'char'
	}
}

# KOSDAQ예상체결(YK3)
db_outblock_subscription_YK3 = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결수량
		'yevolume' : 'long',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'long',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 예상매도호가
		'yofferho0' : 'long',
		# 예상매수호가
		'ybidho0' : 'long',
		# 예상매도호가수량
		'yofferrem0' : 'long',
		# 예상매수호가수량
		'ybidrem0' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# 지수옵션예상체결(YOC)
db_outblock_subscription_YOC = {
	'OutBlock' : {
		# 예상체결시간
		'ychetime' : 'char',
		# 예상체결가격
		'yeprice' : 'float',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'float',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 단축코드
		'optcode' : 'char'
	}
}

# KOSPI예상체결(YS3)
db_outblock_subscription_YS3 = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결수량
		'yevolume' : 'long',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'long',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 예상매도호가
		'yofferho0' : 'long',
		# 예상매수호가
		'ybidho0' : 'long',
		# 예상매도호가수량
		'yofferrem0' : 'long',
		# 예상매수호가수량
		'ybidrem0' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

# ELW예상체결(Ys3)
db_outblock_subscription_Ys3_4ELW = {
	'OutBlock' : {
		# 호가시간
		'hotime' : 'char',
		# 예상체결가격
		'yeprice' : 'long',
		# 예상체결수량
		'yevolume' : 'long',
		# 예상체결가전일종가대비구분
		'jnilysign' : 'char',
		# 예상체결가전일종가대비
		'jnilchange' : 'long',
		# 예상체결가전일종가등락율
		'jnilydrate' : 'float',
		# 예상매도호가
		'yofferho0' : 'long',
		# 예상매수호가
		'ybidho0' : 'long',
		# 예상매도호가수량
		'yofferrem0' : 'long',
		# 예상매수호가수량
		'ybidrem0' : 'long',
		# 단축코드
		'shcode' : 'char'
	}
}

