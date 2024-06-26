from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, Voto

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        
        
        user = User.query.filter_by(user=user).first()
        if user:
            if user.password == password:
                print('login success')
                print('deu certo', password)
                if user.adm == 1:
                    print ('ADM ENTRANDO')
                    return redirect(url_for('views.ranking'))
                elif user.adm == 0:
                    print ('USUARIO ENTRANDO')
                    return redirect(url_for('views.estabelecimento'))
                else:
                    print('erro')
            else:
                print(password)
        else:
            print('user não existe')



    '''
    user = request.form.get('user')
    senha = request.form.get('senha')
    '''
    return render_template("login-adm.html")

'''
#não to usando ---------------------------------#
@auth.route('/logout')                          #
def logout():                                   #
    return"<p>Logout</p>"                       #
                                                #
@auth.route('/sign-up')                         #
def sign_up():                                  #
    return"<p>Sign Up</p>"                      #
#não to usando ---------------------------------#
'''