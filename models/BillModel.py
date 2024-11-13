# FILE: models/BillModel.py
from app import db
from sqlalchemy.sql import func
from datetime import datetime
from enum import Enum

class TipoGasto(str, Enum):
    MANTENCION = "m"
    ASCENSOR = "a"
    CUOTA = "c"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

class Bill(db.Model):
    __tablename__ = 'Bill'

    id_gasto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_gasto = db.Column(db.String(15), nullable=False)
    total_gasto = db.Column(db.Integer, nullable=False)
    fecha_emision = db.Column(db.DateTime, nullable=True)  # Fecha en la que se emite la factura
    fecha_creacion_gasto = db.Column(db.DateTime, nullable=False, server_default=func.now())  # Fecha de creacion de la factura (auditoria)
    tipo_gasto = db.Column(db.Enum(TipoGasto), nullable=False)

    # Relación con PaymentHistory
    payment_history = db.relationship('PaymentHistory', back_populates='bill', lazy=True)
    
    def serialize(self):
        return {
            'id_gasto': self.id_gasto,
            'nom_gasto': self.nom_gasto,
            'total_gasto': self.total_gasto,
            'fecha_creacion_gasto': self.fecha_creacion_gasto.isoformat() if self.fecha_creacion_gasto else None,
            'fecha_emision': self.fecha_emision.isoformat() if self.fecha_emision else None,
            'tipo_gasto': self.tipo_gasto.value,
            'payment_history': [payment.serialize() for payment in self.payment_history],
        }