from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import datetime


from BDManager import BDManager


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    if len(login) > 3 and len(password) > 5:
        if BDManager.get_user(login):
            hash = generate_password_hash(password)
            current_datetime = str(datetime.datetime.now()).split()
            BDManager.add_user(login, hash, current_datetime[0])
            return jsonify({'result': 'success', 'message': 'You have successfully registered'})
        else:
            return jsonify({'result': 'error', 'message': 'A user with that login already exists'})
    else:
        return jsonify({'result': 'error', 'message': 'The data was entered incorrectly'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    if BDManager.check_user(login, password):
        return jsonify({'result': 'success', 'message': 'You have successfully entered'})
    else:
        return jsonify({'result': 'error', 'message': 'There is no such user or the password is entered incorrectly'})


@app.route('/<login>', methods=['GET'])
def get_user(login):
    user = BDManager.enter_user(login)
    if user:
        user_data = {
            'login': user[1],
            'password': user[2],
            'registration_date': user[3]
        }
        return jsonify(user_data)
    else:
        return jsonify({'result': 'error', 'message': 'User not found'})


if __name__ == '__main__':
    BDManager.new_base()
    app.run(host='0.0.0.0', port='7676',  debug = True, ssl_context='adhoc')



