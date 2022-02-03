from app import app, db
from flask import render_template, flash, redirect, url_for, request
from models import Company, Contact
from forms import CompanyForm


@app.route('/')
def card():
    cards = Company.query.all()
    return render_template('company_table.html', cards=cards)



@app.route('/<slug>')
def company_detail(slug):
    detail = Company.query.get(slug)
    contact = Contact.query.filter(Contact.company_id == detail.id).all()
    return render_template('/company_card.html', detail=detail, contact=contact)

@app.route('/add', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    # if request.method == 'POST' and form.validate_on_submit():
    if request.method == 'POST':
        name = form.name.data
        main_phone = form.main_phone.data
        second_phone = form.second_phone.data
        email = form.email.data
        second_email = form.second_email.data
        ynp = form.ynp.data
        rating = form.rating.data
        web = form.web.data
        industry = form.industry.data
        comment = form.comment.data
        bank_name = form.bank_name.data
        bank_account = form.bank_account.data
        country = form.country.data
        company_adr = form.company_adr.data

    #     add data to DATABASE
        company = Company(name=name, main_phone=main_phone, second_phone=second_phone, email=email, second_email=second_email,
            ynp=ynp, rating=rating, web=web, industry=industry, comment=comment, bank_name=bank_name,
            bank_account=bank_account, country=country, adress=company_adr)

        db.session.add(company)
        db.session.commit()
        flash('клиент создан', "success")
        return redirect(url_for('card'))

    return render_template('company_add.html', form=form)

