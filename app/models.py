from flask_admin.contrib.pymongo import ModelView
from flask_wtf import FlaskForm
from wtforms import TextField,BooleanField
from wtforms.validators import DataRequired


class ProposalForm(FlaskForm):
    name = TextField('Name')
    lastname = TextField('Lastname')

class ProposalView(ModelView):
    column_list=('name','lastname')
    form = ProposalForm

class UserForm(FlaskForm):
    name = TextField('User')
    admin = TextField('Password')

class UserView(ModelView):
    column_list=('user','pwd')
    form = UserForm
