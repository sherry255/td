#!/usr/bin/env python
#coding:utf-8
import os

from DateTime import datetime
from flask import Flask,render_template, session, redirect, url_for
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

SECRET_KEY = '?7\x93\xb9\xba\x97\xf3\xaaA\x10t\x03y\xa1\xb1\xd4\xe7\x9f\xa3\xb5X&|\xc6'
SQLALCHEMY_DATABASE_URI='sqlite:///E:\\path\\to\\foo.db'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

manager = Manager(app)
db = SQLAlchemy(app)


class Todo(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_on = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super(Todo, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Todo '%s'>" % self.title

    def store_to_db(self):


        db.session.add(self)
        db.session.commit()

    def delete_todo(self):


        db.session.delete(self)
        db.session.commit()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')





@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



if __name__ == '__main__':
    manager.run()
