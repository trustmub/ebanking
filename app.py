from models.model import db

from flask import Flask, render_template
from views.user import user
from views.statement import statement
from views.landing import landing
from views.bill import bill
from views.transfer import transfer

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

app.register_blueprint(user)
app.register_blueprint(landing)
app.register_blueprint(bill)
app.register_blueprint(transfer)
app.register_blueprint(statement)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
