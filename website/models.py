from . import db
from flask_login import UserMixin
from sqlalchemy import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    adm = db.Column(db.Integer)

class Voto(db.Model):
    __tablename__ = 'voto'

    id = db.Column(db.Integer, primary_key=True)
    codAvaliacao = db.Column(db.String(255))
    nome = db.Column(db.String(255))
    cpf = db.Column(db.String(14))
    telefone = db.Column(db.String(20))
    comentario = db.Column(db.Text)
    atendimento_input = db.Column(db.Integer)
    qualidade_input = db.Column(db.Integer)
    apresentacao_input = db.Column(db.Integer)
    restaurante = db.Column(db.String(255))  # Coluna para armazenar o restaurante

    def __init__(self, codAvaliacao, nome, cpf, telefone, comentario, atendimento_input, qualidade_input, apresentacao_input, restaurante):
        self.codAvaliacao = codAvaliacao
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.comentario = comentario
        self.atendimento_input = atendimento_input
        self.qualidade_input = qualidade_input
        self.apresentacao_input = apresentacao_input
        self.restaurante = restaurante

