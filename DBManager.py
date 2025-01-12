import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS compositions(
            id INT PRIMARY KEY,
            image JPG,
            title VARCHAR (255),
            description TEXT,
            vud TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INT PRIMARY KEY,
            film_id INT,
            content TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Actors (
            id INT PRIMARY KEY,
            name TEXT);
        """)
        self.connection.commit()

    def add_compositions(self, id, image, title, description, vud):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO compositions(id, image, title, description, vud) VALUES (?, ?, ?, ?, ?)", [id, image, title, description, vud])
        self.connection.commit()
        cursor.close()

    def get_compositions(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM compositions")
        res = cursor.fetchall()
        cursor.close()
        return res