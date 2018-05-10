# -*- coding:utf-8 -*-
import sys
import requests,json
from requests import get
from flask import Flask, render_template,request,session
from flask_wtf import Form
import MySQLdb
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, SelectField
from assq import *

app = Flask(__name__)
app.secret_key = 'forget it you can never guess'

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html',data = attr,value = v1)

		
if __name__ == '__main__':
    app.run()


