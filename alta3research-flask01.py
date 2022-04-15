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
    return render_template("index.html")  # renders html page


@app.route("/listed", methods=["POST", "GET"])
def listed():
    # input and assignment to variable
    movies = request.form.get("movies")
    # input and assignment to variable
    name = request.form.get("name")
    print(movies)                               # print in terminal
    print(name)                                 # print in terminal
    # append running list (only on current run, if code hasn't been broken)
    movies_list.append({name: movies})
    if not movies or not name:                  # logic to check entries
        return render_template("failure.html")  # renders failure html page
    # renders listed html page
    return render_template("listed.html", movies=movies_list)


if __name__ == "__main__":
    app.run()
