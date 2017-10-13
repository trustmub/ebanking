from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask.views import View, MethodView
from forms.bill_form import BillerForm, ScheduleForm

bill = Blueprint('bill', __name__)


class BillPayView(View):
    methods = ['POST', 'GET']
    decorators = []

    def dispatch_request(self):
        form = BillerForm()
        dd_form = ScheduleForm()
        if request.method == 'POST':
            print("inside the post")
            if not form.validate_on_submit():
                print("please enter the correct details")
                return redirect(url_for('bill.bill_pay'))
            else:
                print("valid entries")
                account = request.form['account']
                amount = request.form['amount']
                bill_type = request.form['billType']
                print(f" account is : {account} and the amount is {amount} and the biller type is {bill_type}")
                return redirect(url_for('bill.bill_pay'))
        return render_template('bill_payment.html', form=form, ddform=dd_form)


class PaymentScheduleView(View):
    methods = ['POST', 'GET']
    decorators = []

    def dispatch_request(self):
        dd_form = ScheduleForm(request.form)
        form = BillerForm()

        if request.method == 'POST':
            biller = dd_form.biller.data
            service_account = dd_form.service_account.data
            frequency = dd_form.frequency.data
            start_date = dd_form.start_date.data
            amount = dd_form.amount.data
            accept_toc = dd_form.accept_toc.data

            flash("form validated well")
            return redirect(url_for('bill.schedule_pay'))
        return render_template('bill_payment.html', form=form, ddform=dd_form)


bill.add_url_rule('/bill/', view_func=BillPayView.as_view('bill_pay'))
bill.add_url_rule('/bill/schedule_payment', view_func=PaymentScheduleView.as_view('schedule_pay'))
