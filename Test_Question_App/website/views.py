import sqlite3
from flask import Blueprint, render_template, request
from .models import User
from . import db
import os.path
import csv

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        Connection = sqlite3.connect("website/database2.db")
        cursor = Connection.cursor()
        query = "Select * from User"
        cursor.execute(query)
        test = cursor.fetchall()

    return render_template("results.html", testform=test)


@views.route('/export_to_csv')
def csv_export():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database2.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * From User")
    columns = [column[0] for column in c.description]
    results = []
    for row in c.fetchall():
        results.append(dict(zip(columns, row)))
    with open("results.csv", "w", newline='') as new_file:
        fieldnames = columns
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in results:
            writer.writerow(line)
    conn.close()

    return render_template("export_comp.html")
