# from app import app

import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

db = SQLAlchemy()
bcrypt = Bcrypt()


class OtpTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.BigInteger)
    otp = db.Column(db.Integer)
    verified = db.Column(db.Boolean, default=False)

    def __init__(self, account, otp, verified):
        self.account = account
        self.otp = otp
        self.verified = verified


class AccountLookup(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer)
    balance = db.Column(db.Float)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        return self.password_hash

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    biller = db.Column(db.String(50))
    service_account = db.Column(db.Integer)
    frequency = db.Column(db.String(25))
    start_date = db.Column(db.DateTime)
    updated = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)


if __name__ == '__main__':
    db.create_all()
