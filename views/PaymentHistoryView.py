from datetime import datetime
from flask import Blueprint, request, jsonify
from controllers.PaymentHistoryController import PaymentHistoryController

payment_history_blueprint = Blueprint('payment_history_blueprint', __name__)

class PaymentHistoryView:

    @staticmethod
    @payment_history_blueprint.route('/payment_histories/create', methods=['POST'])
    def create_payment_history():
        # Receive the request data
        data = request.get_json()
        
        # Retrieve the fields from the JSON
        idDepartamento = data.get('idDepartamento')
        idGasto = data.get('idGasto')
        fecha_emision_str = data.get('fecha_emision')  # Expecting the date as a string
        cantidad = data.get('cantidad')
        monto_pagado = data.get('monto_pagado')
        estado_deuda = data.get('estado_deuda')

        # Convert the string date to a datetime.date object
        try:
            fecha_emision = datetime.strptime(fecha_emision_str, "%d-%m-%Y").date()
        except ValueError:
            return jsonify({"error": "Fecha de emisión no tiene el formato correcto, use dd-mm-YYYY"}), 400

        # Call the controller to handle the business logic
        new_payment_history = PaymentHistoryController.create_payment_history_controller(
            idDepartamento, idGasto, fecha_emision, cantidad, monto_pagado, estado_deuda
        )
        
        # Return the response
        return jsonify({
            "mensaje": "Historial creado", 
            "Historial de pago": {
                "id": f"{new_payment_history.idDepartamento}-{new_payment_history.idGasto}",
                "fecha_emision": new_payment_history.fecha_emision.strftime("%d-%m-%Y")
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
        payment_history = PaymentHistoryController.get_payment_history_by_id_controller(idDepartamento, idGasto)
        if payment_history is None:
            return jsonify({"mensaje": "Historial inexistente"}), 404
        
        return jsonify({
            "id": f"{payment_history.idDepartamento}-{payment_history.idGasto}",
            "fecha_emision": payment_history.fecha_emision
        }), 200
        
    @payment_history_blueprint.route('/payment_histories/<string:fecha_emision>', methods=['GET'])
    def get_all_payment_history_by_date(fecha_emision):
        try:
            # Intentamos convertir el string recibido en un objeto datetime
            fecha_emision = datetime.strptime(fecha_emision, '%Y-%m-%d')
        except ValueError:
            return jsonify({"mensaje": "Formato de fecha incorrecto"}), 400

        payment_history = PaymentHistoryController.get_payment_history_by_date_controller(fecha_emision)
        if payment_history is None:
            return jsonify({"mensaje": "Historial inexistente"}), 404
        
        return jsonify({
            "id": f"{payment_history.idDepartamento}-{payment_history.idGasto}",
            "fecha_emision": payment_history.fecha_emision.strftime('%Y-%m-%d')
        }), 200
