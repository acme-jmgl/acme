import sqlite3


class SqliteTodoStore:
    """SQLite-backed store. Not wired in yet."""

    def __init__(self, path=":memory:"):
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._db.execute(
            "create table if not exists todos ("
            "id integer primary key, title text not null, done integer not null default 0)"
        )

    def list(self):
        rows = self._db.execute("select id, title, done from todos order by id")
        return [dict(r, done=bool(r["done"])) for r in rows]
