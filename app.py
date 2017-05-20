import redis, string
from flask import Flask, request, redirect

app = Flask(__name__)
r = redis.Redis()
ALPHABET = string.digits + string.ascii_letters

def encode(n):
    out = ''
    while n:
        n, rem = divmod(n, 62)
        out = ALPHABET[rem] + out
    return out or '0'

@app.route('/<code>')
def follow(code):
    target = r.get(f'url:{code}')
    return redirect(target) if target else ('404', 404)
# TODO: expire keys
# TODO: expire keys
