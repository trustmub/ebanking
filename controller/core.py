import random

from functools import wraps

from flask import session as login_session, redirect, url_for, jsonify, json
from flask_bcrypt import Bcrypt
from models.model import OtpTable, db, User
from controller.endpoints import AccountLookup, CustomerLookup

bc = Bcrypt()


# user login decorator


def user_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'username' in login_session:
            return redirect(url_for('user.login'))
        return f(*args, **kwargs)

    return decorator


def login_function(username, password):
    record = User.query.filter_by(username=username).first()
    if record and bc.check_password_hash(record.password_hash, password):
        return True


def get_user_details(username):
    user_account = User.query.filter_by(username=username).first()
    r = AccountLookup(user_account.account).lookup()
    return r.json()


def verify_customer(customer):
    r = CustomerLookup(customer).lookup()
    record = r.json()
    my_id = "".join(("".join(record['id_number'].split(' '))).split('-'))
    return my_id


def verify_details(response):
    record = response.json()
    if record['status'] == 200:
        my_id_entered = "".join(("".join(login_session['reg_id'].split(' '))).split('-'))
        national_id = verify_customer(record['customer_id'].upper().strip().strip('-'))
        if national_id != my_id_entered:
            return False
        otp = generate_otp()
        save_otp(record['account_num'], otp)
        return otp
    return False


def generate_otp():
    otp = random.randint(11111, 99999)
    print(otp)
    return otp


def save_otp(account, otp):
    if otp_status(account):
        record = OtpTable(account=account, otp=otp, verified=False)
        db.session.add(record)
        db.session.commit()


def otp_status(account):
    record = OtpTable.query.filter_by(account=account).filter_by(verified=False).first()
    if record:
        return False
    else:
        return True


def is_otp_valid(account, otp):
    record = OtpTable.query.filter_by(account=account).filter_by(otp=otp).filter_by(verified=False).first()
    if record:
        record.verified = True
        db.session.add(record)
        db.session.commit()
        return True


def create_user(username, password):
    if check_username_exists(username):
        print("username is taken")
        return False
    user = User()
    record = User(username=username, account=login_session['account_num'], password_hash=user.hash_password(password))
    db.session.add(record)
    db.session.commit()
    print("user has bee successfully created")
    return True


def check_username_exists(username):
    record = User.query.filter_by(username=username).first()
    if record:
        print("This use exists")
        return True
