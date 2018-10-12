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

"""
Property - index map: map each property (of the user) to its corresponding
index in the user details vector
"""
ppt_idx_map = {
	'index': 0,
	'username': 1,
	'password': 2,
	'gender': 3,
	'email': 4,
	'ethnic_code': 5,
	'monthly_income': 6,
	'district': 7, 
	'tertiary_class': 8, 
	'tertiary_name': 9
}

# Initialize the database with this command
# Remember to delete jpchase.db everytime you run this
init_db()

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
get_all_user()

"""
Example usage: Add a user to the database
"""

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
	print("Prequel")
	print(prequel_string)
	print("Data")
	print(data_string)
	query_string = prequel_string + data_string
	with app.app_context():
		# insert the user
		db = get_db()
		cur = get_db().execute(query_string)
		db.commit()
		# check for debugging
		print("Newly inserted user")
		new_user = query_db('select * from user_details where username = ?',
	                [detail_dict['username']], one=True)
		if new_user is None:
			print("Fuck something is wrong")
		else:
			print("Yay new user!")
			print(new_user)

"""
Sample usage for insert_user - a dictionary of 
"""
insert_user({
	'index': 2, 
	'username': '9780c4b6faf1183a7ec50761e4d7c172',
	'password': 'sample',
	'gender': 'Female', 
	'ethnic_code': 4,
	#'monthly_income': '$7000 to $8,999',
	'district': 14,
	#'tertiary_class': 'ITE',
	'tertiary_name': 'Ite College East'
	})

"""
Example: retrieve survey questions from the database
-- relevant for student view
Return: a list of questions, each being a dictionary that looks like:
{ 'index': 0, 'content': 'content of the question'}
"""
def get_survey_questions():
	with app.app_context():
		qns_list = []
		for qns in query_db('select * from questions_list'):
			# testing
			print(qns)
			qns_list.append(qns)
		return qns_list

# testing
get_survey_questions()

"""
Track which student (id) do survey for which workshop at what time
"""
def save_survey_frame(stu_idx, wsname, datestr):
	with app.app_context():
		db = get_db()
		query_string = 'INSERT INTO `surveys_list` (`user_index`, `workshop_name`, `date`) VALUES '
		data_string = '(' + str(stu_idx) + ', "' + wsname + '", "' + datestr + '");'
		db.execute(query_string)
		db.commit()
		print("Save survey framework completed!")

"""
Create a workshop
wsdate in Datetime ISO1806 format
"""
def create_workshop(wsname, wsdate):
	with app.app_context():
		query_string = 'INSERT INTO `workshop_list` (`workshop_name`, `date`) VALUES '
		data_string = '("' + wsname + '", "' + wsdate + '");'
		db = get_db()
		cur = db.execute(query_string + data_string)
		db.commit()
		print("Add success")

create_workshop("Living on the edge", "2018-10-12 12:00:00.000")

def get_workshop(wsname, wsdate):
	with app.app_context():
		res = query_db('select * from workshop_list where workshop_name = ? and date = ?',
	                [wsname, wsdate])
		return res

ws = get_workshop("Living on the edge", "2018-10-12 12:00:00.000")
print(ws)

"""
Example: save survey result to the database
Need:
- survey_dict have user_index key
- each key is the index of the question in the database (int)
- value at each key is the result of the question (string)
"""
def save_survey_result(survey_dict):
	usr_idx = survey_dict['user_index']
	ws_idx = survey_dict['workshop_index']
	keys = list(survey_dict.keys())
	key_len = len(keys)
	query_string = 'INSERT INTO `response_list` (`workshop_index`, `user_index`, `question_index`, `score`) VALUES '
	for i in range(2, key_len):
		x = keys[i]
		# answer to qns x is survey_dict[x]
		data_string = '(' + str(ws_idx) + ', ' + str(usr_idx) + ', ' + str(x) + ', ' + str(survey_dict[x]) + ')'
		print(data_string)
		if not i == key_len - 1:
			data_string = data_string + ', '
		query_string = query_string + data_string
	query_string = query_string + ';'
	with app.app_context():
		# insert the user
		db = get_db()
		cur = get_db().execute(query_string)
		db.commit()
		# check for debugging
		print("Newly inserted survey result")
		new_result = query_db('select * from response_list where user_index = ?',
	                [usr_idx])
		print(new_result) # expect all the result

"""
Sample usage of save_survey
"""
save_survey_result({
	'user_index': 1,
	'workshop_index': 1,
	1: 7,
	12: 4,
	56: 5
	})
save_survey_result({
	'user_index': 2,
	'workshop_index': 1,
	13: 7,
	12: 1,
	57: 5
	})

"""
Example: retrieve survey results
for student a, question b
Return: a list of dictionaries, each being result of a particular question
"""
def get_survey_result_by_student(stu_idx):
	with app.app_context():
		result = query_db('select * from response_list where user_index = ?',
	                [stu_idx])
		print("Required result is:")
		print(result)
	return result

def get_survey_result_by_question(qn_idx):
	with app.app_context():
		result = query_db('select * from response_list where question_index = ?',
	                [qn_idx])
		print("Required result is:")
		print(result)
	return result

"""
Sample usage of get_survey_result
"""
get_survey_result_by_student(1) # expect 3 responses
get_survey_result_by_question(12) # expect 2 responses