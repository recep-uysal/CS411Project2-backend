import sqlite3

class AdmissionCRUD:
    def __init__(self):
        self.db_path = "healthcare.db"

    def add_admission(self, admission):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        INSERT INTO admission (patient_name, age, gender, contact, address, admitted_on, reason)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            admission.patient_name,
            admission.age,
            admission.gender,
            admission.contact,
            admission.address,
            admission.admitted_on,
            admission.reason,
        ))
        connection.commit()
        connection.close()
        return {"message": "Patient admitted successfully"}

    def get_all_admissions(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM admission"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
