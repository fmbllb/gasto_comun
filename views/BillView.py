from flask import Blueprint, request, jsonify
from controllers.BillController import BillController

bill_blueprint = Blueprint('bill_blueprint', __name__)
"""
componente>>
    >>BillView
        >>create_bill()
        >>get_all_bills()
        >>get_bill_by_id()
        >>modify_bill_tipo()
"""
class BillView:

    @staticmethod
    @bill_blueprint.route('/bills/create', methods=['POST'])
    def create_bill():
        # Receive the request to create a bill and delegate to the controller
        data = request.get_json()
        nom_gasto = data.get('nom_gasto')
        total_gasto = data.get('total_gasto')
        tipo_gasto = data.get('tipo_gasto')

        new_bill = BillController.create_bill_controller(nom_gasto, total_gasto, 
                                                        tipo_gasto)
        
        return jsonify({
            "mensaje": "Gasto Comun creado", 
            "Gasto Comun": {"id": new_bill.id_gasto, "nombre": new_bill.nom_gasto, "Total Gasto": new_bill.total_gasto, 
                            "Fecha Creacion Gasto": new_bill.fecha_gasto, "Tipo Gasto": new_bill.tipo_gasto}
        }), 201

    @staticmethod
    @bill_blueprint.route('/bills', methods=['GET'])
    def get_all_bills():
        # Call the controller to get all bills
        bills = BillController.get_bill_controller()
        bills_list = [{"id": bill.id_gasto, "Gasto Comun": bill.nom_gasto, "Total Gasto": bill.total_gasto} for bill in bills]
        if len(bills_list) == 0:
            return jsonify({"mensaje": "No hay Gastos Comunes registrados"}), 404
        return jsonify({"Gastos Comunes": bills_list}), 200

    @staticmethod
    @bill_blueprint.route('/bills/<int:id_gasto>', methods=['GET'])
    def get_bill_by_id(id_gasto):
        # Call the controller to get a bill by its ID
        bill = BillController.get_bill_by_id_controller(id_gasto)
        if bill is None:
            return jsonify({"mensaje": "Gasto Comun inexistente"}), 404
        
        return jsonify({"id": bill.id_gasto, "nom_gasto": bill.nom_gasto, "tipo_gasto": bill.tipo_gasto}), 200
    
    @staticmethod
    @bill_blueprint.route('/bills/<int:id_gasto>/tipo', methods=['PUT'])
    def modify_bill_tipo(id_gasto):
        # Obtener el valor de 'tipo_gasto' desde el cuerpo de la solicitud
        data = request.get_json()
        nuevo_tipo = data.get("tipo_gasto")
        
        if not nuevo_tipo or nuevo_tipo not in ['m', 'a', 'a']:
            return jsonify({"mensaje": "El valor de 'tipo_gasto' debe ser 'm', 'a' o 'c'"}), 400

        # Llamar al controlador para realizar la modificación
        response, status_code = BillController.modify_tipo_gasto(id_gasto, nuevo_tipo)
        
        return jsonify(response), status_code
