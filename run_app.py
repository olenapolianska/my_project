from flask import *

from DBManager import DBManager

app = Flask("Films")
db_name = "MY_PROJECT.db"

@app.route("/")
def index():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions()
    return render_template("index.html", compositions=compositions)

@app.route("/films")
def films():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Фільм")
    return render_template("films.html", compositions=compositions)

@app.route("/series")
def series():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Серіал")
    return render_template("series.html", compositions=compositions)


@app.route("/cartoon_series")
def cartoon_series():
    return render_template("cartoon_series.html")

@app.route("/cartoons")
def cartoons():
    return render_template("cartoons.html")

@app.route("/main_page")
def main_page():
    return render_template("main_page.html")


app.run()