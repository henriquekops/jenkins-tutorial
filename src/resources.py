# METADATA
__author__='Henrique Kops'
__date__='2019-06-14'
__version__=1.0

from flask import Flask

app = Flask('Jenkins Tutorial API')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s, you\'re awesome!\n' % name