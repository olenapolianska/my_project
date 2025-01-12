from DBManager import DBManager

db_manager = DBManager("MY_PROJECT1.db")
db_manager.create_tables()

db_manager.add_compositions(1, "втеча з шоушенка.jpg", "Втеча з Шоушенка (1994)", "Драма", "Фільм" )
