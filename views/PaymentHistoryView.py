from datetime import datetime
from flask import Blueprint, request, jsonify
from controllers.PaymentHistoryController import PaymentHistoryController

payment_history_blueprint = Blueprint('payment_history_blueprint', __name__)


"""
componente>>
    >>PaymentHistoryView
        >>create_payment_history()
        >>get_all_payment_histories()        
        >>get_payment_history_by_id()
        >>get_payment_history_by_date()
"""



class PaymentHistoryView:



    @staticmethod
    @payment_history_blueprint.route('/payment_histories/create', methods=['POST'])
    def create_payment_history():
        # Receive the request data
        data = request.get_json()
        
        # Retrieve the fields from the JSON
        idDepartamento = data.get('idDepartamento')
        idGasto = data.get('idGasto')
        cantidad = data.get('cantidad')
        monto_pagado = data.get('monto_pagado')
        estado_deuda = data.get('estado_deuda')

        # Call the controller to handle the business logic
        new_payment_history = PaymentHistoryController.create_payment_history_controller(
            idDepartamento, idGasto, cantidad, monto_pagado, estado_deuda
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
        # Llama al controlador para obtener todos los historiales de pago
        payment_histories = PaymentHistoryController.get_payment_history_controller()
        payment_histories_list = [
            {
                "id": f"{payment_history.idDepartamento}-{payment_history.idGasto}",
                "fecha_emision": payment_history.fecha_emision.strftime("%d/%m/%Y") if payment_history.fecha_emision else None,
                "fecha_pago": payment_history.fecha_pago.strftime("%d/%m/%Y") if payment_history.fecha_pago else None,
                "monto_pagado": payment_history.monto_pagado,
                "estado_deuda": payment_history.estado_deuda
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
        
    @payment_history_blueprint.route('/payment_histories/fecha_pago/<string:fecha_pago>', methods=['GET'])
    def get_all_payment_history_by_date(fecha_pago):
        try:
            # Intentamos convertir el string recibido en un objeto datetime
            fecha_pago_dt = datetime.strptime(fecha_pago, '%Y-%m-%d')
        except ValueError:
            return jsonify({"mensaje": "Formato de fecha incorrecto"}), 400

        # Llama al controlador para obtener todos los historiales de pago en la fecha de pago dada
        payment_histories = PaymentHistoryController.get_payment_history_by_date_controller(fecha_pago_dt)
        
        # Crear la lista de resultados procesados
        payment_histories_list = [
            {
                "id": f"{payment_history.idDepartamento}-{payment_history.idGasto}",
                "fecha_pago": payment_history.fecha_pago.strftime('%Y-%m-%d') if payment_history.fecha_pago else None,
                "monto_pagado": payment_history.monto_pagado,
                "estado_deuda": payment_history.estado_deuda
            } for payment_history in payment_histories
        ]

        return jsonify({"Historiales de pago": payment_histories_list}), 200

    @staticmethod
    @payment_history_blueprint.route('/departamentos/morosos', methods=['GET'])
    def departamentos_morosos():
        limit = request.args.get('limit', type=int)
        morosos = PaymentHistoryController.obtener_morosos(limit=limit)
        return jsonify({"Departamentos morosos": morosos}), 200