from . import db
from flask_login import UserMixin
from sqlalchemy import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Voto(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True) 
    idNfe = db.Column(db.Integer)
    codAvaliacao = db.Column(db.Integer)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(14)) #999.999.999-99
    telefone = db.Column(db.String(15)) #(83) 99999-9999
    comentario = db.Column(db.String(1500))

    def __init__(self, codAvaliacao, nome, cpf, telefone, comentario):
        self.cod_avaliacao = codAvaliacao
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.comentario = comentario