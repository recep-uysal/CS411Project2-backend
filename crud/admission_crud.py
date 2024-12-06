import sqlite3

class AdmissionCRUD:
    def __init__(self):
        self.db_path = "healthcare.db"

    def add_admission(self, admission):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        INSERT INTO admission (patient_name, age, gender, contact, address, admitted_on, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            admission.patient_name,
            admission.age,
            admission.gender,
            admission.contact,
            admission.address,
            admission.admitted_on,
            admission.description,
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

    def get_admission(self, admission_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM admission WHERE id = ?"
        cursor.execute(query, (admission_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    # define a method to update an admission record
    def update_admission(self, admission_id, admission):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        UPDATE admission
        SET patient_name = ?,
            age = ?,
            gender = ?,
            contact = ?,
            address = ?,
            admitted_on = ?,
            description = ?
        WHERE id = ?
        """
        cursor.execute(query, (
            admission.patient_name,
            admission.age,
            admission.gender,
            admission.contact,
            admission.address,
            admission.admitted_on,
            admission.description,
            admission_id,
        ))

        connection.commit()
        connection.close()
        return {"message": "Admission updated successfully"}
    

    # define a method to delete an admission record
    def delete_admission(self, admission_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "DELETE FROM admission WHERE id = ?"
        cursor.execute(query, (admission_id,))
        connection.commit()
        connection.close()
        return {"message": "Admission deleted successfully from the database"}
    

   
    # define a method to get all admissions for a patient
    def get_patient_admissions(self, patient_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM admission WHERE patient_id = ?"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchall()
        connection.close()
        return result
