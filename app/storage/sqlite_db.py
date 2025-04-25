#  Purpose:
#    Lightweight SQLite database wrapper for simplified connection handling
#    and extensibility for higher-level query methods.
#
#  Key Attributes:
#    - db_path (str): Filesystem path to the SQLite database file.
#
#  Main Methods:
#    - __connect(): Internal method to establish and return a database connection.
#    - execute(query, params): Execute a write or DDL statement.
#    - fetchall(query, params): Execute a read query and return all rows.
#    - fetchone(query, params): Execute a read query and return a single row.
#
#   Sources:
#       - https://docs.python.org/3/library/sqlite3.html


import sqlite3
from datetime import datetime

class SqliteDB:
    def __init__(self, db_path=None):
        if not db_path:
            raise ValueError("Database path must be specified.")
        self.db_path = db_path

    # Creat local connection mapped to db_path file
    def __connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    # execute a write query INSERT,UPDATE,DELETE
    def execute(self, query: str, params: tuple | None = None) -> None:
        params = params or ()
        # handle closing and opening automatically
        with self.__connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit() # persist changes

    def fetchall(self, query: str, params: tuple | None = None) -> list[tuple]:
        params = params or () # to ensure always something iterable to avoid TypeError
                              # This is equivalent to params () if params is None
        with self.__connect() as conn: # open connection using __connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetchone(self, query: str, params: tuple | None = None) -> tuple | None:
        params = params or ()
        with self.__connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
