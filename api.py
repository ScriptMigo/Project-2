# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'saurin'
app.config['MYSQL_PASSWORD'] = 'niruas'
app.config['MYSQL_DB'] = 'project_2'
app.config['MYSQL_HOST'] = 'home.unheard.org'

mysql = MySQL(app)


@app.route('/api/v1.0/avgDivorceRate',methods=['GET', 'POST'],defaults={'year': None})
@app.route('/api/v1.0/avgDivorceRate/<year>')
def avgDivorceRate(year):
    cur = mysql.connection.cursor()
    if(year != None):
        sql = f'select * from tblAvgDivorceRate where year = {year}'
    else:
        sql = 'select * from tblAvgDivorceRate'
    cur.execute(sql)
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/v1.0/stateDivorceRate',methods=['GET', 'POST'],defaults={'state': None})
@app.route('/api/v1.0/stateDivorceRate/<state>')
def stateDivorceRate(state):
    cur = mysql.connection.cursor()
    if(state != None):
        sql = f"select * from tblStateDivorceRate where state = '{state}'"
    else:
        sql = 'select * from tblStateDivorceRate'
    cur.execute(sql)
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/v1.0/unemploymentRate',methods=['GET', 'POST'],defaults={'state': None})
@app.route('/api/v1.0/unemploymentRate/<state>')
def unemploymentRate(state):
    cur = mysql.connection.cursor()
    if(state != None):
        sql = f"select * from tblUnemployment where state = '{state}'"
    else:
        sql = 'select * from tblUnemployment'
    cur.execute(sql)
    results = cur.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')