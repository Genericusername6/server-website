import flask

app = flask.Flask(__name__)

@app.route("/")
def whatever():
    return flask.render_template("something.html", x=30)

@app.route("/anything")
def where_ever():
    return flask.render_template("anything.html")

@app.route("/<file>.<ext>")
def serveCss(file, ext):
    return app.send_static_file(f'{file}.{ext}')