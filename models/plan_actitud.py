from db import db

class PlanActitud(db.Model):
    __tablename__ = 'PlanActitud'
    
    id = db.Column('Id', db.Integer, primary_key=True)
    id_plan = db.Column('IdPlan', db.Integer, db.ForeignKey('Plan.Id'), nullable=True)
    nombre = db.Column('Nombre', db.String(150), nullable=True)
    descripcion = db.Column('Descripcion', db.String(150), nullable=True)
    peso = db.Column('Peso', db.Float, nullable=True)
