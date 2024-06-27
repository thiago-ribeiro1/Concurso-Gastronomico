from flask import Blueprint, render_template, request, jsonify, send_file, send_from_directory, current_app, redirect, url_for, flash
from .models import Voto
from . import db
from sqlalchemy import func
import pandas as pd
import matplotlib.pyplot as plt
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/estabelecimento')
def estabelecimento():
    return render_template("estabelecimento.html")

@views.route('/bdc', methods=['GET', 'POST'])
def bdc():
    if request.method == 'POST':
        print('POST request received') 
        codAvaliacao = request.form.get('codAvaliacao')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        comentario = request.form.get('comentario')
        atendimento_input = request.form.get('atendimento_input')
        qualidade_input = request.form.get('qualidade_input')
        apresentacao_input = request.form.get('apresentacao_input')
        restaurante = request.form.get('restaurante')

        new_voto = Voto(
                codAvaliacao=codAvaliacao,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                comentario=comentario,
                atendimento_input=int(atendimento_input),
                qualidade_input=int(qualidade_input),
                apresentacao_input=int(apresentacao_input),
                restaurante=restaurante
            )
        db.session.add(new_voto)
        db.session.commit()

        print('Voto registrado com sucesso!')
        return redirect(url_for('views.home'))
    
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
        restaurante = request.form.get('restaurante')


        new_voto = Voto(
            codAvaliacao=codAvaliacao,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            comentario=comentario,
            atendimento_input=int(atendimento_input),
            qualidade_input=int(qualidade_input),
            apresentacao_input=int(apresentacao_input),
            restaurante=restaurante
            )

        db.session.add(new_voto)
        db.session.commit()

        print('Voto registrado com sucesso!')
        return redirect(url_for('index'))
        

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
        restaurante = request.form.get('restaurante')


        new_voto = Voto(
            codAvaliacao=codAvaliacao,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            comentario=comentario,
            atendimento_input=int(atendimento_input),
            qualidade_input=int(qualidade_input),
            apresentacao_input=int(apresentacao_input),
            restaurante=restaurante
            )

        db.session.add(new_voto)
        db.session.commit()

        print('Voto registrado com sucesso!')
        return redirect(url_for('index'))

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
        restaurante = request.form.get('restaurante')


        new_voto = Voto(
            codAvaliacao=codAvaliacao,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            comentario=comentario,
            atendimento_input=int(atendimento_input),
            qualidade_input=int(qualidade_input),
            apresentacao_input=int(apresentacao_input),
            restaurante=restaurante
            )

        db.session.add(new_voto)
        db.session.commit()

        print('Voto registrado com sucesso!')
        return redirect(url_for('index'))

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
        restaurante = request.form.get('restaurante')


        new_voto = Voto(
            codAvaliacao=codAvaliacao,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            comentario=comentario,
            atendimento_input=int(atendimento_input),
            qualidade_input=int(qualidade_input),
            apresentacao_input=int(apresentacao_input),
            restaurante=restaurante
            )

        db.session.add(new_voto)
        db.session.commit()

        print('Voto registrado com sucesso!')
        return redirect(url_for('index'))
        
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
        restaurante = request.form.get('restaurante')


        new_voto = Voto(
            codAvaliacao=codAvaliacao,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            comentario=comentario,
            atendimento_input=int(atendimento_input),
            qualidade_input=int(qualidade_input),
            apresentacao_input=int(apresentacao_input),
            restaurante=restaurante
            )

        db.session.add(new_voto)
        db.session.commit()

        print('Voto registrado com sucesso!')
        return redirect(url_for('index'))

    return render_template("dominos.html")


def calcular_media_ponderada():
    session = db.session

    result = session.query(
        Voto.restaurante,
        func.count(Voto.id).label('num_votos'),
        func.avg(Voto.atendimento_input).label('media_atendimento'),
        func.avg(Voto.qualidade_input).label('media_qualidade'),
        func.avg(Voto.apresentacao_input).label('media_apresentacao')
    ).group_by(Voto.restaurante).all()

    df = pd.DataFrame(result, columns=['restaurante', 'num_votos', 'media_atendimento', 'media_qualidade', 'media_apresentacao'])

    # Pesos dos votos
    peso_votos = 0.64
    peso_atendimento = 0.12
    peso_qualidade = 0.12
    peso_apresentacao = 0.12

    # Calcular a média ponderada
    max_votos = df['num_votos'].max()
    df['media_ponderada'] = (peso_votos * (df['num_votos'] / max_votos) + 
                             peso_atendimento * df['media_atendimento'] + 
                             peso_qualidade * df['media_qualidade'] + 
                             peso_apresentacao * df['media_apresentacao'])
    
    # Duas casas decimais
    df['media_atendimento'] = df['media_atendimento'].round(2)
    df['media_qualidade'] = df['media_qualidade'].round(2)
    df['media_apresentacao'] = df['media_apresentacao'].round(2)
    df['media_ponderada'] = df['media_ponderada'].round(2)

    # Ordenar os restaurantes pela média ponderada
    df = df.sort_values(by='media_ponderada', ascending=False)

    # Plotar gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(df['restaurante'], df['media_ponderada'], color='red')
    plt.xlabel('Restaurantes')
    plt.ylabel('Média Ponderada')
    plt.title('Ranking de Restaurantes por Média Ponderada')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Configurar o caminho relativo para salvar o plot
    plot_dir = os.path.join(current_app.root_path, 'static', 'plots')
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    plot_filename = os.path.join(plot_dir, 'plot.png')
    print(f"Salvando arquivo em: {plot_filename}")

    # Salvar o gráfico
    plt.savefig(plot_filename)
    return df, plot_filename

@views.route('/ranking')
def ranking():
    df, plot_filename = calcular_media_ponderada()
    return render_template('ranking.html', data=df.to_dict(orient='records'), plot_filename=plot_filename)

@views.route('/static/plots/<path:filename>')
def plots(filename):
    return send_from_directory('static/plots', filename)