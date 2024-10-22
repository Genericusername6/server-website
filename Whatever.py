import flask

app = flask.Flask(__name__)

@app.route("/")
def whatever():
    return flask.render_template("something.html")

