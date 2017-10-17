from flask import Blueprint, request, render_template, redirect, url_for, jsonify, flash, json
from flask import session as login_session
from flask.views import View, MethodView
from forms.login_form import LoginForm, RegisterForm

from controller.core import verify_details, is_otp_valid, create_user
from controller.validators import *
from controller.endpoints import Login, Register, AccountLookup

user = Blueprint('user', __name__)


class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = LoginForm()
        register_form = RegisterForm()

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
        return render_template('login.html', form=form, register_form=register_form)


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


class RegisterView(MethodView):
    methods = ['POST', 'GET']
    decorators = []

    def get(self):
        pass

    def post(self):
        print("inside the post")
        account_num = request.form['accountNumber']
        type = request.form['idType']
        id_number = request.form['idNumber']
        dob = request.form['dob']
        tandc_check = request.form['tndcRegCheck']
        # save the use this for the login session so that data can be retained when the modal is closed
        login_session['reg_type'] = type
        login_session['reg_id'] = id_number
        login_session['dob'] = dob
        login_session['accept_toc'] = tandc_check

        acc_look = AccountLookup(account_num)
        r = acc_look.lookup()
        login_session.pop('new_otp', None)
        if hasattr(r, 'status_code') and r.status_code == 200:
            verify = verify_details(r)
            login_session['new_otp'] = verify
            login_session['account_num'] = account_num
            print(f"hass attribure and {verify} status {r.status_code}")
        print(f"This is jsonified response : {r.json()}")
        return jsonify(r.json())


class RegisterOtpView(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        pass

    def post(self):
        otp = request.form['otpNumber']
        account = login_session['account_num']

        if is_otp_valid(account, otp):
            return jsonify({'status': 200, 'message': 'OTP verified'}), 200
        else:
            return jsonify({'status': 404, 'message': 'Failed to authenticate OTP'}), 200


class RegisterUserView(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        pass

    def post(self):
        print("in Register User")
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        print(f"Collected from the forms {username} and {password} and {password2}")
        if password != password2:
            return jsonify({'message': 'passwords don\'t match', 'status': 401}), 200
        if create_user(username, password):
            print("ater create user")
            return jsonify({'message': 'User Created', 'status': 200}), 200
        return jsonify({'message': 'Username is not Unique', 'status': 404}), 200


user.add_url_rule('/', view_func=LoginView.as_view('login'))
user.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))
user.add_url_rule('/reset/', view_func=ResetView.as_view('reset'))
user.add_url_rule('/register/info/', view_func=RegisterView.as_view('register_info'))
user.add_url_rule('/register/otp/', view_func=RegisterOtpView.as_view('register_otp'))
user.add_url_rule('/register/user/', view_func=RegisterUserView.as_view('register_user'))


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
