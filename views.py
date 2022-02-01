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
    # detail = Company.query.filter(Company.slug == slug).first()
    detail = Company.query.get(slug)
    # contact = Contact.query.filter(Contact.company_id == detail.id).all()
    contact = Contact.query.filter(Contact.company_id == detail.id).all()
    # contact = Contact.query.all()
    return render_template('/company_card.html', detail=detail, contact=contact)

@app.route('/add', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        ynp = form.ynp.data
        comment = form.comment.data
        bank_name = form.bank_name.data
        bank_account = form.bank_account.data
        email = form.email.data
        country = form.country.data

    #     add data to DATABASE
        company = Company(name=name, ynp=ynp, comment=comment, bank_name=bank_name, bank_account=bank_account, email=email, country=country)
        db.session.add(company)
        db.session.commit()
        flash('MESSAGE RECIVED', "success")
        return redirect(url_for('card'))

    return render_template('company_add.html', form=form)