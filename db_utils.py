import psycopg2


def create_db_connection():
	conn_string='host=localhost port=5432 dbname=boyddb user=stu'
	return psycopg2.connect(conn_string)
