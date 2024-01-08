import os

class Config:
    # SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DB_CONFIG = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '12345',
        'database': 'ELECTRONICS',
    }

    TABLE_NAME1 = 'user_data'
    TABLE_NAME2 = 'user_auth_data'
    TABLE_NAME3 = 'jwt_token'
    SECRET_KEY = 'kavirajElectronics'