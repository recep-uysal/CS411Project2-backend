from crud.admission_crud import AdmissionCRUD
from model.admission_dto import AdmissionDTO, UpdateAdmissionDTO

class AdmissionService:
    def __init__(self):
        self.admission_crud = AdmissionCRUD()

    def admit_patient(self, admission: AdmissionDTO):
        return self.admission_crud.add_admission(admission)

    def list_admissions(self):
        return self.admission_crud.get_all_admissions()

    def get_admission(self, admission_id):
        return self.admission_crud.get_admission(admission_id)
    
    def update_admission(self, admission_id, admission: UpdateAdmissionDTO):
        self.admission_crud.update_admission(admission_id, admission)

    def delete_admission(self, admission_id):
        self.admission_crud.delete_admission(admission_id)

    def get_patient_admissions(self, government_id):
        return self.admission_crud.get_patient_admissions(government_id)
        

    def get_department_admissions(self, department_id):
        return self.admission_crud.get_department_admissions(department_id)
