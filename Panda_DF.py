import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:reyansh123@localhost:3306/puppycare')
pshape=pd.read_sql_query("select * from puppies",engine)
oshape=pd.read_sql_query("select * from owners",engine)
pcolor=pd.read_sql_query("select count(*) as 'COUNT PUPPIES' , puppy_color as 'COLOR' from puppies group by puppy_color",engine)
powner=pd.read_sql_query("select concat(o.oname,' is the owner of puppy ', p.name ,'.')  as 'Puppy Owners list' from owners o, puppies p where p.id=o.f_id;",engine)

print("Column counts in Puppies table {}".format(pshape.shape[1]))
print("Record counts in Puppies table {}".format(pshape.shape[0]))
print("Column counts in Owners table {}".format(oshape.shape[1]))
print("Record counts in Owners table {}".format(oshape.shape[0]))
print(pcolor)
print(powner)
