from models.PaymentHistoryModel import db, PaymentHistory

class PaymentHistoryService:
    
    @staticmethod
    def create_payment_history(idDepartamento, idGasto, fecha_emision, cantidad, precio_pago, estado_deuda):
        payment_history = PaymentHistory(
            idDepartamento=idDepartamento,
            idGasto=idGasto,
            fecha_emision=fecha_emision,
            cantidad=cantidad,
            precio_pago=precio_pago,
            estado_deuda=estado_deuda
        )
        db.session.add(payment_history)
        db.session.commit()
        return payment_history 
        
    @staticmethod
    def get_all_payment_histories():
        return PaymentHistory.query.all()        
    
    @staticmethod
    def get_payment_history_by_id(idDepartamento, idGasto):
        return PaymentHistory.query.get((idDepartamento, idGasto))
