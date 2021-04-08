
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy:')
    puppy_gender = StringField('Gender of Puppy:')
    puppy_breed = StringField('Breed of Puppy:')
    puppy_age = StringField('Age of Puppy:(Years)')
    puppy_color = StringField('Color of Puppy:')
    puppy_height = StringField('Height of Puppy(cm):')
    puppy_weight = StringField('Weight of Puppy(lbs):')
    submit = SubmitField('Add Puppy')

class AddOwner(FlaskForm):
    oname = StringField('Owner Name:')
    address = StringField('Owner Address:')
    zip = StringField('Zipcode:')
    f_id = IntegerField('Puppy id:')
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')
