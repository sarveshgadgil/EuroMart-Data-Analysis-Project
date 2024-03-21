#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import OperationalError
from sqlalchemy.schema import CreateSchema

# Prompting user for MySQL connection details
db_username = input("Enter MySQL username: ")
db_password = input("Enter MySQL password: ")
db_host = input("Enter MySQL host (default: localhost): ") or 'localhost'
db_port = input("Enter MySQL port (default: 3306): ") or '3306'
db_database = input("Enter MySQL database name: ")

# Establish connection to MySQL database
connection_string = f'mysql://{db_username}:{db_password}@{db_host}:{db_port}'
engine = create_engine(connection_string)

# Check if the database exists, if not, create it
try:
    with engine.connect() as connection:
        inspector = inspect(engine)
        if not inspector.has_schema(db_database):
            connection.execute(CreateSchema(db_database))
            print(f"Database '{db_database}' created successfully.")
except OperationalError as e:
    print(f"Error: {e}")

# Establish connection to the specified database
connection_string = f'mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}'
engine = create_engine(connection_string)

# Read data from Excel into DataFrame
df = pd.read_excel('EuroMart Data Store.xlsx')

# Prompting user for table name
table_name = input("Enter table name: ")

# Write DataFrame to MySQL database
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print("Data copied from Excel to MySQL successfully.")

