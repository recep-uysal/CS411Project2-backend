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

    def update_inpatient(self, patient_id, inpatient):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        UPDATE inpatient
        SET room_number = ?,
            admission_date = ?,
            discharge_date = ?,
            status = ?
        WHERE patient_id = ?
        """
        cursor.execute(query, (
            inpatient.room_number,
            inpatient.admission_date,
            inpatient.discharge_date,
            inpatient.status,
            patient_id,
        ))
        connection.commit()
        connection.close()
        return {"message": "Inpatient updated successfully"}
    
    def delete_inpatient(self, patient_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "DELETE FROM inpatient WHERE patient_id = ?"
        cursor.execute(query, (patient_id,))
        connection.commit()
        connection.close()
        return {"message": "Inpatient deleted successfully"}
    
    def get_all_inpatients(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM inpatient"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    

    def get_all_inpatients_by_user(self, user_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        SELECT inpatient.*
        FROM inpatient
        JOIN room ON inpatient.room_number = room.room_number
        JOIN staff ON room.department_id = staff.department_id
        WHERE staff.user_id = ?
        """
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        connection.close()
        return result
    
    def get_all_inpatients_by_department(self, department_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        SELECT inpatient.*
        FROM inpatient
        JOIN room ON inpatient.room_number = room.room_number
        WHERE room.department_id = ?
        """
        cursor.execute(query, (department_id,))
        result = cursor.fetchall()
        connection.close()
        return result
    
    def delete_all_inpatients(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "DELETE FROM inpatient"
        cursor.execute(query)
        connection.commit()
        connection.close()
        return {"message": "All inpatients deleted successfully"}
    
    
