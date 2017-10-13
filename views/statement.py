from flask import Blueprint, request, render_template, redirect, url_for
from flask.views import View

statement = Blueprint('statement', __name__)


class StateRequestView(View):
    methods = ['POST', 'GET']
    decorators = []

    def dispatch_request(self):
        if request.method == 'POST':
            start_date = request.form['startDate']
            end_date = request.form['endDate']

        return render_template('stmt.html')


statement.add_url_rule('/statement/', view_func=StateRequestView.as_view('stat_request'))
