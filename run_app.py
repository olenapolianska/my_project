from flask import *

app = Flask("Films")



@app.route("/")
def index():
    return render_template("index.html")


app.run()