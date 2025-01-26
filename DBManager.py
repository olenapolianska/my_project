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
            producer TEXT,
            content TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Actors (
            id INT PRIMARY KEY,
            photo JPG,
            name TEXT,
            full_name TEXT,
            birthday INT,
            country TEXT,
            films TEXT);""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS film_actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            film_id INT,
            actor_id INT,
            FOREIGN KEY (film_id) REFERENCES compositions(id),
            FOREIGN KEY (actor_id) REFERENCES actors(id)
        );""")
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
    def add_topic(self, id, composition_id, photo,  year, country, age, genre, actors, producer, content):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO topics(id, composition_id, photo, year, country, age, genre, actors, producer, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [id, composition_id, photo, year, country, age, genre, actors, producer, content])
        self.connection.commit()
        cursor.close()

    def get_topics(self, composition_id):
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

    def add_actor_to_film(self, film_id, actor_id):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO film_actors(film_id, actor_id) VALUES (?, ?)", [film_id, actor_id])
        self.connection.commit()
        cursor.close()

    def get_actors_by_film(self, film_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT actors.id, actors.name, actors.full_name, actors.photo, actors.birthday, actors.country, actors.films 
            FROM film_actors
            JOIN actors ON film_actors.actor_id = actors.id
            WHERE film_actors.film_id = ?
        """, [film_id])
        res = cursor.fetchall()
        cursor.close()
        return res





