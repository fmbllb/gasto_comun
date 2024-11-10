from app import db

class PaymentHistory(db.Model):
    __tablename__ = 'payment_history'
    
    idDepartamento = db.Column(db.Integer, db.ForeignKey('department.id_departamento'), primary_key=True)
    idGasto = db.Column(db.Integer, db.ForeignKey('bill.id_gasto'), primary_key=True)
    fecha_emision = db.Column(db.Date, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_pago = db.Column(db.Integer, nullable=False)
    estado_deuda = db.Column(db.String(1), nullable=False)


    bill = db.relationship('Bill', back_populates='departments')
    department = db.relationship('Department', back_populates='bills')

    def serialize(self):
        return {
            'idDepartamento': self.idDepartamento,
            'idGasto': self.idGasto,
            'fecha_emision': self.fecha_emision,
            'cantidad': self.cantidad,
            'precio_pago': self.precio_pago,
            'estado_deuda': self.estado_deuda,
        }