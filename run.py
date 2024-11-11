from app import create_app
from views.DepartmentView import department_blueprint
from views.BillView import bill_blueprint
from views.PaymentHistoryView import payment_history_blueprint

app = create_app()
app.register_blueprint(department_blueprint)
app.register_blueprint(bill_blueprint)
app.register_blueprint(payment_history_blueprint)

if __name__ == '__main__':
    app.run(debug=True)