from models.DepartmentModel import asociar_facturas_a_departamento, db, Department
from models.PaymentHistoryModel import EstadoDeuda, PaymentHistory
from datetime import datetime

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
    def registrar_pago(id_departamento, id_gasto, monto_pagado, fecha_pago):
        print("id_departamento:", id_departamento)  # Verifica que sea 3
        print("id_gasto:", id_gasto)                # Verifica que sea 1
        # Convertir `fecha_pago` a un objeto datetime si es necesario
        fecha_pago_dt = datetime.fromisoformat(fecha_pago)

        # Buscar el registro de `PaymentHistory` correspondiente
        payment_record = PaymentHistory.query.filter_by(idDepartamento=id_departamento, idGasto=id_gasto).first()
        if payment_record:
            print("Registro encontrado:", payment_record)
        else:
            print("Registro no encontrado")

        if not payment_record:
            return {"error": "Registro de pago no encontrado"}, 404

        # Verificar que `bill` esté relacionado
        if not payment_record.bill:
            return {"error": "No se encontró la relación con el gasto (Bill)"}, 404

        # Actualizar los campos de pago
        payment_record.monto_pagado = monto_pagado
        payment_record.fecha_pago = fecha_pago_dt
        payment_record.estado_deuda = EstadoDeuda.ALDIA if monto_pagado >= payment_record.bill.total_gasto else EstadoDeuda.MOROSO

        # Guardar los cambios en la base de datos
        db.session.commit()

        return {"message": "Pago registrado con éxito"}, 200
