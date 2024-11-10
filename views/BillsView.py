from flask import Blueprint, request, jsonify
from controllers.BillsController import BillController

bill_blueprint = Blueprint('bill_blueprint', __name__)

class DepartmentView:

    @staticmethod
    @bill_blueprint.route('/departments/create', methods=['POST'])
    def create_department():
        # Receive the request to create a department and delegate to the controller
        data = request.get_json()
        n_piso = data.get('n_piso')
        new_department = DepartmentController.create_department_controller(n_piso)
        
        return jsonify({
            "mensaje": "Departamento creado", 
            "Departmento": {"id": new_department.id_departamento, "n_piso": new_department.n_piso}
        }), 201

    @staticmethod
    @department_blueprint.route('/departments', methods=['GET'])
    def get_all_departments():
        # Call the controller to get all departments
        departments = DepartmentController.get_departments_controller()
        departments_list = [{"id": department.id_departamento, "n_piso": department.n_piso} for department in departments]
        return jsonify({"Departamentos": departments_list}), 200

    @staticmethod
    @department_blueprint.route('/departments/<int:department_id>', methods=['GET'])
    def get_department_by_id(department_id):
        # Call the controller to get a department by its ID
        department = DepartmentController.get_department_by_id_controller(department_id)
        if department is None:
            return jsonify({"mensaje": "Departamento inexistente"}), 404
        
        return jsonify({"id": department.id_departamento, "n_piso": department.n_piso}), 200
