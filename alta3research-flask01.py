#!/usr/bin/env python3
"""-----FINAL PROJECT: FLASK API (Jeffrey Lee)-----"""
"""--- this file to show proficiency with Flask ---"""


from tkinter.font import names
from flask import Flask, render_template, request
import requests
from flask import redirect
from flask import jsonify
from html import unescape
import csv
app = Flask(__name__)

# List of movies
movies = []


# serve homepage template
@app.route("/")
def index():
    return render_template("index.html")

# accepting input from user POSTing a submission


@app.route("/wanted", methods=["POST"])
def wanted():
    movies = request.form.get["movies"]
    name = request.form.get["name"]
    if not movies or not name:
        return render_template("failure.html")
    with open("/Users/jeffrlek/PythonClass/finalboss/list.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((movies, name))
    return render_template("listed.html")

# submissions pushed here


@app.route("/listed", methods=['POST'])
def listed():
    with open("/Users/jeffrlek/PythonClass/finalboss/list.csv", "r") as file:
        reader = csv.reader(file)
        movies = list(reader)
    return render_template("success.html", movies=movies)


if __name__ == "__main__":
    app.run()
