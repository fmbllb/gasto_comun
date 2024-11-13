from flask import Blueprint, request, jsonify
from controllers.DepartmentController import DepartmentController

department_blueprint = Blueprint('department_blueprint', __name__)

""" 
componente>>
    >>DepartamentoView
        >>create_department()
        >>get_all_departments()
        >>get_department_by_id()
        >>update_disponibilidad()
        >>registrar_pago() 
"""

class DepartmentView:

    @staticmethod
    @department_blueprint.route('/departments/create', methods=['POST'])
    def create_department():
        data = request.get_json()

        n_departamento = data.get('n_departamento')
        n_piso = data.get('n_piso')
        direccion = data.get('direccion')
        n_telefono = data.get('n_telefono')
        disponibilidad = data.get('disponibilidad')

        new_department = DepartmentController.create_department_controller(n_departamento, n_piso, 
                                                                        direccion, n_telefono, disponibilidad)
        
        return jsonify({
            "mensaje": "Departamento creado", 
            "Departamento": {"id": new_department.id_departamento, "n_departamento": new_department.n_departamento, "n_piso": new_department.n_piso, 
                            "direccion": new_department.direccion, "n_telefono": new_department.n_telefono,
                            "disponibilidad": new_department.disponibilidad}
        }), 201

    @staticmethod
    @department_blueprint.route('/departments', methods=['GET'])
    def get_all_departments():
        # Call the controller to get all departments
        departments = DepartmentController.get_department_controller()
        departments_list = [{"id": department.id_departamento, "n_piso": department.n_piso, 
                            "direccion": department.direccion, "n_telefono": department.n_telefono,
                            "disponibilidad": department.disponibilidad} for department in departments]
        if departments is None:
            return jsonify({"mensaje": "No hay departamentos"}), 404
        
        return jsonify({"Departamentos": departments_list}), 200

    @staticmethod
    @department_blueprint.route('/departments/<int:id_departamento>', methods=['GET'])
    def get_department_by_id(id_departamento):
        # Call the controller to get a department by its ID
        department = DepartmentController.get_department_by_id_controller(id_departamento)
        if department is None:
            return jsonify({"mensaje": "Departamento inexistente"}), 404
        
        return jsonify({"id": department.id_departamento, "n_piso": department.n_piso, 
                            "direccion": department.direccion, "n_telefono": department.n_telefono,
                            "disponibilidad": department.disponibilidad }), 200
    
    @staticmethod
    @department_blueprint.route('/departments/update_disponibilidad', methods=['PUT'])
    def update_disponibilidad():
        data = request.get_json()
        id_departamento = data.get('id_departamento')
        new_disponibilidad = data.get('disponibilidad')
        
        # Call the controller method
        updated_department = DepartmentController.update_disponibilidad_controller(
            id_departamento, new_disponibilidad
        )

        if updated_department:
            return jsonify({
                "mensaje": "Disponibilidad actualizada",
                "Departmento": {
                    "id": updated_department.id_departamento,
                    "disponibilidad": updated_department.disponibilidad
                }
            }), 200
        else:
            return jsonify({"mensaje": "Departamento no encontrado"}), 404
        
    @staticmethod
    @department_blueprint.route('/departments/<int:id_departamento>/pagar/<int:id_gasto>', methods=['POST'])
    def registrar_pago(idDepartamento, idGasto):
        # Llamar al servicio para manejar el pago
        response, status_code = DepartmentController.registrar_pago(idDepartamento, idGasto)
        return jsonify(response), status_code
