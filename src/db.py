from __init__ import driver
# DB = {}

def get_session(db_type='write'):
	# if DB.get(db_type):
	# 	return DB[db_type]

	# DB[db_type] = driver.session()
	return driver.session()


def run_get_query(query):
	def fetch(tx, query):
		return tx.run(query)

	session = get_session()
	result = session.read_transaction(fetch, query)
	session.close()
	return result

def run_post_query(query, data):
	def put(tx, query, data):
		return tx.run(query, **data).single().value()

	session = get_session()
	result = session.write_transaction(put, query, data)
	session.close()
	return result