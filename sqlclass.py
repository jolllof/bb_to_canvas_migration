import cx_Oracle

class sqlclass:

	def __init__(self, username, password, database, sql):
		self._username = username
		self._password = password
		self._database = database
		self._sql = sql
		self._cursor = None
		self._results = None

	def connect(self):
		con = cx_Oracle.connect(self._username, self._password, self._database)
		self._cursor = con.cursor()

	def runsql(self):
		self._cursor.execute(str(self._sql))
		self._results = self._cursor.fetchall()

	@property
	def cursor(self):
		return self._cursor
	
	@property
	def results(self):
		return self._results
	 