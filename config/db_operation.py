import mysql.connector
from config.config import DB_CONFIG

def connect_to_database() -> mysql.connector:
    """
    Establish the database connection.
    """

    connection = mysql.connector.connect(
        user="root",
        password="12345",
        host="127.0.0.1",
        database="ELECTRONICS",
        connection_timeout=10000
    )

    return connection

def create_cursor(connection):
    print("Connection is ready!!")
    return connection.cursor()

def close_connection(connection):
    connection.close()
