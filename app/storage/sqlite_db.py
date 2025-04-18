#  Purpose:
#
#
#  Key Attributes:
#
#
#  Main Methods:
#
#
#  Example:

import sqlite3
from datetime import datetime

class SqliteDB:
    def __init(self, db_path=None):
     self.db_path = db_path


    # create and return database connection
    def __connect(self):
        return sqlite3.connect(self.db_path)