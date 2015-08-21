#dbutil.py

try:
	import pystock_xingAPI.outblock_template_for_db as outblock_list
except:
	import outblock_template_for_db as outblock_list

class DBUtil:
	def insert_for_outblock(cursor, table_name, outblocks, place_flag = False):
		"""
		cursor : cursor of sqlite3
		table_name(str) : table name to insert
		outblocks(dict or list) : return value of TR request
		place_flag(boolean) : if there is already a data in the table, place or ignore
		"""
		if not isinstance(outblocks, list):
			outblocks = [outblocks]
		if len(outblocks) < 0:
			return
		keys = list(outblocks[0].keys())
		columns = ', '.join(keys)
		values = ', '.join(map(lambda col:':'+col, keys))

		insert_query = "INSERT OR " + ('REPLACE' if place_flag else 'IGNORE') + " INTO " + table_name + " (" + columns +") VALUES (" + values +")"
		#print(insert_query)
		cursor.executemany(insert_query, outblocks)

	def create_table_for_outblock(cursor, table_name, tr_code, outblock_name, key_names = None, index_names = None):
		"""
		cursor : cursor of sqlite3
		table_name(str) : table name to create
		tr_code(str) : tr code
		outblock_name(str) : outblock name
		key_names(list) : column name for primary keynames
		index_names(list) : column names for index
		"""
		subscription = "db_outblock_subscription_" + tr_code
		query = "db_outblock_query_" + tr_code

		if hasattr(outblock_list, subscription):
			outblocks = getattr(outblock_list, subscription)
		elif hasattr(outblock_list, query):
			outblocks = getattr(outblock_list, query)
		else:
			raise TypeError("There is no such tr_code(%s)" % tr_code)

		outblock = outblocks.get(outblock_name)
		if not outblock:
			raise TypeError("There is no such outblock_name(%s)" % outblock_name)
		return DBUtil._create_table_for_outblock(cursor, table_name, outblock, key_names, index_names)

	def _create_table_for_outblock(cursor, table_name, outblock_for_db, key_names = None, index_names = None):
		type_table = {'long':int, 'char':str, 'float':float, 'double':float}
		if isinstance(outblock_for_db, list):
			outblock_for_db = outblock_for_db[0]
		if not isinstance(outblock_for_db, dict):
			raise TypeError("outblock_for_db must be an instance of dict or list that has dict as the first element")
		column_names = list(outblock_for_db.keys())
		types = list(map(lambda col:type_table[outblock_for_db[col]], column_names))
		return DBUtil.create_table(cursor, table_name, column_names, types, key_names, index_names)

	def create_table(cursor, table_name, column_names, types, key_names = None, index_names = None):
		"""
		cursor : cursor of sqlite3
		table_name(str) : table name to create
		column_names(list) : column names
		types(list) : column types, types must be one of int, float, str
		key_names(list) : column name for primary keynames
		index_names(list) : column names for index
		"""
		query_columns = []
		for i, type_ in enumerate(types):
			type_name = "TEXT"
			if type_ is int:
				type_name = "INTEGER"
			elif type_ is float:
				type_name = "REAL"
			elif type_ is str:
				type_name = "TEXT"

			query_columns.append("%s %s" % (column_names[i], type_name))
		query = "CREATE TABLE IF NOT EXISTS " + table_name + " (" + ', '.join(query_columns) + ");"

		if key_names is not None:
			index_name = '_'.join(key_names)
			key_name = ', '.join(key_names)
			query += "CREATE UNIQUE INDEX IF NOT EXISTS %s ON %s (%s);" % (table_name+'_'+index_name+'_id', table_name, key_name)

		if index_names is not None:
			for index in index_names:
				query += "CREATE INDEX IF NOT EXISTS %s ON %s (%s);" % (table_name+'_'+index+'_idx', table_name, index)
		#print(query)
		cursor.executescript(query)

if __name__ == '__main__':
	#DBUtil.create_table_for_outblock(None, 'table_name', 'CCEAQ01100', 'CCEAQ01100OutBlock3')
	#DBUtil.insert_for_outblock(None, 'table_name', outblock, place_flag = False)
	pass