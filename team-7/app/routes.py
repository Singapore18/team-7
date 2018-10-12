from app import app
# from .models import *
# from flask_login import current_user, login_user
from flask import render_template, flash, redirect, url_for, request

@app.route('/')
@app.route('/index')
def index():
    # if not current_user.is_authenticated:
    #     return redirect(url_for('login'))
    return "Hello, World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    # user = User.query.filter_by(username=username).first()
    # if user is None or not user.check_password(password):
    #     flash('Invalid username or password')
    #     return redirect(url_for('login'))
    # login_user(user, remember=form.remember_me.data)
    return redirect(url_for('index'))

