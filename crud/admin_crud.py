# dal/user_crud.py
import os
import sqlite3
from model.user_dto import UserDtoForAdmin, new_user_dto

class AdminCRUD:
    def __init__(self):
        self.db_path = "hospital_management.db"

    def get_all_users(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT id, name, surname, email, role FROM user"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        
        users = [UserDtoForAdmin(
            id=str(row[0]),
            name=row[1],
            surname=row[2],
            email=row[3],
            role=row[4]
        ) for row in result]

        return users
    
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
