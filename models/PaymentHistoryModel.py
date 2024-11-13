from datetime import datetime, timedelta
from sqlalchemy.sql import func
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
    
    idDepartamento = db.Column(db.Integer, db.ForeignKey('Department.id_departamento'), primary_key=True)
    idGasto = db.Column(db.Integer, db.ForeignKey('Bill.id_gasto'), primary_key=True)
    fecha_emision = db.Column(db.DateTime, nullable=True)
    fecha_pago = db.Column(db.DateTime, nullable=True)
    monto_pagado = db.Column(db.Integer, nullable=True)
    estado_deuda = db.Column(db.Enum(EstadoDeuda), nullable=False) # n = Notificado, m = Moroso, a = Al día

    bill = db.relationship('Bill', back_populates='payment_history')
    department = db.relationship('Department', back_populates='payment_history')

    def serialize(self):
        return {
            'idDepartamento': self.idDepartamento,
            'idGasto': self.idGasto,
            'fecha_emision': self.fecha_emision.isoformat() if self.fecha_emision else None,
            'fecha_pago': self.fecha_pago.isoformat() if self.fecha_pago else None,
            'monto_pagado': self.monto_pagado,
            'estado_deuda': self.estado_deuda.name if self.estado_deuda else None,
        }
    
    @staticmethod
    def get_next_emission_date(day_of_month):
        today = datetime.today()
        if today.day <= day_of_month:
            return today.replace(day=day_of_month)
        else:
            # Move to next month if today is past the specified day
            next_month = today.replace(day=1) + timedelta(days=32)
            return next_month.replace(day=day_of_month)