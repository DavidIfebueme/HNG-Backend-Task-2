from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def database_connection():
    connection = psycopg2.connect(database="UserDB", host="localhost", user="postgres", password="Da07011337310@")
    return connection

@app.route('/')
def index():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM persons ORDER BY id''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', data=data)

@app.route('/person/<int:id>')
def view_person(id):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM persons WHERE id = %s''', (id,))
    person = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('view_person.html', person=person)

@app.route('/update/<int:id>', methods=['POST'])
def update_person(id):
    connection = database_connection()
    cursor = connection.cursor()
    name = request.form['name']
    cursor.execute('''UPDATE persons SET name=%s WHERE id=%s''', (name, id))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('view_person', id=id))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_person(id):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM persons WHERE id=%s''', (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        connection = database_connection()
        cursor = connection.cursor()
        name = request.form['name']
        cursor.execute('''INSERT INTO persons (name) VALUES (%s)''', (name,))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('index'))
    else:
        return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)
