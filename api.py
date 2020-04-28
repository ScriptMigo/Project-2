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

db_connection_str = 'mysql+pymysql://saurin:niruas@home.unheard.org/project_2'
db_connection = create_engine(db_connection_str)

app = Flask(__name__)

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
    results = df.to_json()
    return results

@app.route('/api/v1.0/unemploymentRate',methods=['GET', 'POST'],defaults={'year': None})
@app.route('/api/v1.0/unemploymentRate/<year>')
def unemploymentRate(year):
    #cur = mysql.connection.cursor()
    if(year != None):
        sql = f"select u.*, abb.code from tblUnemployment u inner join tblStateAbbreviations abb on u.state = abb.state where u.year = {year}"
        df = pd.read_sql(sql, con=db_connection)
    else:
        sql = 'select u.*, abb.code from tblUnemployment u inner join tblStateAbbreviations abb on u.state = abb.state'
        df = pd.read_sql(sql, con=db_connection)
    #cur.execute(sql)
    #results = cur.fetchall()
    results = df.to_json()
    return results

@app.route('/api/v1.0/getData',methods=['GET', 'POST'],defaults={'year': None})
@app.route('/api/v1.0/getData/<year>')
def data(year):
    #cur = mysql.connection.cursor()
    if(year != None):
        sql = f"select sdr.State as State, sdr.year as Year, sdr.Value as DivorceRate, u.rate as UnemploymentRate, u.rank as UnemploymentRank, sa.code as Abbv from tblStateDivorceRate sdr inner join tblUnemployment u on sdr.State = u.state and sdr.Year = u.year inner join tblStateAbbreviations sa on sdr.State = sa.State where u.year = {year}"
        df = pd.read_sql(sql, con=db_connection)
    else:
        sql = "select sdr.State as State, sdr.year as Year, sdr.Value as DivorceRate, u.rate as UnemploymentRate, u.rank as UnemploymentRank, sa.code as Abbv from tblStateDivorceRate sdr inner join tblUnemployment u on sdr.State = u.state and sdr.Year = u.year inner join tblStateAbbreviations sa on sdr.State = sa.State"
        df = pd.read_sql(sql, con=db_connection)
    #cur.execute(sql)
    #results = cur.fetchall()
    results = df.to_json()
    return results




if __name__ == '__main__':
    app.run(host='0.0.0.0')
