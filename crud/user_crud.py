# dal/user_crud.py
import os
import sqlite3
from model.user_dto import new_user_dto

class UserCRUD:
    def __init__(self):
        self.db_path = "hospital_management.db"

    def get_user_by_email(self, email: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT id, name, surname, email, role FROM user WHERE email = ?"
        cursor.execute(query, (email,))
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
            new_user.email,
            new_user.password,
            new_user.name,
            new_user.surname,
            new_user.role,
        ))
        connection.commit()
        connection.close()


    def get_user_by_email_and_password(self, email: str, password: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT id, email, role FROM user WHERE email = ? AND password = ?"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        connection.close()
        return result

    def verify_user_code(self, email: str, code: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT email, code FROM verification WHERE email = ? AND code = ?"
        cursor.execute(query, (email, code))
        result = cursor.fetchone()
        connection.close()
        return result

    def remove_user_code (self, email: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "DELETE FROM verification WHERE email = ?"
        cursor.execute(query, (email, ))
        result = cursor.fetchone()
        connection.close()
        return result

    def change_user_password(self, email: str, password: str):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = ("UPDATE user SET password = ? WHERE email = ?")
        cursor.execute(query, (password, email))
        connection.commit()
        connection.close()