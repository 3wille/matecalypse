from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField

class MateForm(Form):
    contact = StringField('openid')
