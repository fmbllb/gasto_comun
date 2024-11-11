from flask import Blueprint, request, jsonify
from controllers.BillController import BillController

bill_blueprint = Blueprint('bill_blueprint', __name__)

class BillView:

    @staticmethod
    @bill_blueprint.route('/bills/create', methods=['POST'])
    def create_bill():
        # Receive the request to create a bill and delegate to the controller
        data = request.get_json()
        nom_gasto = data.get('nom_gasto')
        total_gasto = data.get('total_gasto')
        fecha_gasto = data.get('fecha_gasto')
        tipo_gasto = data.get('tipo_gasto')

        new_bill = BillController.create_bill_controller(nom_gasto, total_gasto, 
                                                        fecha_gasto, tipo_gasto)
        
        return jsonify({
            "mensaje": "Gasto Comun creado", 
            "Gasto Comun": {"id": new_bill.id_gasto, "nombre": new_bill.nom_gasto, 
                            "Fecha Creacion Gasto": new_bill.fecha_gasto, "Tipo Gasto": new_bill.tipo_gasto}
        }), 201

    @staticmethod
    @bill_blueprint.route('/bills', methods=['GET'])
    def get_all_bills():
        # Call the controller to get all bills
        bills = BillController.get_bill_controller()
        bills_list = [{"id": bill.id_gasto, "Gasto Comun": bill.nom_gasto} for bill in bills]
        return jsonify({"Gastos Comunes": bills_list}), 200

    @staticmethod
    @bill_blueprint.route('/bills/<int:id_gasto>', methods=['GET'])
    def get_bill_by_id(id_gasto):
        # Call the controller to get a bill by its ID
        bill = BillController.get_bill_by_id_controller(id_gasto)
        if bill is None:
            return jsonify({"mensaje": "Gasto Comun inexistente"}), 404
        
        return jsonify({"id": bill.id_gasto, "nom_gasto": bill.nom_gasto}), 200
