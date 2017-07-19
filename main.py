from flask import Flask, render_template, request, redirect
from datetime import date, datetime as dt
from models import leads, notes
from peewee import *
from conf import def_auth_data
from fill_data import auth, fill_leads, fill_notes

app = Flask(__name__)


@app.route('/update', methods=['GET', 'POST'])
def update():
    alert = False
    if request.method == 'POST':
        print(request.form)
        if not request.form.get('domain') or not request.form.get('email') or not request.form.get('api_key'):
            auth_api_key = def_auth_data['auth_api_key']
            auth_email = def_auth_data['auth_email']
            auth_domain = def_auth_data['auth_domain']
        else:
            auth_api_key = request.form.get('api_key')
            auth_email = request.form.get('email')
            auth_domain = request.form.get('domain')
        # if
        upload_time = dt.now()
        try:
            s = auth(auth_api_key, auth_email, auth_domain)
            if s:
                fill_leads(s, upload_time, auth_domain)
                # success = True
                return redirect('/')
            else:
                alert = True
                # success = False
        except:
            alert = True
            # success = False
    return render_template('update.html', alert=alert)#, success=success)


@app.route('/')
def index():
    may = leads.select().where(leads.date_create >= date(2017, 5, 1), leads.date_create < date(2017, 6, 1))
    juni = leads.select().where(leads.date_create >= date(2017, 6, 1), leads.date_create < date(2017, 7, 1))
    juli_17 = leads.select().where(leads.date_create >= date(2017, 7, 1), leads.date_create <= date(2017, 7, 17))
    juli = leads.select().where(leads.date_create >= date(2017, 7, 1), leads.date_create < date(2017, 8, 1))
    print(dt.now())
    print(leads.select(fn.SUM(leads.price)).where(leads.status_id == 142).scalar())

    # dohod
    doh_usp_5 = may.select(fn.SUM(leads.price)).where(leads.status_id == 142).scalar()
    doh_usp_6 = juni.select(fn.SUM(leads.price)).where(leads.status_id == 142).scalar()
    doh_usp_7 = juli.select(fn.SUM(leads.price)).where(leads.status_id == 142).scalar()
    doh_usp_7_17 = juli_17.select(fn.SUM(leads.price)).where(leads.status_id == 142).scalar()

    # leads
    leads_5 = may.select().where(leads.status_id == 142)
    leads_6 = juni.select().where(leads.status_id == 142)
    leads_7_17 = juli_17.select().where(leads.status_id == 142)
    leads_7 = juli.select().where(leads.status_id == 142)

    # leads_count
    leads_count_5 = leads_5.count()
    leads_count_6 = leads_6.count()
    leads_count_7_17 = leads_7_17.count()
    leads_count_7 = leads_7.count()

    # users_count
    users_count_5 = leads_5.group_by(leads.responsible_user_id).count()
    users_count_6 = leads_6.group_by(leads.responsible_user_id).count()
    users_count_7_17 = leads_7_17.group_by(leads.responsible_user_id).count()
    users_count_7 = leads_7.group_by(leads.responsible_user_id).count()

    # av_cheque
    av_cheque_5 = doh_usp_5 / leads_count_5 if doh_usp_5 and leads_count_5 else 0
    av_cheque_6 = doh_usp_6 / leads_count_6 if doh_usp_6 and leads_count_6 else 0
    av_cheque_7_17 = doh_usp_7_17 / leads_count_7_17 if doh_usp_7_17 and leads_count_7_17 else 0
    av_cheque_7 = doh_usp_7 / leads_count_7 if doh_usp_7 and leads_count_7 else 0

    # leads_confirm
    leads_confirm_5 = may.select().where((leads.status_id == 15636931) | (leads.status_id == 15636928))
    leads_confirm_6 = juni.select().where((leads.status_id == 15636931) | (leads.status_id == 15636928))
    leads_confirm_7_17 = juli_17.select().where((leads.status_id == 15636931) | (leads.status_id == 15636928))
    leads_confirm_7 = juli.select().where((leads.status_id == 15636931) | (leads.status_id == 15636928))

    # leads_confirm_count
    leads_confirm_count_5 = leads_confirm_5.count()
    leads_confirm_count_6 = leads_confirm_6.count()
    leads_confirm_count_7_17 = leads_confirm_7_17.count()
    leads_confirm_count_7 = leads_confirm_7.count()

    # users_confirm_count
    users_confirm_count_5 = leads_confirm_5.group_by(leads.responsible_user_id).count()
    users_confirm_count_6 = leads_confirm_6.group_by(leads.responsible_user_id).count()
    users_confirm_count_7_17 = leads_confirm_7_17.group_by(leads.responsible_user_id).count()
    users_confirm_count_7 = leads_confirm_7.group_by(leads.responsible_user_id).count()

    return render_template('index.html',
                           doh_usp_5=doh_usp_5,
                           doh_usp_6=doh_usp_6,
                           doh_usp_7=doh_usp_7,
                           doh_usp_7_17=doh_usp_7_17,

                           leads_count_5=leads_count_5,
                           leads_count_6=leads_count_6,
                           leads_count_7_17=leads_count_7_17,
                           leads_count_7=leads_count_7,

                           leads_confirm_count_5=leads_confirm_count_5,
                           leads_confirm_count_6=leads_confirm_count_6,
                           leads_confirm_count_7_17=leads_confirm_count_7_17,
                           leads_confirm_count_7=leads_confirm_count_7,

                           users_count_5=users_count_5,
                           users_count_6=users_count_6,
                           users_count_7_17=users_count_7_17,
                           users_count_7=users_count_7,

                           av_cheque_5=av_cheque_5,
                           av_cheque_6=av_cheque_6,
                           av_cheque_7_17=av_cheque_7_17,
                           av_cheque_7=av_cheque_7,

                           users_confirm_count_5=users_confirm_count_5,
                           users_confirm_count_6=users_confirm_count_6,
                           users_confirm_count_7_17=users_confirm_count_7_17,
                           users_confirm_count_7=users_confirm_count_7,
                           )


if __name__ == "__main__":
    app.run(debug=True)
