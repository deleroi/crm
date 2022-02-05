from app import app, db
from flask import render_template, flash, redirect, url_for, request, session, g
from models import Company, Contact
from forms import CompanyForm, ContactForm



events = [
    {
      'todo': 'first todo',
      'date': '2022-02-05'
    },
{
      'todo': 'second todo',
      'date': '2022-02-06'
    },
]

@app.route('/')
def card():
    cards = Company.query.all()
    return render_template('company_table.html', cards=cards)



@app.route('/<slug>')
def company_detail(slug):
    detail = Company.query.get(slug)
    session['card_id'] = detail.id
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


@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        position = form.position.data
        comment = form.comment.data
        company_id = session.get('card_id')

    # #     add data to DATABASE
        contact = Contact(name=name, phone=phone, email=email, position=position, comment=comment,
                          company_id=company_id)
        db.session.add(contact)
        db.session.commit()
        flash('контакт создан', "success")
        return redirect(url_for('company_detail', slug=company_id))

    return render_template('contact_add.html', form=form)


@app.route('/calendar')
def calendar():

    return render_template('calendar.html', events=events)