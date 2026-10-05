import sqlite3
from pathlib import Path
from .models import MemoryCreate, MemoryItem

class MemorySystem:
    def __init__(self, db_path: str):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._initialize()
    def _connect(self):
        db = sqlite3.connect(self.db_path)
        db.row_factory = sqlite3.Row
        return db
    def _initialize(self):
        with self._connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS memories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                category TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
    def add(self, item: MemoryCreate) -> MemoryItem:
        with self._connect() as db:
            cursor = db.execute("INSERT INTO memories(content,category) VALUES (?,?)",(item.content,item.category))
            row = db.execute("SELECT id,content,category,created_at FROM memories WHERE id=?",(cursor.lastrowid,)).fetchone()
        return MemoryItem(**dict(row))
    def recent(self, limit: int = 20) -> list[MemoryItem]:
        with self._connect() as db:
            rows = db.execute("SELECT id,content,category,created_at FROM memories ORDER BY id DESC LIMIT ?",(limit,)).fetchall()
        return [MemoryItem(**dict(row)) for row in rows]
