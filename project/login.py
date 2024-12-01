import os
import sqlite3
from fastapi import APIRouter
from model.user_dto import user_dto

login_router = APIRouter()

USER_TABLE = "data"
USER_DB_FILE = "user.db"


@login_router.post("/checkPassword")
def checkPassword(user:user_dto):
    db_file = os.path.join(USER_TABLE, USER_DB_FILE)
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, user FROM user WHERE user = '{user.user_name}' and password = '{user.password}'")
    result = cursor.fetchall()
    connection.close()
    return result