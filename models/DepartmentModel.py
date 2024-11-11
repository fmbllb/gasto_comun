from app import db
from enum import Enum


class Disponibilidad(str, Enum):
    INMEDIATA = "i"
    PRONTA = "p"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

class Department(db.Model):
    __tablename__ = 'department'

    id_departamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_departamento = db.Column(db.Integer, unique=True, nullable=False)
    n_piso = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    n_telefono = db.Column(db.Integer, nullable=True)
    disponibilidad = db.Column(db.Enum(Disponibilidad), nullable=False)
    
    # Relación con PaymentHistory
    payment_history = db.relationship('PaymentHistory', back_populates='department', lazy=True)

def serialize(self):
    return {
        'id_departamento': self.id_departamento,
        'n_departamento': self.n_departamento,
        'n_piso': self.n_piso,
        'direccion': self.direccion,
        'n_telefono': self.n_telefono,
        'disponibilidad': self.disponibilidad.value,
        'bills': [bill.serialize() for bill in self.bills],
    }
