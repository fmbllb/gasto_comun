from services.DepartmentService import DepartmentService

class DepartmentController:    
    @staticmethod
    def create_department_controller(department_id, floor, address, phone_number, availability):        
        return DepartmentService.create_user(
            department_id, floor, address, 
            phone_number, availability)
            
    @staticmethod
    def get_department_controller():        
        return DepartmentService.get_all_departments()
    
    @staticmethod
    def get_department_by_id_controller(department_id):
        return DepartmentService.get_department_by_id(department_id)