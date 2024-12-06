import sqlite3

def initialize_database():
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()

    # Create the user table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            role TEXT NOT NULL,
            verified BOOLEAN DEFAULT 0
        );
    """)

    # Create admission table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admission (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        address TEXT,
        admitted_on TEXT,
        reason TEXT
    )
    """)

    # Create inpatient table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inpatient (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        department_id INTEGER,
        room_number TEXT,
        admission_date TEXT,
        discharge_date TEXT,
        status TEXT
    )
    """)

    # create table for the clinic departments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT
    )
    """)

    # create table for the department rooms. Each room belongs to a department and has a room number. also has a status, which can be either "occupied" or "vacant". als, patient_id field to reference inpateint table. it can be null if the room is vacant.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS room (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_id INTEGER,
        room_number TEXT,
        status TEXT,
        patient_id INTEGER
    )
    """)


    # create table for the department staff. they are users who are assigned to a department. use user_id to reference the user table, and department_id to reference the department table.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        department_id INTEGER
    )
    """)


    connection.commit()
    connection.close()
