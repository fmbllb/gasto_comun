from models.BillModel import db, Bill, TipoGasto
from datetime import datetime

class BillService:
    
    @staticmethod
    def create_bill(nom_gasto, total_gasto, fecha_creacion_gasto, tipo_gasto):
        # Convierte la fecha de creación a datetime si es un string
        if isinstance(fecha_creacion_gasto, str):
            fecha_creacion_gasto = datetime.strptime(fecha_creacion_gasto, '%Y-%m-%d %H:%M:%S')

        bill = Bill(
            nom_gasto=nom_gasto,
            total_gasto=total_gasto,
            fecha_creacion_gasto=fecha_creacion_gasto,  # Usa fecha_creacion_gasto directamente
            tipo_gasto=tipo_gasto
        )
        db.session.add(bill)
        db.session.commit()
        return bill
        
    @staticmethod
    def get_all_bills():
        return Bill.query.all()        
    
    @staticmethod
    def get_bill_by_id(id_gasto):
        return Bill.query.get(id_gasto)

    
    @staticmethod
    def update_tipo_gasto(id_gasto, nuevo_tipo):
        # Verificar si el gasto existe
        bill = Bill.query.get(id_gasto)
        if not bill:
            return {"error": "Gasto no encontrado"}, 404

        # Asignar el nuevo tipo de gasto si es válido
        if nuevo_tipo in [TipoGasto.MANTENCION.value, TipoGasto.ASCENSOR.value, TipoGasto.CUOTA.value]:
            bill.tipo_gasto = TipoGasto(nuevo_tipo)
        else:
            return {"error": "Valor de tipo de gasto no válido"}, 400

        # Guardar los cambios
        db.session.commit()
        return bill.serialize(), 200