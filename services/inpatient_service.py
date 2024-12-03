from crud.inpatient_crud import InpatientCRUD
from model.inpatient_dto import InpatientDTO

class InpatientService:
    def __init__(self):
        self.inpatient_crud = InpatientCRUD()

    def add_inpatient(self, inpatient: InpatientDTO):
        return self.inpatient_crud.add_inpatient(inpatient)

    def get_inpatient(self, patient_id: int):
        return self.inpatient_crud.get_inpatient_by_id(patient_id)
