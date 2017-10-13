from flask import Blueprint, render_template, url_for, redirect
from flask.views import View, MethodView

transfer = Blueprint('transfer', __name__)


class TransferView(View):
    methods = ['POST', 'GET']
    decorators = []

    def dispatch_request(self):
        return render_template('transfer.html')


transfer.add_url_rule('/transfers/', view_func=TransferView.as_view('transfer'))
