from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)

def database_connection():
    connection = psycopg2.connect(database="UserDB", host="localhost", user="", password="")
    return connection


@app.route('/')
def index():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', users=users)