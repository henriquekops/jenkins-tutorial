from flask import Flask

app = Flask('Jenkins Tutorial API')

@app.route('/')
def index():
    return 'Hello World!'
