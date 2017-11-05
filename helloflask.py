import sqlite3

from flask import Flask, request, session, render_template, g, redirect ,url_for, \
    abort, flash

#from __future__ import with_statement
from contextlib import closing

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def index():
    return '상자아이의 웹페이지 1'
@app.route('/hello/')
def hello():
    return 'Hello World!'

@app.route('/user/<username>/')
def show_user_profile(username):
#유저 이름을 보여줌
    #app.logger.debug('RETRIEVE DATA - USER ID : %s' % username)
    #app.logger.debug('RETRIEVE DATA - Check Compelete')
    return  'User %s' % username
#with app.test_request_context():
    #print url_for('index')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')

