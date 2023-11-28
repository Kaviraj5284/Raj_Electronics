from config.db_operation import connect_to_database, create_cursor, close_connection
from config.config import TABLE_NAME1

def Booking():
    try:
        connection = connect_to_database()
        cursor = create_cursor(connection)
        print("Connection to the database successful!!")
        cursor.execute(f'SELECT * FROM {TABLE_NAME1}')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Exception as e:
        print(f'Error: {e}')

    # cursor.execute(f'Select * from {TABLE_NAME1}')

Booking()