"""cx_Oracle module allows access to Oracle Databases and has methods that allow execution of SQL"""
import cx_Oracle

class SqlClass:
    """sqlclass receives multiple executes Oracle SQL query and returns the results"""

    def __init__(self, username, password, database, sql):
        """Init method intializes all variables passed into the class"""
        self._username = username
        self._password = password
        self._database = database
        self._sql = sql
        self._cursor = None
        self._results = None

    def connect(self):
        """this method makes connection to Oracle Database
           and connection is kept open for other methods to execute query"""
        con = cx_Oracle.connect(self._username, self._password, self._database)
        self._cursor = con.cursor()

    def runsql(self):
        """this method retrieves variable containing code and executes query"""
        self._cursor.execute(str(self._sql))
        self._results = self._cursor.fetchall()

    @property
    def cursor(self):
        """cursor property simply keeps database connection open so runsql
           can execute sql query"""
        return self._cursor

    @property
    def results(self):
        """results method stores query results to be returned"""
        return self._results
	 
