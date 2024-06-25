from flask import Blueprint, render_template, request, jsonify
from .models import Voto
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/bdc', methods=['GET', 'POST'])
def bdc():
    if request.method == 'POST':
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')  # Captura o restaurante do formulário

        try:
            new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input) if atendimento_input else None,  # Converte para inteiro se existir
                qualidade_input=int(qualidade_input) if qualidade_input else None,
                apresentacao_input=int(apresentacao_input) if apresentacao_input else None,
                restaurante=restaurante
            )

            db.session.add(new_voto)
            db.session.commit()

            print('Voto registrado com sucesso!')
            return 'Voto registrado com sucesso!'
        
        except Exception as e:
            db.session.rollback()
            print(f'Erro ao registrar voto: {str(e)}')
            return f'Erro ao registrar voto: {str(e)}'

    return render_template("bdc.html")

@views.route('/seuManoel', methods=['GET', 'POST'])
def seuManoel():
    if request.method == 'POST':
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')  # Captura o restaurante do formulário

        try:
            new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input) if atendimento_input else None,
                qualidade_input=int(qualidade_input) if qualidade_input else None,
                apresentacao_input=int(apresentacao_input) if apresentacao_input else None,
                restaurante=restaurante
            )

            db.session.add(new_voto)
            db.session.commit()

            print('Voto registrado com sucesso!')
            return 'Voto registrado com sucesso!'
        
        except Exception as e:
            db.session.rollback()
            print(f'Erro ao registrar voto: {str(e)}')
            return f'Erro ao registrar voto: {str(e)}'

    return render_template("seuManoel.html")

@views.route('/pastelDaLiberdade', methods=['GET', 'POST'])
def pastelDaLiberdade():
    if request.method == 'POST':
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')  # Captura o restaurante do formulário

        try:
            new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input) if atendimento_input else None,
                qualidade_input=int(qualidade_input) if qualidade_input else None,
                apresentacao_input=int(apresentacao_input) if apresentacao_input else None,
                restaurante=restaurante
            )

            db.session.add(new_voto)
            db.session.commit()

            print('Voto registrado com sucesso!')
            return 'Voto registrado com sucesso!'
        
        except Exception as e:
            db.session.rollback()
            print(f'Erro ao registrar voto: {str(e)}')
            return f'Erro ao registrar voto: {str(e)}'

    return render_template("pastelDaLiberdade.html")

@views.route('/picanha200', methods=['GET', 'POST'])
def picanha200():
    if request.method == 'POST':
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')  # Captura o restaurante do formulário

        try:
            new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input) if atendimento_input else None,
                qualidade_input=int(qualidade_input) if qualidade_input else None,
                apresentacao_input=int(apresentacao_input) if apresentacao_input else None,
                restaurante=restaurante
            )

            db.session.add(new_voto)
            db.session.commit()

            print('Voto registrado com sucesso!')
            return 'Voto registrado com sucesso!'
        
        except Exception as e:
            db.session.rollback()
            print(f'Erro ao registrar voto: {str(e)}')
            return f'Erro ao registrar voto: {str(e)}'

    return render_template("picanha200.html")

@views.route('/saporeDItalia', methods=['GET', 'POST'])
def saporeDItalia():
    if request.method == 'POST':
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')  # Captura o restaurante do formulário

        try:
            new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input) if atendimento_input else None,
                qualidade_input=int(qualidade_input) if qualidade_input else None,
                apresentacao_input=int(apresentacao_input) if apresentacao_input else None,
                restaurante=restaurante
            )

            db.session.add(new_voto)
            db.session.commit()

            print('Voto registrado com sucesso!')
            return 'Voto registrado com sucesso!'
        
        except Exception as e:
            db.session.rollback()
            print(f'Erro ao registrar voto: {str(e)}')
            return f'Erro ao registrar voto: {str(e)}'
        
    return render_template("saporeDItalia.html")

@views.route('/dominos', methods=['GET', 'POST'])
def dominos():
    if request.method == 'POST':
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')  # Captura o restaurante do formulário

        try:
            new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input) if atendimento_input else None,
                qualidade_input=int(qualidade_input) if qualidade_input else None,
                apresentacao_input=int(apresentacao_input) if apresentacao_input else None,
                restaurante=restaurante
            )

            db.session.add(new_voto)
            db.session.commit()

            print('Voto registrado com sucesso!')
            return 'Voto registrado com sucesso!'
        
        except Exception as e:
            db.session.rollback()
            print(f'Erro ao registrar voto: {str(e)}')
            return f'Erro ao registrar voto: {str(e)}'

    return render_template("dominos.html")
