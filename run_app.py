from flask import *

from DBManager import DBManager

app = Flask("Films")
app.secret_key = "2503"
db_name = "MY_PROJECT.db"

@app.route("/")
def main_page():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Фільм")
    return render_template("main_page.html", compositions=compositions)

@app.route("/composition/<int:composition_id>")
def get_topic(composition_id):
    db_manager = DBManager(db_name)
    topic = db_manager.get_topic(composition_id)
    return render_template("topic.html", topic=topic, composition_id=composition_id)


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
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Мультфільм")
    return render_template("cartoons.html", compositions=compositions)




app.run()