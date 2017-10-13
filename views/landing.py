from flask import Blueprint, request, render_template, url_for, redirect
from flask.views import View
from controller.core import user_required

landing = Blueprint('landing', __name__)


class HomeView(View):
    methods = ['POST', 'GET']
    decorators = []

    def dispatch_request(self):
        if request.method == 'POST':
            return None
        return render_template('landing.html')


landing.add_url_rule('/landing/', view_func=HomeView.as_view('home'))
