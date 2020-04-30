# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, jsonify
from flask_mysqldb import MySQL
import pandas as pd

from sqlalchemy import create_engine
import pymysql
from flask_cors import CORS

db_connection_str = 'mysql+pymysql://saurin:niruas@home.unheard.org/project_2'
db_connection = create_engine(db_connection_str)

app = Flask(__name__)
CORS(app)

'''
app.config['MYSQL_USER'] = 'saurin'
app.config['MYSQL_PASSWORD'] = 'niruas'
app.config['MYSQL_DB'] = 'project_2'
app.config['MYSQL_HOST'] = 'home.unheard.org'

mysql = MySQL(app)
'''

@app.route('/api/v1.0/avgDivorceRate',methods=['GET', 'POST'],defaults={'year': None})
@app.route('/api/v1.0/avgDivorceRate/<year>')
def avgDivorceRate(year):
    #cur = mysql.connection.cursor()
    if(year != None):
        sql = f'select * from tblAvgDivorceRate where year = {year}'
        df = pd.read_sql(sql, con=db_connection)
    else:
        sql = 'select * from tblAvgDivorceRate'
        df = pd.read_sql(sql, con=db_connection)
    #cur.execute(sql)
    #results = cur.fetchall()
    results = df.to_json()
    return results

@app.route('/api/v1.0/stateDivorceRate',methods=['GET', 'POST'],defaults={'year': None})
@app.route('/api/v1.0/stateDivorceRate/<year>')
def stateDivorceRate(year):
    #cur = mysql.connection.cursor()
    if(year != None):
        sql = f"select d.*, abb.code from tblStateDivorceRate d inner join tblStateAbbreviations abb on d.state = abb.state where d.year = {year}"
        df = pd.read_sql(sql, con=db_connection)
    else:
        sql = 'select d.*, abb.code from tblStateDivorceRate d inner join tblStateAbbreviations abb on d.state = abb.state'
        df = pd.read_sql(sql, con=db_connection)
    #cur.execute(sql)
    #results = cur.fetchall()
    results = df.to_json(orient="records")
    return results

@app.route('/api/v1.0/getData',methods=['GET', 'POST'])
def unemploymentRate():
    #cur = mysql.connection.cursor()
    sql = f"select * from JoinedData2"
    df = pd.read_sql(sql, con=db_connection)
    #cur.execute(sql)
    #results = cur.fetchall()
    results = df.to_json(orient="records")
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0')
