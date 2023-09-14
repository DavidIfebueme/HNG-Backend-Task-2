from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

def database_connection():
    connection = psycopg2.connect(DATABASE_URL)
    return connection

@app.route('/persons', methods=['GET'])
def get_persons():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM persons ORDER BY id''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    persons = [{'id': row[0], 'name': row[1]} for row in data]
    return jsonify(persons)

@app.route('/person/<int:id>', methods=['GET'])
def get_person(id):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM persons WHERE id = %s''', (id,))
    person = cursor.fetchone()
    cursor.close()
    connection.close()
    if person:
        return jsonify({'id': person[0], 'name': person[1]})
    else:
        return jsonify({'message': 'Person not found'}), 404

@app.route('/update/<int:id>', methods=['PUT'])
def update_person(id):
    connection = database_connection()
    cursor = connection.cursor()
    data = request.get_json()
    name = data.get('name')
    cursor.execute('''UPDATE persons SET name=%s WHERE id=%s''', (name, id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Person updated successfully'})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_person(id):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM persons WHERE id=%s''', (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Person deleted successfully'})

@app.route('/create', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO persons (name) VALUES (%s) RETURNING id''', (name,))
    new_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Person created successfully', 'id': new_id})

if __name__ == "__main__":
    app.run(debug=True)

