import smtplib
import sqlite3
from email.message import EmailMessage
import random

db_path = "hospital_management.db"

def generate_otp(length=6):
    return ''.join(random.choices('0123456789', k=length))

def send_verification_email(receiver_email: str):
    sender_email = "lhospital411@gmail.com"
    sender_password = "monmkuchwtujkyfe"

    otp = generate_otp()
    msg = EmailMessage()
    msg.set_content(f"Your verification code is: {otp}")
    msg['Subject'] = "LHOSPITAL VERIFICATION MAIL"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    delete_old_verification_code(receiver_email)
    save_verification_code(receiver_email, otp)

def save_verification_code(email:str, code: str):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    query = """
                INSERT INTO verification (email, code)
                VALUES (?, ?)
            """
    cursor.execute(query, (
        email,
        code,
    ))
    connection.commit()
    connection.close()

def delete_old_verification_code(email:str):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    query = """
                DELETE FROM verification
                WHERE email = ?
            """
    cursor.execute(query, (
        email,
    ))
    connection.commit()
    connection.close()
