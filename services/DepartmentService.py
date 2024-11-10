from models.DepartmentModel import db, Department

class DepartmentService:
    
    @staticmethod
    def create_department(id_departmento, n_piso, direccion, n_telefono, disponibilidad):
        department = Department(
            id_departmento=id_departmento,
            n_piso=n_piso,
            direccion=direccion,
            n_telefono=n_telefono,
            disponibilidad=disponibilidad
        )
        db.session.add(department)
        db.session.commit()
        return department 
        
    @staticmethod
    def get_all_departments():
        return Department.query.all()        
    
    @staticmethod
    def get_department_by_id(id_departmento):
        return Department.query.get(id_departmento)
