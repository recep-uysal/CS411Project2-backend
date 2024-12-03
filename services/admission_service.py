from crud.admission_crud import AdmissionCRUD
from model.admission_dto import AdmissionDTO

class AdmissionService:
    def __init__(self):
        self.admission_crud = AdmissionCRUD()

    def admit_patient(self, admission: AdmissionDTO):
        return self.admission_crud.add_admission(admission)

    def list_admissions(self):
        return self.admission_crud.get_all_admissions()
