import psycopg2

connection = psycopg2.connect(database="UserDB", host="localhost", user="postgres", password="Da07011337310@")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS persons (id serial PRIMARY KEY, name VARCHAR(50))''')

cursor.execute('''INSERT INTO persons (name) VALUES ('John')''')
cursor.execute('''INSERT INTO persons (name) VALUES ('Mary')''')
cursor.execute('''INSERT INto persons (name) VALUES ('Tinubu')''')

connection.commit()
cursor.close()
connection.close()
print("Database created successfully")
