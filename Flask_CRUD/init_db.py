import psycopg2

connection = psycopg2.connect(database="UserDB", host="localhost", user="", password="")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username VARCHAR(50), age integer)''')

cursor.execute('''INSERT INTO users (username, age) VALUES ('John', 25)''')
cursor.execute('''INSERT INTO users (username, age) VALUES ('Mary', 27)''')

connection.commit()
cursor.close()
connection.close()
print("Database created successfully")
