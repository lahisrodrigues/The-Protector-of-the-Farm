import os
import sqlite3


class Database:
    def __init__(self, db_name="farm_scores.db"):
        base_path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_path, "..", db_name)

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS highscores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_score(self, name: str, score: int, date: str):
        self.cursor.execute('''
            INSERT INTO highscores (name, score, date)
            VALUES (?, ?, ?)
        ''', (name, score, date))
        self.conn.commit()
        # aparece no terminal
        print(f"Success! {name} saved with {score} points in the database.")

    def get_top_scores(self, limit=5):
        self.cursor.execute('''
            SELECT name, score, date FROM highscores
            ORDER BY score DESC LIMIT ?
        ''', (limit,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
