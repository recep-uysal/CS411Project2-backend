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
        query = "SELECT id, name, surname, email, role FROM user WHERE role <> 'admin'"
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
    
    def delete_user(self, id, email):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        query_user = "DELETE FROM user WHERE id = ?"
        cursor.execute(query_user, (id, ))

        query_verification = "DELETE FROM verification WHERE email = ?"
        cursor.execute(query_verification, (email, ))

        connection.commit()
        connection.close()
        return True
