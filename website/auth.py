from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    user = request.form.get('user')
    senha = request.form.get('senha')
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