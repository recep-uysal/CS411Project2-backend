import sqlite3
import uuid

class AdmissionCRUD:
    def __init__(self):
        self.db_path = "hospital_management.db"

    def add_admission(self, admission):
        try:
            # Generate a specific ID for the admission
            admission_id = str(uuid.uuid4())  # Generate a unique ID as a string
            
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            
            # Query to insert into the updated schema
            query = """
            INSERT INTO admission (
                id, 
                government_id,
                patient_name, 
                patient_surname, 
                age, 
                gender, 
                contact, 
                address, 
                admitted_on, 
                insurance,
                department_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            # Execute the query with all fields
            cursor.execute(query, (
                admission_id,           # id
                admission.government_id,        # government_id
                admission.patient_name,         # patient_name
                admission.patient_surname,      # patient_surname
                admission.age,          # age
                admission.gender,       # gender
                admission.contact,      # contact
                admission.address,      # address
                admission.admitted_on,  # admitted_on time
                admission.insurance,        # reason
                admission.department_id # department_id
            ))
            
            connection.commit()
            connection.close()
            
            return {
                "message": "Patient admitted successfully",
                "admission_id": admission_id
            }
        except Exception as e:
            print(f"Database Error: {e}")
            raise

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

    def update_admission(self, admission_id, admission):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        # Retrieve the current values from the database
        select_query = "SELECT * FROM admission WHERE id = ?"
        cursor.execute(select_query, (admission_id,))
        current_admission = cursor.fetchone()
        
        if not current_admission:
            connection.close()
            return {"error": "Admission record not found"}

        # Map the current database values
        current_data = {
            "government_id": current_admission[1],
            "patient_name": current_admission[2],
            "patient_surname": current_admission[3],
            "age": current_admission[4],
            "gender": current_admission[5],
            "contact": current_admission[6],
            "address": current_admission[7],
            "admitted_on": current_admission[8],
            "insurance": current_admission[9],
            "department_id": current_admission[10]
        }

        # Use new values if provided; otherwise, keep old ones
        updated_data = {
        "patient_name": admission.patient_name or current_data["patient_name"],
        "patient_surname": admission.patient_surname or current_data["patient_surname"],
        "age": admission.age or current_data["age"],
        "gender": admission.gender or current_data["gender"],
        "contact": admission.contact or current_data["contact"],
        "address": admission.address or current_data["address"],
        "insurance": admission.insurance or current_data["insurance"],
        "department_id": admission.department_id or current_data["department_id"]
        }

        # Perform the update with the merged data
        update_query = """
        UPDATE admission
        SET patient_name = ?,
        patient_surname = ?,
        age = ?,
        gender = ?,
        contact = ?,
        address = ?,
        insurance = ?,
        department_id = ?
        WHERE id = ?
        """
        cursor.execute(update_query, (
        updated_data["patient_name"],
        updated_data["patient_surname"],
        updated_data["age"],
        updated_data["gender"],
        updated_data["contact"],
        updated_data["address"],
        updated_data["insurance"],
        updated_data["department_id"],
        admission_id
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
    def get_patient_admissions(self, government_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM admission WHERE government_id = ?"
        cursor.execute(query, (government_id,))
        result = cursor.fetchall()
        connection.close()
        return result


    # define a method to get all admissions for a department
    def get_department_admissions(self, department_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM admission WHERE department_id = ?"
        cursor.execute(query, (department_id,))
        result = cursor.fetchall()
        connection.close()
        return result
