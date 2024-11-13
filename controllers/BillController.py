from services.BillService import BillService

class BillController:    
    @staticmethod
    def create_bill_controller(nom_gasto, total_gasto, fecha_creacion_gasto, tipo_gasto):
        return BillService.create_bill(nom_gasto, total_gasto, fecha_creacion_gasto, tipo_gasto)
            
    @staticmethod
    def get_bill_controller():        
        return BillService.get_all_bills()
    
    @staticmethod
    def get_bill_by_id_controller(id_gasto):
        return BillService.get_bill_by_id(id_gasto)
    
    @staticmethod
    def modify_tipo_gasto(id_gasto, nuevo_tipo):
        return BillService.update_tipo_gasto(id_gasto, nuevo_tipo)