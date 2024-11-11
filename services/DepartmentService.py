from models.DepartmentModel import db, Department

class DepartmentService:
    
    @staticmethod
    def create_department(n_departamento, n_piso, direccion, n_telefono, disponibilidad):
        department = Department(
            n_departamento=n_departamento,
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
    def get_department_by_id(id_departamento):
        return Department.query.get(id_departamento)

    @staticmethod
    def update_disponibilidad(id_departamento, new_disponibilidad):
        department = Department.query.filter_by(id_departamento=id_departamento).first()
        
        if department:
            department.disponibilidad = new_disponibilidad
            db.session.commit()
            return department
        else:
            return None