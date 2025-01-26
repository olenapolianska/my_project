from flask import *

from DBManager import DBManager

app = Flask("Films")
app.secret_key = "2503"
db_name = "MY_PROJECT.db"

@app.route("/")
def films():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Фільм")
    return render_template("films.html", compositions=compositions)

@app.route("/composition/<int:composition_id>")
def get_topic(composition_id):
    db_manager = DBManager(db_name)
    topics = db_manager.get_topics(composition_id)
    session["topics"] = topics
    session["composition_index"] = 0

    return redirect(url_for("show_topic", composition_id=composition_id))

@app.route("/composition/<int:composition_id>/topic")
def show_topic(composition_id):
    nomer = session["composition_index"]
    t = session["topics"][nomer]
    db_manager = DBManager(db_name)

    return render_template("topic.html", topic=t, composition_id=composition_id)


@app.route("/composition/<int:composition_id>/actors")
def get_actors(composition_id):
    db_manager = DBManager(db_name)
    actors = db_manager.get_actors_by_film(composition_id)
    return render_template("actors.html", actors=actors, composition_id=composition_id)




@app.route("/series")
def series():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Серіал")
    return render_template("series.html", compositions=compositions)


@app.route("/cartoon_series")
def cartoon_series():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Мультсеріал")
    return render_template("cartoon_series.html", compositions=compositions)


@app.route("/cartoons")
def cartoons():
    db_manager = DBManager(db_name)
    compositions = db_manager.get_compositions_by_vud("Мультфільм")
    return render_template("cartoons.html", compositions=compositions)




app.run()