from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


# don't forget gunicorn and nginx
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/templates")
def templates():
    return render_template("templates.html")


@app.route("/code")
def code():
    return render_template("code.html")


@app.route("/resume")
def tos():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf/'
    return send_from_directory(filepath, 'Resume(1).pdf')


if __name__ == "__main__":
    app.run(debug=True)
