import json
import csv
from io import TextIOWrapper
from zipfile import ZipFile
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import logging

#File path
json_schema_path = '~/Downloads/sql/schemas/user_address.json'
zip_small_path = '~/Downloads/temp/dataset-small.zip'
csv_small_name = 'dataset-small.csv'
zip_medium_path = '~/Downloads/temp/dataset-medium.zip'
csv_medium_name = 'dataset-medium.csv'
table_name = 'user_address_master'
sql_queries_file = '~/Downloads/sql/queries/result_ingestion_user_address.sql'

create_schema_sql = """ CREATE TABLE IF NOT EXISTS user_address_master {}; """

#Parse schema details from json
with open(json_schema_path, 'r') as j:
    contents = json.loads(j.read())

list_schema = []
for c in contents:
    col_name = c['column_name']
    data_type = c['column_type']
    constraint = c['is_null_able']
    x = [col_name, data_type, constraint]
    list_schema.append(x)

t = ()
for w in list_schema:
    s = ' '.join(w)
    t.append(s)

#Create schema in postgres
create_schema_sql_final = create_schema_sql.format(tuple(t)).replace("'", "")

conn = psycopg2.connect(database="shipping_orders",
                        user='postgres', password='postgres', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute(create_schema_sql_final)

#Load zipped csv to dataframe and then load to postgres
zf = ZipFile(zip_medium_path)
df = pd.read_csv(zf.open(csv_medium_name), header=None)
df.columns =['first_name', 'last_name', 'email', 'address', 'created_at']

engine = create_engine('postgresql://postgres:postgres@localhost:5432/shipping_orders')

#Split into 10 chunks
df.to_sql(table_name, engine, if_exists='append', index=False, chunksize=int(len(df)/10))

#Print ingestion log using python
logging.info("Total inserted rows: {}".format(len(df)))
logging.info("Last created_at: {}".format(df['created_at'].max()))


# Print ingestion log using sql query
file = open(sql_queries_file, 'r')
read_query_file = " ".join(file.readlines())
cursor.execute(read_query_file)
rs = cursor.fetchall()

results = []
attr = ['row', 'created_at']
for row in rs:
    results.append(dict(zip(attr, row)))

logging.info("job is finish. table '{}' has {} rows and last created_at is {}".format(table_name,  results[0]['row'] ,str(results[0]['created_at'])))
