from flask import Flask, render_template
from config import Configuration
# from forms import Company
from flask_sqlalchemy import SQLAlchemy
# from models import Company
from flask_migrate import Migrate
# from flask_script import Manager



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *    # import models for migrations



# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = Company()
#     name = None
#
#     if form.validate_on_submit():
#         name = form.name.data()
#         return name
#
#     return render_template('index.html', form=form, name=name)


