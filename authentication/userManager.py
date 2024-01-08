import jwt
import bcrypt
import datetime
from config.config import Config
from config.db_operation import connect_to_database, create_cursor, close_connection

class UserManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __connect_to_database(self):
        try:
            self.connection = connect_to_database()
            self.cursor = create_cursor(self.connection)
            print('Connection to the database is established!!')
        except Exception as e:
            print(f'Error connecting to the database: {e}')
            raise e

    def __close_connection(self):
        close_connection(self.connection)

    def __create_table_if_not_exists(self):
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {Config.TABLE_NAME2} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
        '''
        self.cursor.execute(create_table_query)
    
    def __create_token_table_if_not_exists(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS user_tokens (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            token VARCHAR(255) NOT NULL,
            expiration_date DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        '''
        self.cursor.execute(create_table_query)

    def __hash_password(self,password):
        salt = bcrypt.gensalt(10)
        hashed_password = bcrypt.hashpw(password.encode('utf8'),salt)
        return hashed_password.decode('utf8')

    def __generate_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
        return token.decode('utf8')

    def __store_token(self, user_id, token):
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        insert_token_query = 'INSERT INTO user_token (user_id, token, expiration_date) VALUES (%s, %s, %s)'
        data = (user_id, token, expiration_date)
        self.cursor.execute(insert_token_query, data)
        self.connection.commit()

    def signup(self):
        try:
            self.__connect_to_database()
            self.__create_table_if_not_exists()
            self.__create_token_table_if_not_exists()


            username = str(input("Enter your username: "))
            password = str(input("Enter your password: "))

            if username != "" and password != "":
                hashed_password = self._hash_password(password)
                insert_query = f'INSERT INTO {Config.TABLE_NAME2} (username, password_hash) VALUES (%s, %s)'
                data = (username,hashed_password)
                self.cursor.execute(insert_query,data)
                self.connection.commit()
                print("User signed up successfully")
            
            else:
                print("\tUsername and password cannot be empty")
        except Exception as e:
                print(f'Error in creating user: {e}')

        finally:
            self._close_connection()