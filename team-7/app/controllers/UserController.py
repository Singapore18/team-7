import sqlite3
from app import query_db
from werkzeug.security import check_password_hash

def validate(session, username, password):
    users = query_db('select id, role, username, password from `user_details` where role = 0')
    print(users)
    # return users[0][1] == password
    # for user in query_db('select * from user_details'):
    #     print(user)
    for user in users:
        if user[2] == username and user[3] == password:
            session['id'] = user[0]
            session['role'] = user[1]
            return True
    return False