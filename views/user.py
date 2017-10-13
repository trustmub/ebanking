from flask import Blueprint, request, render_template, redirect, url_for, jsonify, flash, json
from flask import session as login_session
from flask.views import View
from forms.login_form import LoginForm

from controller.validators import *
from controller.endpoints import Login, Register

user = Blueprint('user', __name__)


class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = LoginForm()

        if request.method == 'POST':
            if not form.validate():
                flash("please enter valid information")
                return redirect(url_for('user.login'))
            else:
                username = request.form['username']
                password = request.form['password']

                user_auth = Login(username, password)
                r = user_auth.login_user()

                if hasattr(r, 'status_code') and r.status_code == 200:
                    record = r.json()
                    login_session['username'] = username
                    login_session['name'] = record['name']
                    login_session['account'] = record['accountNumber']
                    return redirect(url_for('landing.home'))
                return redirect(url_for('user.login'))
        return render_template('login.html', form=form)


class LogoutView(View):
    methods = ['GET', 'POST']
    decorators = []

    def dispatch_request(self):
        login_session.pop('username', None)
        login_session.pop('name', None)
        login_session.pop('account', None)
        return redirect(url_for('user.login'))


class ResetView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        return "Reset template here"


class RegisterView(View):
    methods = ['POST', 'GET']
    decorators = []

    def dispatch_request(self):
        print("in middleware post")
        if request.method == 'POST':
            print("inside the post")
            account_num = request.form['accountNumber']
            type = request.form['idType']
            idNumber = request.form['idNumber']
            dob = request.form['dob']
            tandc_check = request.form['tndcRegCheck']

            print(tandc_check)
            print(type)
            print(idNumber)
            print(dob)

            data_dict = {'accountNumber': account_num}

            # r = Register.register_user(data_dict)
            rr = '{"status": 200}'
            varr = jsonify(json.dumps(rr))
            print(rr)
            return rr
        # Return a jsonified dictionary for the jQuery
        return jsonify()


class RegisterOtpView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            otp = request.form['otpNumber']
            username = request.form['username']
            password = request.form['password']
            password2 = request.form['passwordConf']
            account = request.form['account']
            if password != password2:
                flash("Password don't match")
                return

            data = {'otp': otp, 'username': username, 'password': password, 'account': account}
            r = Register.register_otp(data)
            return r
        return


user.add_url_rule('/', view_func=LoginView.as_view('login'))
user.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))
user.add_url_rule('/reset/', view_func=ResetView.as_view('reset'))
user.add_url_rule('/register/info/', view_func=RegisterView.as_view('register_info'))
user.add_url_rule('/register/otp/', view_func=RegisterOtpView.as_view('register_otp'))


@user.route('/register/pe/')
def register_pe():
    if request.method == 'post':
        return
    return 'jsonified response to the JQuery Ajax Response'


@user.route('/register/set/')
def register_set_password():
    if request.method == 'post':
        return
    return 'jsonified response to the JQuery Ajax Response'
