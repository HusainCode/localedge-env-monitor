import tempfile
import os
import pytest
from pathlib import Path

from storage.sqlite_db import SqliteDB


class TestSqliteDB:
    @pytest.fixture(scope="function")
    def temp_db(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            db = SqliteDB(db_path=tmp.name)
            yield db
            os.unlink(tmp.name)

    def test_write_and_read_roundtrip(self, temp_db):
        create_query = "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"
        insert_query = "INSERT INTO users (name) VALUES (?)"
        select_query = "SELECT * FROM users"

        temp_db.execute(create_query)
        temp_db.execute(insert_query, ("Alice",))
        temp_db.execute(insert_query, ("Bob",))

        all_rows = temp_db.fetchall(select_query)
        assert len(all_rows) == 2
        assert all_rows[0][1] == "Alice"
        assert all_rows[1][1] == "Bob"

    def test_fetchone_returns_single_row(self, temp_db):
        temp_db.execute("CREATE TABLE t (v TEXT)")
        temp_db.execute("INSERT INTO t (v) VALUES (?)", ("value",))
        row = temp_db.fetchone("SELECT * FROM t")
        assert row == (1, "value")
