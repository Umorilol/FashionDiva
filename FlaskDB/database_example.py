# Based on example here https://hevodata.com/learn/flask-mysql/#51

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

#Creating a connection cursor
cursor = mysql.connection.curson()

#Executing SQL Statements
cursor.execute(''' CREATE TABLE table_name(field1, field2) ''')
cursor.execute('''INSERT INTO table_name VALUES(v1, v2) ''')
cursor.execute('''DELETE FROM table_name WHERE condition) ''')

#Saving the Actions performed on the DB
mysql.conection.commit()

#Closing the cursor
cursor.close()

