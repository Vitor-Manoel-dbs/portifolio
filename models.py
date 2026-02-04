from db import db

class Projetos(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False )
    url = db.Column(db.String, nullable=False, unique=True)
    image_url = db.Column(db.String, nullable=False)
    