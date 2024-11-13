from datetime import datetime
from app import db
from enum import Enum

class EstadoDeuda(str, Enum):
    NOTIFICADO = "n"
    MOROSO = "m"
    ALDIA = "a"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]
    
class PaymentHistory(db.Model):
    __tablename__ = 'payment_history'
    
    idDepartamento = db.Column(db.Integer, db.ForeignKey('department.id_departamento'), primary_key=True)
    idGasto = db.Column(db.Integer, db.ForeignKey('bill.id_gasto'), primary_key=True)
    fecha_emision = db.Column(db.Date, nullable=False, default=datetime.now)
    cantidad = db.Column(db.Integer, nullable=False)
    monto_pagado = db.Column(db.Integer, nullable=False)
    estado_deuda = db.Column(db.Enum(EstadoDeuda), nullable=False) # n = Notificado, m = Moroso, a = Al día

    bill = db.relationship('Bill', back_populates='payment_history')
    department = db.relationship('Department', back_populates='payment_history')

    def serialize(self):
        return {
            'idDepartamento': self.idDepartamento,
            'idGasto': self.idGasto,
            'fecha_emision': self.fecha_emision,
            'cantidad': self.cantidad,
            'monto_pagado': self.monto_pagado,
            'estado_deuda': self.estado_deuda,
        }