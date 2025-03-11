import hashlib

db = {}

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')