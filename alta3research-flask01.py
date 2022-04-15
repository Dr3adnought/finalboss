#!/usr/bin/env python3
"""-----FINAL PROJECT: FLASK API (Jeffrey Lee)-----"""
"""--- this file to show proficiency with Flask ---"""


from tkinter.font import names
from flask import Flask, render_template, request
import requests
from flask import redirect
from flask import url_for
from flask import jsonify
from html import unescape
import csv
app = Flask(__name__)

# List of movies
movies_list = []


# serve homepage template
@app.route("/")
def index():
    return render_template("index.html")

# accepting input from user POSTing a submission


# @app.route("/addtolist", methods=["POST"])
# def addtolist():
#     return render_template("listed.html", movies=movies)


@app.route("/listed", methods=["POST", "GET"])
def listed():
    movies = request.form.get("movies")
    name = request.form.get("name")
    print(movies)
    print(name)
    movies_list.append({name: movies})
    if not movies or not name:
        return render_template("failure.html")
    return render_template("listed.html", movies=movies_list)


if __name__ == "__main__":
    app.run()
