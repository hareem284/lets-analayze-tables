#importing sqlite3
import sqlite3
# importing pandas
import pandas as pd
connection=sqlite3.connect('database.sqlite')
print("connection is estaished.you are lucky!")
# now starting code for pandas
tables=pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';",connection)
print(tables)
read=pd.read_sql("SELECT * FROM Match;",connection)
print(read.info())