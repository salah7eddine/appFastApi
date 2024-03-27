import psycopg2 as psycopg
from psycopg2.extras import RealDictCursor

# Replace these variables with your actual database credentials
DATABASE_NAME = 'DB_Fastapi'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = '1442'
DATABASE_HOST = 'localhost'
DATABASE_PORT = 5432  # Default PostgreSQL port is usually 5432

try:
    # Establish a connection to the database
    connection = psycopg.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        cursor_factory=RealDictCursor
    )

    # Create a cursor object using the connection
    cursor = connection.cursor()
    print("Connected!")
    

except psycopg.Error as e:
    print("Error connecting to the PostgreSQL database:", e)


def get_conn():
    return cursor