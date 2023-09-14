import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the DATABASE_URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Attempt to establish a database connection
try:
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    
    # Execute a simple query to test the connection
    cursor.execute("SELECT 1")
    
    # If the query executed successfully, print a message
    print("Database connection is successful")
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
except Exception as e:
    # If there was an error, print an error message
    print("Error connecting to the database:", e)
