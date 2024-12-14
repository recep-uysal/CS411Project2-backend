from crud.inpatient_crud import InpatientCRUD
from model.inpatient_dto import InpatientDTO, InpatientAddDTO
from model.inpatient_dto import updateDTO

class InpatientService:
    def __init__(self):
        self.inpatient_crud = InpatientCRUD()

    def add_inpatient(self, inpatient: InpatientAddDTO):
        return self.inpatient_crud.add_inpatient(inpatient)

    def get_inpatient(self, inpatient_id):
        return self.inpatient_crud.get_inpatient_by_id(inpatient_id)

    def update_inpatient(self, inpatient_id: str, inpatient: InpatientDTO):
        return self.inpatient_crud.update_inpatient(inpatient_id, inpatient)

    def delete_inpatient(self, inpatient_id):
        return self.inpatient_crud.delete_inpatient(inpatient_id)
    
    def get_all_inpatients(self):
        return self.inpatient_crud.get_all_inpatients()
    
    def get_all_inpatients_by_government_id(self, government_id: int):
        return self.inpatient_crud.get_all_inpatients_by_government_id(government_id)
    
    def get_all_inpatients_by_department(self, department_id: int):
        return self.inpatient_crud.get_all_inpatients_by_department(department_id)
    
    def delete_all_inpatients(self):
        return self.inpatient_crud.delete_all_inpatients()

    def discharge_inpatient(self, inpatient_id):
        return self.inpatient_crud.discharge_inpatient(inpatient_id)

    def update_department_room_status(self, inpatient_id: str, update: updateDTO):
        return self.inpatient_crud.update_department_room_status(inpatient_id, update)

    # get all rooms in the system
    def get_all_rooms(self):
        return self.inpatient_crud.get_all_rooms() 
