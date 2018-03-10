# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Secret"
@app.route("/")
def index():
    if "visits" in session:
        session["visits"] = session.get("visits") + 1
    else:
        session["visits"] = 1
        print session["visits"]
    return render_template("index.html")
@app.route("/addcount", methods = ["POST"])
def addcount():
    add2 = request.form["add2"]
    if add2 == "Add":
        session["visits"] = session.get("visits") + 1
    return redirect("/")
@app.route("/reset", methods = ["POST"])
def reset():
    reset = request.form["reset"]
    if reset == "reset":
        session["visits"] = 0
    return redirect("/")
app.run(debug=True)