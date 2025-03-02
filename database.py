import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='quiz_app'
    )
    return connection
