
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'smartcapi_pwa'

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    print(f"Database '{DB_NAME}' created or already exists.")
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
