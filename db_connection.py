# db_connection.py

import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname="dellstore",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
        )
        return connection
    except Exception as e:
        print("Error: ", e)
        return None