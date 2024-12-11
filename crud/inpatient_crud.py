import sqlite3
import uuid
from datetime import date
class InpatientCRUD:
    def __init__(self):
        self.db_path = "hospital_management.db"

    def add_inpatient(self, inpatient):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        try:
            # Generate a unique inpatient ID
            inpatient_id = str(uuid.uuid4())

            # Check if the room is already occupied
            room_query = "SELECT status FROM room WHERE room_number = ?"
            cursor.execute(room_query, (inpatient.room_number,))
            room_status = cursor.fetchone()

            if not room_status:
                return {"error": "Room not found"}
            
            if room_status[0].lower() == "occupied":
                return {"error": "Room is already occupied"}

            department = "SELECT id, department_id FROM admission WHERE government_id = ?"
            cursor.execute(department, (inpatient.government_id,))
            patient_admission_id, department_id = cursor.fetchone()
            current_date = date.today()

            # Assign the room to the patient and mark it as occupied, check the department_id is matching
            update_room_query = "UPDATE room SET status = 'occupied', patient_id = ? WHERE room_number = ? AND department_id = ?"
            cursor.execute(update_room_query, (inpatient_id, inpatient.room_number, department_id))

            

            # Insert the new inpatient record
            insert_query = """
            INSERT INTO inpatient (id, patient_admission_id, department_id, room_number, entrance_date, discharge_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (
                inpatient_id,            # Unique inpatient ID
                patient_admission_id,    # Patient's admission ID
                department_id, # Department ID
                inpatient.room_number,   # Room number
                current_date, # Admission date
                None, # Discharge date
                "active"          # Inpatient status
            ))

            connection.commit()
            return {"message": "Inpatient added successfully", "inpatient_id": inpatient_id}

        except Exception as e:
            print(f"Database Error: {e}")
            return {"error": str(e)}
        finally:
            connection.close()

    def get_inpatient_by_id(self, patient_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM inpatient WHERE patient_id = ?"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    # get inpatient by inpatient id
    def get_inpatient_by_id(self, inpatient_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "SELECT * FROM inpatient WHERE inpatient_id = ?"
        cursor.execute(query, (inpatient_id,))
        result = cursor.fetchone()
        connection.close()
        return result

    def update_inpatient(self, id: str, inpatient):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # Step 1: Retrieve the current values from the database
        select_query = "SELECT room_number, entrance_date, discharge_date, status, department_id FROM inpatient WHERE id = ?"
        cursor.execute(select_query, (id,))
        current_values = cursor.fetchone()

        if not current_values:
            connection.close()
            return {"error": "Inpatient record not found"}

        current_data = {
            "room_number": current_values[0],
            "entrance_date": current_values[1],
            "discharge_date": current_values[2],
            "status": current_values[3],
            "department_id": current_values[4],  # Retrieve department_id for filtering
        }

        # Step 2: Validate room availability if a new room number is provided
        if inpatient.room_number and inpatient.room_number != current_data["room_number"]:
            room_check_query = """
            SELECT status 
            FROM room 
            WHERE room_number = ? AND department_id = ?
            """
            cursor.execute(room_check_query, (inpatient.room_number, current_data["department_id"]))
            room_status = cursor.fetchone()

            if not room_status:
                connection.close()
                return {"error": "Room not found"}
            if room_status[0].lower() == "occupied":
                connection.close()
                return {"error": "Room is already occupied"}

            # If the room is assignable, mark it as occupied
            update_room_query = """
            UPDATE room
            SET status = 'occupied',
                patient_id = ?
            WHERE room_number = ? AND department_id = ?
            """
            cursor.execute(update_room_query, (id, inpatient.room_number, current_data["department_id"]))

            # Free the previously assigned room
            free_room_query = """
            UPDATE room
            SET status = 'vacant',
                patient_id = NULL
            WHERE room_number = ? AND department_id = ?
            """
            cursor.execute(free_room_query, (current_data["room_number"], current_data["department_id"]))

        # Step 3: Merge old and new values
        updated_data = {
            "room_number": inpatient.room_number if inpatient.room_number is not None else current_data["room_number"],
            "entrance_date": inpatient.entrance_date if inpatient.entrance_date is not None else current_data["entrance_date"],
            "discharge_date": inpatient.discharge_date if inpatient.discharge_date is not None else current_data["discharge_date"],
            "status": inpatient.status if inpatient.status is not None else current_data["status"],
        }

        # Step 4: Update the inpatient record
        update_query = """
        UPDATE inpatient
        SET room_number = ?,
            entrance_date = ?,
            discharge_date = ?,
            status = ?
        WHERE id = ?
        """
        cursor.execute(update_query, (
            updated_data["room_number"],
            updated_data["entrance_date"],
            updated_data["discharge_date"],
            updated_data["status"],
            id,
        ))

        connection.commit()
        connection.close()
        return {"message": "Inpatient updated successfully"}



    
    def delete_inpatient(self, id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        # Step 1: Retrieve the assigned room for the inpatient
        room_query = "SELECT room_number, department_id FROM inpatient WHERE id = ?"
        cursor.execute(room_query, (id,))
        assigned_room = cursor.fetchone()

        if not assigned_room:
            connection.close()
            return {"error": "Inpatient record not found"}

        room_number, department_id = assigned_room

        # Step 2: Free the assigned room
        free_room_query = """
        UPDATE room
        SET status = 'vacant',
            patient_id = NULL
        WHERE room_number = ? AND department_id = ?
        """
        cursor.execute(free_room_query, (room_number, department_id))

        # Step 3: Delete the inpatient record
        delete_query = "DELETE FROM inpatient WHERE id = ?"
        cursor.execute(delete_query, (id,))

        connection.commit()
        connection.close()

        return {"message": "Inpatient deleted successfully and room freed"}

    
    
    # get all inpatients. also fetch the admission details. patient_admission_id is the foreign key to admission table's id. also reference to department table by inpatient's department_id and department table's id.
    def get_all_inpatients(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        SELECT inpatient.*, admission.*, department.name
        FROM inpatient
        JOIN admission ON inpatient.patient_admission_id = admission.id
        JOIN department ON inpatient.department_id = department.id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result   

    

    def get_all_inpatients_by_government_id(self, government_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        print(f"Checking government_id: {government_id}")
        
        # Debug: Check if the government_id exists in the admission table
        cursor.execute("SELECT id FROM admission WHERE government_id = ?", (government_id,))
        admission_ids = cursor.fetchall()
        print(f"Admission IDs for government_id {government_id}: {admission_ids}")
        
        # Debug: Check if any inpatient records match these admission IDs
        for admission_id in admission_ids:
            cursor.execute("SELECT * FROM inpatient WHERE patient_admission_id = ?", (admission_id[0],))
            inpatient_records = cursor.fetchall()
            print(f"Inpatient records for admission_id {admission_id[0]}: {inpatient_records}")

        # Actual query
        query = """
        SELECT inpatient.*
        FROM inpatient
        JOIN admission ON inpatient.patient_admission_id = admission.id
        WHERE admission.government_id = ?
        """
        cursor.execute(query, (government_id,))
        result = cursor.fetchall()
        print(f"Final Query Result: {result}")
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
    
    
    def discharge_inpatient(self, inpatient_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()

                # Step 1: Retrieve the assigned room for the inpatient
                room_query = "SELECT room_number, department_id FROM inpatient WHERE id = ?"
                cursor.execute(room_query, (inpatient_id,))
                assigned_room = cursor.fetchone()

                if not assigned_room:
                    return {"error": "Inpatient record not found"}

                room_number, department_id = assigned_room

                # Step 2: Free the assigned room
                free_room_query = """
                UPDATE room
                SET status = 'vacant',
                    patient_id = NULL
                WHERE room_number = ? AND department_id = ?
                """
                cursor.execute(free_room_query, (room_number, department_id))

                # Step 3: Discharge the inpatient
                discharge_query = """
                UPDATE inpatient
                SET discharge_date = CURRENT_TIMESTAMP,
                    status = 'discharged'
                WHERE id = ?
                """
                cursor.execute(discharge_query, (inpatient_id,))

                connection.commit()
            return {"message": "Inpatient discharged successfully and room freed"}

        except sqlite3.OperationalError as e:
            return {"error": f"Database operation failed: {str(e)}"}


    # update department, room and status of inpatient. first check if the new room is available. if available, update the room assignment and free the previously assigned room. then update the inpatient record. finally, find and update the admission record.
    def update_department_room_status(self, inpatient_id, update):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()

                # Step 1: Retrieve the current values from the database
                select_query = "SELECT room_number, department_id FROM inpatient WHERE id = ?"
                cursor.execute(select_query, (inpatient_id,))
                current_values = cursor.fetchone()

                if not current_values:
                    return {"error": "Inpatient record not found"}

                current_data = {
                    "room_number": current_values[0],
                    "department_id": current_values[1],
                }

                # Step 2: Validate room availability if a new room number is provided
                if update.room_number and update.room_number != current_data["room_number"]:
                    room_check_query = """
                    SELECT status 
                    FROM room 
                    WHERE room_number = ? AND department_id = ?
                    """
                    cursor.execute(room_check_query, (update.room_number, update.department_id))
                    room_status = cursor.fetchone()

                    if not room_status:
                        return {"error": "Room not found"}
                    if room_status[0].lower() == "occupied":
                        return {"error": "Room is already occupied"}

                    # If the room is assignable, mark it as occupied
                    update_room_query = """
                    UPDATE room
                    SET status = 'occupied',
                        patient_id = ?
                    WHERE room_number = ? AND department_id = ?
                    """
                    cursor.execute(update_room_query, (inpatient_id, update.room_number, update.department_id))

                    # Free the previously assigned room
                    free_room_query = """
                    UPDATE room
                    SET status = 'vacant',
                        patient_id = NULL
                    WHERE room_number = ? AND department_id = ?
                    """
                    cursor.execute(free_room_query, (current_data["room_number"], current_data["department_id"]))

                # Step 3: Update the inpatient record
                update_query = """
                UPDATE inpatient
                SET room_number = ?,
                    department_id = ?,
                    status = ?
                WHERE id = ?
                """
                cursor.execute(update_query, (
                    update.room_number,
                    update.department_id,
                    update.status,
                    inpatient_id,
                ))

                # Step 4: Update the admission record
                admission_update_query = """
                UPDATE admission
                SET department_id = ?
                WHERE id = (
                    SELECT patient_admission_id
                    FROM inpatient
                    WHERE id = ?
                )
                """
                cursor.execute(admission_update_query, (update.department_id, inpatient_id))

                connection.commit()
            return {"message": "Inpatient department and room updated successfully"}
        
        except sqlite3.OperationalError as e:
            return {"error": f"Database operation failed: {str(e)}"}
        
