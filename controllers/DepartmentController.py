from services.DepartmentService import DepartmentService

class DepartmentController:    
    @staticmethod
    def create_department_controller(id_departamento, 
        n_departamento, n_piso, direccion, n_telefono, 
        disponibilidad):        
        return DepartmentService.create_department(
            id_departamento, n_departamento, n_piso, 
            direccion, n_telefono, disponibilidad)
            
    @staticmethod
    def get_department_controller():        
        return DepartmentService.get_all_departments()
    
    @staticmethod
    def get_department_by_id_controller(id_departamento):
        return DepartmentService.get_department_by_id(id_departamento)