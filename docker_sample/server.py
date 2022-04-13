import imp

import flask
app = flask.Flask("app server")

@app.route("/")
def index():
    return "Hello World"

app.run(debug=True, host="0.0.0.0", port=80)