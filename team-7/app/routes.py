from app import app, get_db, query_db
import sqlite3
# from .models import *
# from flask_login import current_user, login_user
from app.controllers import *
from flask import render_template, flash, redirect, url_for, request, session

@app.route('/')
@app.route('/index')
def index():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    if session['role'] == 0:
        return render_template('dashboard.html')
    else:
        return render_template('dashboardTeach.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    # user = User.query.filter_by(username=username).first()
    # if user is None or not user.check_password(password):
    if not validate(session, username, password):
        flash('Invalid username or password')
        return redirect(url_for('login'))
    # login_user(user, remember=form.remember_me.data)
    session['logged_in'] = True
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')
    username = request.form['username']
    password = request.form['password']
    gender = request.form['gender']
    dob = request.form['dob']
    email = request.form['email']
    income = request.form['income']
    institute = request.form['institute']
    institute_name = request.form['institute_name']
    ethnic_code = request.form['ethnic_code']
    district = request.form['district']
    insert_user({'username': username,
        'password': password,
        'role': 0,
        'gender': gender,
        'email': email,
        'monthly_income': income,
        'tertiary_class': institute,
        'tertiary_name': institute_name,
        'ethnic_code': ethnic_code,
        'district': district
        })
    return redirect(url_for('login'))

@app.route('/survey')
def survey():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    
    return render_template('surveypage.html')

    @app.route('/workshop')
def survey():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    
    return render_template('CreateWorkshop.html')

@app.route('/results')
def results():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    if session['role'] == 0:
        return render_template('studentResultHome.html')
    else:
        return render_template('teacherResultHome.html')
    

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def insert_user(detail_dict):
	keys = list(detail_dict.keys())
	prequel_string = 'INSERT INTO `user_details` (' + ','.join(["`" + str(key) + "`" for key in keys]) + ') '
	format_data = []
	for x in keys:
		if is_number(detail_dict[x]):
			format_data.append(str(detail_dict[x]))
		else:
			format_data.append("'" + detail_dict[x] + "'")
	data_string = 'VALUES (' + ', '.join(format_data) + ');'
	# print("Prequel")
	# print(prequel_string)
	# print("Data")
	# print(data_string)
	query_string = prequel_string + data_string
	with app.app_context():
		# insert the user
		db = get_db()
		cur = get_db().execute(query_string)
		# check for debugging
		print("Newly inserted user")
		new_user = query_db('select * from user_details where username = ?',
	                [detail_dict['username']], one=True)
		if new_user is None:
			print("something is wrong")
		else:
			print("Yay new user!")
			print(new_user)

