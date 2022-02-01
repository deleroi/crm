import re

from app import db
from datetime import datetime

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s).lower()

class Company(db.Model):
    """" Company table model with overriding the __init__ magic method to automatically generate and
     add the slug column to the table """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ynp = db.Column(db.String(20))
    comment = db.Column(db.Text, default='')
    bank_name = db.Column(db.String(50))
    bank_account = db.Column(db.String(50))
    email = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    country = db.Column(db.String(50), default='дом')
    contact = db.relationship('Contact', backref='employee', lazy=True)

    def __init__(self, *args, **kwargs):
        super(Company, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)


class Contact(db.Model):
    """" Contact table model with overriding the __init__ magic method to automatically generate and
         add the slug column to the table """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    comment = db.Column(db.Text, default='')
    email = db.Column(db.String(50))
    slug = db.Column(db.String(140), unique=True)
    position = db.Column(db.String(100))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)


class Countrys(db.Model):
    id = db.Column(db.String(64), primary_key=True, nullable=False)
    value = db.Column(db.String(64))

    def __repr__(self):
        return '%r' % (self.value)
