import sqlite3

class InpatientCRUD:
    def __init__(self):
        self.db_path = "healthcare.db"

    def add_inpatient(self, inpatient):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        INSERT INTO inpatient (patient_id, room_number, admission_date, discharge_date, status)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            inpatient.patient_id,
            inpatient.room_number,
            inpatient.admission_date,
            inpatient.discharge_date,
            inpatient.status,
        ))
        connection.commit()
        connection.close()
        return {"message": "Inpatient added successfully"}

    def get_inpatient_by_id(self, patient_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM inpatient WHERE patient_id = ?"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()
        connection.close()
        return result
