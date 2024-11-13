from services.PaymentHistoryService import PaymentHistoryService
from models.PaymentHistoryModel import PaymentHistory
from sqlalchemy import func



class PaymentHistoryController:    
    @staticmethod
    def create_payment_history_controller(idDepartamento, idGasto, 
                                        fecha_emision, precio_pago, estado_deuda):
        return PaymentHistoryService.create_payment_history(idDepartamento, idGasto,
                                                fecha_emision, precio_pago, estado_deuda)
            
    @staticmethod
    def get_payment_history_controller():        
        return PaymentHistoryService.get_all_payment_histories()
    
    @staticmethod
    def get_payment_history_by_id_controller(idDepartamento, idGasto):
        return PaymentHistoryService.get_payment_history_by_id(idDepartamento, idGasto)
    
    @staticmethod
    def get_payment_history_by_date_controller(fecha_pago):
        return PaymentHistory.query.filter(func.date(PaymentHistory.fecha_pago) == fecha_pago.date()).all()