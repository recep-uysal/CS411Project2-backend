from crud.inpatient_crud import InpatientCRUD
from model.inpatient_dto import InpatientDTO

class InpatientService:
    def __init__(self):
        self.inpatient_crud = InpatientCRUD()

    def add_inpatient(self, inpatient: InpatientDTO):
        return self.inpatient_crud.add_inpatient(inpatient)

    def get_inpatient(self, patient_id: int):
        return self.inpatient_crud.get_inpatient_by_id(patient_id)

    def update_inpatient(self, patient_id: int, inpatient: InpatientDTO):
        return self.inpatient_crud.update_inpatient(patient_id, inpatient)

    def delete_inpatient(self, patient_id: int):
        return self.inpatient_crud.delete_inpatient(patient_id)
    
    def get_all_inpatients(self):
        return self.inpatient_crud.get_all_inpatients()
    
    def get_all_inpatients_by_user(self, user_id: int):
        return self.inpatient_crud.get_all_inpatients_by_user(user_id)
    
    def get_all_inpatients_by_department(self, department_id: int):
        return self.inpatient_crud.get_all_inpatients_by_department(department_id)
    
    def delete_all_inpatients(self):
        return self.inpatient_crud.delete_all_inpatients()
