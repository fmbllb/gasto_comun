from models.BillModel import db, Bill

class BillService:
    
    @staticmethod
    def create_bill(id_gasto, nom_gasto, total_gasto, fecha_gasto, tipo_gasto):
        bill = Bill(
            id_gasto=id_gasto,
            nom_gasto=nom_gasto,
            total_gasto=total_gasto,
            fecha_gasto=fecha_gasto,
            tipo_gasto=tipo_gasto
        )
        db.session.add(bill)
        db.session.commit()
        return bill 
        
    @staticmethod
    def get_all_bills():
        return Bill.query.all()        
    
    @staticmethod
    def get_bill_by_id(id_departmento):
        return Bill.query.get(id_departmento)