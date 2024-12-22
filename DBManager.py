import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS films (
            id INT PRIMARY KEY,
            title VARCHAR (255),
            description TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INT PRIMARY KEY,
            film_id INT,
            content TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Actors (
            id INT PRIMARY KEY,
            film_id INT,
            content TEXT,);
        """)
        self.connection.commit()

#потрібно створити бд для фільмів сюжету і акторів