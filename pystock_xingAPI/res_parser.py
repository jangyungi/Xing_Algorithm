#res_parser.py
import os

def _readline_until_not_empty(f):
	line = f.readline().strip()
	while line == '':
		line = f.readline().strip()
	if line is None:
		raise EOFError('Unexpected EOF while reading an res file')
	return line

def _case_insensitive_compare(str0, str1):
	return str0.lower() == str1.lower()

def _clean_strip(line):
	return list(map(str.strip, line.strip(';').strip().split(',')))

def res_parser(filepath, include_human_readable_info = False):
	ret = dict()
	with open(filepath, 'r') as f:
		# find BEGIN_FUNCTION_MAP start point
		line = _readline_until_not_empty(f)
		while not _case_insensitive_compare(line, 'BEGIN_FUNCTION_MAP'):
			line = _readline_until_not_empty(f)
		
		# parse tr_code
		line = _readline_until_not_empty(f)
		contents = _clean_strip(line)

		#query or subscription
		is_query = _case_insensitive_compare(contents[0], '.Func')
		desc = contents[1]

		# tr_code
		#---------------
		# res 파일속의 tr코드와 파일이름의 tr코드가 다른경우가 있음
		# 추측컨데, 비슷한 tr코드를(ex: 'YS3' vs. 'Ys3', Ys3->Ys3_4ELW)을 개발자들이 헷갈리지 않도록 원래의 tr코드 그대로 사용치 않고 변화를 준 것 같음
		# 원래 TR코드보다는 res파일이름을 기준으로 tr_code 저장
		#---------------
		#tr_code from rest file
		#tr_code = contents[2]
		#tr_code from filename
		tr_code = os.path.split(filepath)[1].split('.')[0].strip()

		header = {'tr_code':tr_code, 'is_query':is_query}
		if include_human_readable_info:
			header.update({'desc':desc, 'path':filepath})

		ret.update({'header':header})
		
		#find BEGIN_DATA_MAP start point
		line = _readline_until_not_empty(f)
		while not _case_insensitive_compare(line, 'BEGIN_DATA_MAP'):
			line = _readline_until_not_empty(f)
		
		line = _readline_until_not_empty(f)
		block = []
		while not _case_insensitive_compare(line, 'END_DATA_MAP'):
			a_block = dict()
			# a_block name, input or output, occurs
			contents = _clean_strip(line)
			is_input = 'input' in contents
			is_occurs = 'occurs' in contents
			a_block.update({'bname':contents[0],'is_input':is_input,'is_occurs':is_occurs}) #-------- bname ...

			line = _readline_until_not_empty(f)
			while not _case_insensitive_compare(line, 'begin'):
				line = _readline_until_not_empty(f)

			line = _readline_until_not_empty(f)
			args = []
			while not _case_insensitive_compare(line, 'end'):
				contents = _clean_strip(line)
				arg = {'code':contents[1]}
				if include_human_readable_info:
					arg.update({'desc':contents[0], 'type':contents[3], 'length':contents[4]})
				args.append(arg)
				line = _readline_until_not_empty(f)
			a_block.update({'args':args})
			line = _readline_until_not_empty(f)
			block.append(a_block)
		ret.update({'block':block})
		return ret

def multi_res_parser(filepath_list, include_human_readable_info = False):
	code_set = set()
	ret = []
	for filepath in filepath_list:
		r = res_parser(filepath, include_human_readable_info)
		tr_code = r['header']['tr_code']
		if not tr_code in code_set:
			code_set.add(tr_code)
			ret.append(r)
	return ret