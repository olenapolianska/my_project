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
    def add_topics(self, id, film_id, content):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO topics(id, film_id, content) VALUES (?, ?, ?)", [id, film_id, content])
        self.connection.commit()
        cursor.close()

    def get_topics(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM topics")
        res = cursor.fetchall()
        cursor.close()
        return res
    def add_actors(self, id, name):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO actors(id, name) VALUES (?, ?)", [id, name])
        self.connection.commit()
        cursor.close()