# dal/user_crud.py
import os
import sqlite3

from config.email_authenticator import encrypter
from config.encryption import Encrypter
from model.user_dto import UserDtoForAdmin

class AdminCRUD:
    def __init__(self):
        self.db_path = "hospital_management.db"
        self.encrypter = Encrypter()

    def get_all_users(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT id, name, surname, email, role FROM user WHERE role <> 'admin'"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        
        users = [UserDtoForAdmin(
            id=str(row[0]),
            name=encrypter.decode(row[1]),
            surname=encrypter.decode(row[2]),
            email=encrypter.decode(row[3]),
            role=row[4]
        ) for row in result]

        return users
    
    def update_user(self, id, user:UserDtoForAdmin):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # Retrieve the current values from the database
        select_query_user = "SELECT * FROM user WHERE id = ?"
        cursor.execute(select_query_user, (id,))
        current_user = cursor.fetchone()
        
        
        if not current_user:
            connection.close()
            return {"error": "User record not found"}
        
        old_email = current_user[1]

        select_query_verify = "SELECT * from verification WHERE email = ?"
        cursor.execute(select_query_verify, (old_email,))
        verification = cursor.fetchone()
        
        update_query_user = """
        UPDATE user
        SET name = ?,
        surname = ?,
        email = ?,
        role = ?
        WHERE id = ?
        """
        cursor.execute(update_query_user, (
        encrypter.encode(user.name),
        encrypter.encode(user.surname),
        encrypter.encode(user.email),
        user.role,
        id
        ))
        
        if verification:
            update_query_verify = """
            UPDATE verification
            SET email = ?
            WHERE email = ?
            """
            cursor.execute(update_query_verify, (
            encrypter.encode(user.email),
            encrypter.encode(old_email)
            ))
        
        connection.commit()
        connection.close()
        return {"message": "User updated successfully"}
    
    def delete_user(self, id, email):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        query_user = "DELETE FROM user WHERE id = ?"
        cursor.execute(query_user, (id, ))

        query_verification = "DELETE FROM verification WHERE email = ?"
        cursor.execute(query_verification, (encrypter.encode(email), ))

        connection.commit()
        connection.close()
        return True
