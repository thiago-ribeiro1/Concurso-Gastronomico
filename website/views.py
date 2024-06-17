from flask import Blueprint, render_template, request
from .models import Voto
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/bdc', methods=['GET', 'POST'])
def bdc():
    if request.method == 'POST':
        
        print(request.form)
        cod = request.form.get('codAvaliacao')
        nom = request.form.get('nome')
        cp = request.form.get('cpf')
        telefon = request.form.get('telefone')
        comentari = request.form.get('comentario')


        print(cod)
        print(nom)
        print(cp)
        print(telefon)
        print(comentari)



        new_voto = Voto(codAvaliacao=cod, nome=nom, cpf=cp, telefone=telefon, comentario=comentari)
        db.session.add(new_voto)
        db.session.commit()
        print('Teje Votado')
        #return redirect(url_for('views.home'))

    return render_template("bdc.html")




#def ranking():
    return render_template("ranking.html")

