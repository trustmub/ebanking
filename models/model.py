from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)