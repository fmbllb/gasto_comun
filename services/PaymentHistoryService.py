from typing import Dict, List, Optional
from models.PaymentHistoryModel import EstadoDeuda, db, PaymentHistory

class PaymentHistoryService:
    
    @staticmethod
    def create_payment_history(idDepartamento, idGasto, fecha_emision, cantidad, monto_pagado, estado_deuda):
        payment_history = PaymentHistory(
            idDepartamento=idDepartamento,
            idGasto=idGasto,
            fecha_emision=fecha_emision,
            cantidad=cantidad,
            monto_pagado=monto_pagado,
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

    @staticmethod
    def obtener_departamentos_morosos(limit: Optional[int] = None) -> List[Dict]:
        query = PaymentHistory.query.filter_by(estado_deuda=EstadoDeuda.MOROSO)
        
        if limit:
            query = query.limit(limit)
            
        morosos = query.all()
        return [m.serialize() for m in morosos]
    
    @staticmethod
    def get_payment_history_by_date(fecha_emision):
        return PaymentHistory.query.filter_by(fecha_emision=fecha_emision).all()