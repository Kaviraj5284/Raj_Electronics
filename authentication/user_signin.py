# signin.py

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


def signin():
    try:
        connection = connect_to_database()
        cursor = create_cursor(connection)
        print("Connection to the database successful!!")

        create_table_if_not_exists(cursor)

        username = str(input("Username: "))
        password = str(input("Password: "))

        if username != "" and password != "":
            select_query = f'SELECT * FROM {TABLE_NAME2} WHERE username = %s AND password = %s'
            data = (username, password)
            cursor.execute(select_query, data)

            user = cursor.fetchone()

            if user:
                # Generate JWT token
                token = jwt.encode({"username": username},
                                   SECRET_KEY, algorithm="HS256")
                print("User signed in successfully!")
                print(f'Token: {token}')
            else:
                print("Invalid username or password.")

        else:
            print("\tUsername and password cannot be empty..!!")

    except Exception as e:
        print(f'Error: {e}')

    finally:
        close_connection(connection)


if __name__ == "__main__":
    signin()
