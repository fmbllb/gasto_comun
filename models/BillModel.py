from app import db

class Bill(db.Model):
    __tablename__ = 'bill'

    id_gasto = db.Column(db.Integer, primary_key=True)
    nom_gasto = db.Column(db.String(15), nullable=False)
    total_gasto = db.Column(db.Integer, nullable=False)
    fecha_gasto = db.Column(db.Date, nullable=False)
    tipo_gasto = db.Column(db.String(1), nullable=False)

    # Relación con PaymentHistory
    departments = db.relationship('PaymentHistory', back_populates='bill', lazy=True)
    
    def serialize(self):
        return {
            'id_gasto': self.id_gasto,
            'nom_gasto': self.nom_gasto,
            'total_gasto': self.total_gasto,
            'fecha_gasto': self.fecha_gasto,
            'tipo_gasto': self.tipo_gasto,
        }