import pandas as pd
import csv
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

response_file = "responses_180815.csv"
response_df = pd.read_csv(response_file)
# all column names
column_names = list(response_df.columns.values)
l = len(column_names)
# add user
all_users = [{'password': 'sample'} for i in range(response_df.shape[0])]
for i in range(8):
	if not i == 6:
		fld = column_names[i]
		if i == 0:
			fld = 'username'
		elif i == 1:
			fld = 'gender'
		elif i == 2:
			fld = 'ethnic_code'
		elif i == 3:
			fld = 'monthly_income'
		elif i == 4:
			fld = 'district'
		elif i == 5:
			fld = 'tertiary_class'
		elif i == 7:
			fld = 'tertiary_name'
		for j in range(response_df.shape[0]):
			info = response_df[column_names[i]][j]
			if is_number(info):
				if math.isnan(float(info)):
					info = "N.A."
			all_users[j][fld] = info

# save all users to database
import sqlite3
from flask import g
from flask import Flask

app = Flask(__name__)

DATABASE = 'jpchase.db'

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		db.row_factory = make_dicts
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def insert_user(detail_dict):
	keys = list(detail_dict.keys())
	prequel_string = 'INSERT INTO `user_details` (' + ','.join(["`" + str(key) + "`" for key in keys]) + ') '
	format_data = []
	for x in keys:
		if is_number(detail_dict[x]):
			format_data.append(str(detail_dict[x]))
		else:
			format_data.append('"' + detail_dict[x] + '"')
	data_string = 'VALUES (' + ', '.join(format_data) + ');'
	query_string = prequel_string + data_string
	with app.app_context():
		# insert the user
		db = get_db()
		cur = get_db().execute(query_string)
		db.commit()

init_db()

for user in all_users:
	insert_user(user)

"""
Example usage: retrieve all users from the database
"""
def get_all_user():
	all_users = []
	with app.app_context():
		for user in query_db('select * from user_details'):
			all_users.append(user)
			print(user)
	return all_users

"""
Sample get_all_user usage
"""
#get_all_user()

def save_survey_result(survey_dict):
	usr_idx = survey_dict['user_index']
	ws_idx = survey_dict['workshop_index']
	keys = list(survey_dict.keys())
	key_len = len(keys)
	for i in range(2, key_len):
		x = keys[i]
		val = survey_dict[x]
		if is_number(val):
			if math.isnan(float(val)):
				val = '"N.A."'
				query_string = 'INSERT INTO `response_list` (`workshop_index`, `user_index`, `question_index`, `word`) VALUES '
				data_string = '(' + str(ws_idx) + ', ' + str(usr_idx) + ', ' + str(x) + ', ' + val + ');'
				query_string = query_string + data_string
				db = get_db()
				cur = get_db().execute(query_string)
				db.commit()
			else:
				val = str(val)
				query_string = 'INSERT INTO `response_list` (`workshop_index`, `user_index`, `question_index`, `score`) VALUES '
				data_string = '(' + str(ws_idx) + ', ' + str(usr_idx) + ', ' + str(x) + ', ' + val + ');'
				query_string = query_string + data_string
				db = get_db()
				cur = get_db().execute(query_string)
				db.commit()
		else:
			val = '"' + val + '"'
			query_string = 'INSERT INTO `response_list` (`workshop_index`, `user_index`, `question_index`, `word`) VALUES '
			data_string = '(' + str(ws_idx) + ', ' + str(usr_idx) + ', ' + str(x) + ', ' + val + ');'
			query_string = query_string + data_string
			db = get_db()
			cur = get_db().execute(query_string)
			db.commit()
	"""
	with app.app_context():
		# check for debugging
		#print("Newly inserted survey result")
		#new_result = query_db('select * from response_list where user_index = ?',
	    #            [usr_idx])
		#print(new_result) # expect all the result
	"""
for ii in range(len(all_users)):
	usr_idx = ii + 1
	ws_idx = 1
	offset = 7
	for jj in range(8,l-4):
		fld = column_names[jj]
		qn_idx = jj - offset
		info = response_df[fld][qn_idx]
		if is_number(info):
			if math.isnan(float(info)):
				info = "N.A."
		with app.app_context():
			save_survey_result({
				'user_index': usr_idx,
				'workshop_index': ws_idx,
				qn_idx: info
				})
