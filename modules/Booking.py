from config.db_operation import connect_to_database, create_cursor, close_connection
from config.config import TABLE_NAME1

def create_table_if_not_exists(cursor):
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME1} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone_number BIGINT NOT NULL,
        address VARCHAR(255) NOT NULL
    )
    '''
    cursor.execute(create_table_query)

def Booking():
    try:
        connection = connect_to_database()
        cursor = create_cursor(connection)
        print("Connection to the database successful!!")

        create_table_if_not_exists(cursor)
        name = str(input("Name: "))
        phone_number = int(input("Phone Number: "))
        address = str(input("Address: "))
        if name != "" and phone_number != 0 and address != "":
            insert_query = f'INSERT INTO {TABLE_NAME1} (name, phone_number, address) VALUES (%s, %s, %s)'
            data = (name, phone_number, address)
            cursor.execute(insert_query, data)
            connection.commit()
            print("Data inserted successfully!")
        else:
            print("\tName, Phone no. & Address cannot be empty..!!")
        
    except Exception as e:
        print(f'Error: {e}')

    finally:
        close_connection(connection)