import base64
import os
import hashlib

database = {} #nameとpasswordを保存
salt = base64.b64encode(os.urandom(32))

def signin(name, password):
    value = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 9800
    )
    database[name] = value
    print(database)

def login(name, password):
    value = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 9800
    )
    if(value == database[name]):
        print('ログイン完了しました')
    else:
        print('nameとpasswordが一致しませんでした')

    return value == database[name]


if __name__ == "__main__":
    signin('tetoblog', 'password')
    login('tetoblog','password')

