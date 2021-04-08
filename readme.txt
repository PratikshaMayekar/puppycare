
1) Install below modules

pip install pandas
pip install sqlalchemy
pip install flask_sqlalchemy
pip install flask_migrate
pip install flask

2) create environment and activate

conda create  -n puppycare
conda activate puppycare

3) create schema structure in mysql database

python schemacreate.py

4) Execute below file to start Flast App for "Puppy Care"

python adoption_site.py

5)  Execute below file to get statistics

python Panda_DF.py
