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
            composition_id INT,
            photo JPG,
            year INT,
            country TEXT,
            age INT,
            genre TEXT,
            actors TEXT,
            producer TEXT
            content TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Actors (
            id INT PRIMARY KEY,
            photo JPG,
            name TEXT,
            full_name TEXT,
            birthday INT,
            country TEXT,
            films TEXT);
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

    def get_compositions_by_vud(self, vud):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM compositions WHERE vud = \"{vud}\"")
        res = cursor.fetchall()
        cursor.close()
        return res
    def add_topics(self, id, composition_id, photo,  year, country, age, genre, actors, producer, content):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO topics(id, composition_id, photo, year, country, age, genre, actors, producer, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [id, composition_id, photo, year, country, age, genre, actors, producer, content])
        self.connection.commit()
        cursor.close()

    def get_topic(self, composition_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM topics WHERE composition_id = ?", [composition_id])
        res = cursor.fetchall()
        cursor.close()
        return res
    def add_actors(self, id, photo, name, full_name, birthday, country, films ):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO actors(id, photo, name, full_name, birthday, country, films ) VALUES (?, ?, ?, ?, ?, ?, ?)", [id, photo, name, full_name, birthday, country, films ])
        self.connection.commit()
        cursor.close()