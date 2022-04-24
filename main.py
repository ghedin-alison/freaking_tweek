from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Olá!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



ImportError: cannot import name 'escape' from 'jinja2' (/usr/local/lib/python3.9/site-packages/jinja2/__init__.py)

