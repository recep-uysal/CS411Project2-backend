import sqlite3

def initialize_database():
    connection = sqlite3.connect("hospital_management.db")
    cursor = connection.cursor()

    # Create the user table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            role TEXT NOT NULL
        );
    """)

    # Create admission table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admission (
        id TEXT PRIMARY KEY,
        government_id TEXT UNIQUE,
        patient_name TEXT,
        patient_surname TEXT,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        address TEXT,
        admitted_on TEXT,
        insurance TEXT,
        department_id INTEGER
    )
    """)

    # Create inpatient table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inpatient (
        id TEXT PRIMARY KEY,
        patient_admission_id TEXT,
        department_id INTEGER,
        room_number INTEGER,
        entrance_date TEXT,
        discharge_date TEXT,
        status TEXT
    )
    """)

    # Create table for the clinic departments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT
    )
    """)

    # Create table for the department rooms
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS room (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_id INTEGER,
        room_number INTEGER,
        status TEXT,
        patient_id INTEGER
    )
    """)

    # Create table for the department staff
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        department_id INTEGER
    )
    """)

    # Create table for the clinic departments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS verification (
        email TEXT NOT NULL,
        code TEXT NOT NULL
    )
    """)

    connection.commit()

    # Check if departments already exist
    cursor.execute("SELECT COUNT(*) FROM department")
    department_count = cursor.fetchone()[0]

    if department_count == 0:
        # Add departments if none exist
        departments = [
            ("Cardiology", "Handles heart-related issues"),
            ("Neurology", "Focuses on brain and nervous system disorders"),
            ("Orthopedics", "Deals with bone and muscle issues")
        ]
        cursor.executemany("INSERT INTO department (name, description) VALUES (?, ?)", departments)
        print("Departments added.")

    # Check if rooms already exist
    cursor.execute("SELECT COUNT(*) FROM room")
    room_count = cursor.fetchone()[0]

    if room_count == 0:
        # Add 5 rooms for each department if none exist
        for department_id in range(1, 4):  # Assuming department IDs start from 1
            rooms = [(department_id, i, "vacant", None) for i in range(1, 6)]
            cursor.executemany("INSERT INTO room (department_id, room_number, status, patient_id) VALUES (?, ?, ?, ?)", rooms)
        print("Rooms added.")

    connection.commit()
    connection.close()

    print("Database initialized.")
