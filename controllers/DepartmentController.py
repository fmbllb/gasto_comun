from services.DepartmentService import DepartmentService

class DepartmentController:    
    @staticmethod
    def create_department_controller(n_departamento, n_piso,
                                    direccion, n_telefono, disponibilidad):  
        
        return DepartmentService.create_department(n_departamento, n_piso, direccion,
                                                    n_telefono, disponibilidad)
            
    @staticmethod
    def get_department_controller():        
        return DepartmentService.get_all_departments()
    
    @staticmethod
    def get_department_by_id_controller(id_departamento):
        return DepartmentService.get_department_by_id(id_departamento)
    
    @staticmethod
    def update_disponibilidad_controller(id_departamento, new_disponibilidad):
        return DepartmentService.update_disponibilidad(id_departamento, new_disponibilidad)
    
    @staticmethod
    def registrar_pago_controller(id_departamento, id_gasto, monto_pagado, fecha_pago):
        return DepartmentService.registrar_pago(id_departamento, id_gasto, monto_pagado, fecha_pago)

        
        return DepartmentService.registrar_pago(id_departamento, id_gasto, 
                                                fecha_emision, precio_pago, estado_deuda)