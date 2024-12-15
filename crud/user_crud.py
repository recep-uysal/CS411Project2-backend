import sqlite3

from config.encryption import Encrypter
from model.user_dto import new_user_dto

class UserCRUD:
    def __init__(self):
        self.db_path = "hospital_management.db"
        self.encrypter = Encrypter()

    def get_user_by_email(self, email: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT id, name, surname, email, role FROM user WHERE email = ?"
        cursor.execute(query, (self.encrypter.encode(email),))
        result = cursor.fetchone()  # Use fetchone for a single result
        connection.close()
        return result
    
    def add_user(self, new_user: new_user_dto):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
            INSERT INTO user (email, password, name, surname, role)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            self.encrypter.encode(new_user.email),
            self.encrypter.encode(new_user.password),
            self.encrypter.encode(new_user.name),
            self.encrypter.encode(new_user.surname),
            new_user.role,
        ))
        connection.commit()
        connection.close()


    def get_user_by_email_and_password(self, email: str, password: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT id, email, role FROM user WHERE email = ? AND password = ?"
        cursor.execute(query, (self.encrypter.encode(email), self.encrypter.encode(password)))
        result = cursor.fetchone()
        connection.close()
        return result

    def verify_user_code(self, email: str, code: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        query = "SELECT email, code FROM verification WHERE email = ? AND code = ?"
        cursor.execute(query, (self.encrypter.encode(email), code))
        result = cursor.fetchone()

        query_role = "SELECT role FROM user WHERE email = ?"
        cursor.execute(query_role, (self.encrypter.encode(email),))
        result_code = cursor.fetchone()
        
        combined_result = result + result_code
        connection.close()
        return combined_result

    def remove_user_code (self, email: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "DELETE FROM verification WHERE email = ?"
        cursor.execute(query, (self.encrypter.encode(email), ))
        result = cursor.fetchone()
        connection.close()
        return result

    def change_user_password(self, email: str, password: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = ("UPDATE user SET password = ? WHERE email = ?")
        cursor.execute(query, (self.encrypter.encode(password), self.encrypter.encode(email)))
        connection.commit()
        connection.close()