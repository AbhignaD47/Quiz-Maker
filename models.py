from database import get_db_connection

class User:
    @staticmethod
    def register(username, password):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def login(username, password):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user

class Quiz:
    @staticmethod
    def create_quiz(user_id, title):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO quizzes (user_id, title) VALUES (%s, %s)", (user_id, title))
        connection.commit()
        quiz_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return quiz_id
