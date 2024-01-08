# signup.py

import jwt
from config.db_operation import connect_to_database, create_cursor, close_connection
from config.config import TABLE_NAME2, SECRET_KEY

def create_table_if_not_exists(cursor):
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME2} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    '''
    cursor.execute(create_table_query)

def signup():
    try:
        connection = connect_to_database()
        cursor = create_cursor(connection)
        print("Connection to the database successful!!")

        create_table_if_not_exists(cursor)

        username = str(input("Username: "))
        password = str(input("Password: "))

        if username != "" and password != "":
            # You may want to hash the password before storing it in the database for security.
            # For simplicity, we're storing the plain password here.
            insert_query = f'INSERT INTO {TABLE_NAME2} (username, password) VALUES (%s, %s)'
            data = (username, password)
            cursor.execute(insert_query, data)
            connection.commit()
            print("User signed up successfully!")

        else:
            print("\tUsername and password cannot be empty..!!")

    except Exception as e:
        print(f'Error: {e}')

    finally:
        close_connection(connection)

if __name__ == "__main__":
    signup()