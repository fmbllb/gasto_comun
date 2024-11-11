from flask import Blueprint, request, jsonify
from controllers.PaymentHistoryController import PaymentHistoryController

payment_history_blueprint = Blueprint('payment_history_blueprint', __name__)

class PaymentHistoryView:

    @staticmethod
    @payment_history_blueprint.route('/payment_histories/create', methods=['POST'])
    def create_payment_history():
        # Receive the request data and delegate to the controller
        data = request.get_json()
        idDepartamento = data.get('idDepartamento')
        idGasto = data.get('idGasto')
        fecha_emision = data.get('fecha_emision')
        cantidad = data.get('cantidad')
        precio_pago = data.get('precio_pago')
        estado_deuda = data.get('estado_deuda')
        
        new_payment_history = PaymentHistoryController.create_payment_history_controller(
            idDepartamento, idGasto, fecha_emision, cantidad, precio_pago, estado_deuda
        )
        
        return jsonify({
            "mensaje": "Historial creado", 
            "Historial de pago": {
                "id": f"{new_payment_history.idDepartamento}-{new_payment_history.idGasto}",
                "fecha_emision": new_payment_history.fecha_emision
            }
        }), 201

    @staticmethod
    @payment_history_blueprint.route('/payment_histories', methods=['GET'])
    def get_all_payment_histories():
        # Call the controller to get all payment histories
        payment_histories = PaymentHistoryController.get_payment_history_controller()
        payment_histories_list = [
            {
                "id": f"{payment_history.idDepartamento}-{payment_history.idGasto}",
                "fecha_emision": payment_history.fecha_emision
            } for payment_history in payment_histories
        ]
        return jsonify({"Historiales de pago": payment_histories_list}), 200

    @staticmethod
    @payment_history_blueprint.route('/payment_histories/<int:idDepartamento>/<int:idGasto>', methods=['GET'])
    def get_payment_history_by_id(idDepartamento, idGasto):
        # Call the controller to get a payment history by its composite ID
        payment_history = PaymentHistoryController.get_payment_history_by_id_controller(idDepartamento, idGasto)
        if payment_history is None:
            return jsonify({"mensaje": "Historial inexistente"}), 404
        
        return jsonify({
            "id": f"{payment_history.idDepartamento}-{payment_history.idGasto}",
            "fecha_emision": payment_history.fecha_emision
        }), 200
