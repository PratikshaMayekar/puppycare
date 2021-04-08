import os
from forms import  AddForm , DelForm , AddOwner
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os.path import join, dirname, realpath
import pandas as pd
import sqlalchemy





app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:reyansh123@localhost:3306/puppycare"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Owner(db.Model):
    __tablename__ = 'owners'
    oid = db.Column(db.Integer, primary_key = True)
    oname = db.Column(db.Text)
    address = db.Column(db.Text)
    zip = db.Column(db.Text)
    f_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self,oname,address,zip,f_id):
        self.oname = oname
        self.address = address
        self.zip = zip
        self.f_id = f_id

    def __repr__(self):
        return f"Owner id: {self.oid}  Name: {self.oname}  Address  :{self.address}  Zipcode : {self.zip} Puppy ID {self.f_id}"


class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    puppy_gender =db.Column(db.Text)
    puppy_breed =db.Column(db.Text)
    puppy_age =db.Column(db.Integer)
    puppy_color = db.Column(db.Text)
    puppy_height = db.Column(db.Integer)
    puppy_weight = db.Column(db.Integer)


    def __init__(self,name,puppy_gender, puppy_breed, puppy_age,puppy_color, puppy_height, puppy_weight):
        self.name = name
        self.puppy_gender = puppy_gender
        self.puppy_breed = puppy_breed
        self.puppy_age = puppy_age
        self.puppy_color = puppy_color
        self.puppy_height = puppy_height
        self.puppy_weight = puppy_weight


    def __repr__(self):
        return f"Puppy ID :{self.id} Name: {self.name}  Age : {self.puppy_age}   "



###################################

#  upload Folder

#############################

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER



############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')

def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_gender = form.puppy_gender.data
        puppy_breed = form.puppy_breed.data
        puppy_age = form.puppy_age.data
        puppy_color = form.puppy_color.data
        puppy_height = form.puppy_height.data
        puppy_weight = form.puppy_weight.data

        # Add new Puppy to database
        new_pup = Puppy(name,puppy_gender,puppy_breed,puppy_age,puppy_color,puppy_height,puppy_weight)
        #new_pup.name=name
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html',form=form)

@app.route('/owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwner()
    if form.validate_on_submit():
        oname = form.oname.data
        address = form.address.data
        zip = form.zip.data
        f_id= form.f_id.data

        # Add new O to database
        new_owner = Owner(oname,address,zip,f_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_own'))

    return render_template('owner.html',form=form)

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/listowner')
def list_own():
    own = Owner.query.all()
    return render_template('listowner.html', owners=own)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)

# Get the uploaded files
# Root URL
@app.route('/upload')
def upload():
     # Set The upload HTML template '\templates\index.html'
    return render_template('upload.html')




# Get the uploaded files
@app.route("/upload", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path)
          # save the file
      return redirect(url_for('index'))

def parseCSV(file_path):
      # CVS Column Names
      col_names = ['name','puppy_gender', 'puppy_breed','puppy_age','puppy_color','puppy_height','puppy_weight']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(file_path,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
                  name = (row['name'])
                  puppy_gender = (row['puppy_gender'])
                  puppy_breed = (row['puppy_breed'])
                  puppy_age = (row['puppy_age'])
                  puppy_color = (row['puppy_color'])
                  puppy_height = (row['puppy_height'])
                  puppy_weight = (row['puppy_weight'])

                  # Add new Puppy to database
                  Addpup = Puppy(name,puppy_gender,puppy_breed,puppy_age,puppy_color,puppy_height,puppy_weight)
                  #new_pup.name=name
                  db.session.add(Addpup)
                  db.session.commit()
                  print(i,row['name'])


if __name__ == '__main__':
    app.run(debug=True)
