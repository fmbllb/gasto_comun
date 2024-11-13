from models.DepartmentModel import asociar_facturas_a_departamento, db, Department
from models.PaymentHistoryModel import EstadoDeuda, PaymentHistory

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
        asociar_facturas_a_departamento(department.id_departamento)
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
    
    @staticmethod
    def registrar_pago(id_departamento, id_gasto, precio_pago, estado_deuda):
        # Buscar la entrada en PaymentHistory
        payment_history_entry = PaymentHistory.query.filter_by(
            idDepartamento=id_departamento,
            idGasto=id_gasto
        ).first()
        # Si el registro no existe, simplemente retornar None para que la vista maneje el error
        if not payment_history_entry:
            return None
        # Actualizar el monto pagado
        payment_history_entry.monto_pagado += precio_pago
        # Cambiar el estado de la deuda si está completamente pagada
        if payment_history_entry.monto_pagado >= payment_history_entry.precio_total:
            payment_history_entry.estado_deuda = EstadoDeuda.PAGADO
        else:
            # Mantener el estado actual o actualizarlo a un estado parcial si es necesario
            payment_history_entry.estado_deuda = estado_deuda
        # Confirmar los cambios en la base de datos
        db.session.commit()

        return payment_history_entry  # Devolver el objeto actualizado para que la vista pueda utilizarlo si es necesario