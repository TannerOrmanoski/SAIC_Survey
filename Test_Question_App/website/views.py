import sqlite3
from flask import Blueprint, render_template, request
from .models import User
from . import db 

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

    return render_template("results.html", testform = test)
