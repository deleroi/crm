# Customer Accounting System


###### Create a file config.py ######
``````python
    DEBUG = 
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
``````
###### Create a database ######
``````python
import models
from app import db
db.create_all()

###### start app ######

python main.py
``````
