
import sys, os

from flask import Flask, render_template, url_for
from flask_frozen import Freezer
from jinja2 import Environment, PackageLoader, select_autoescape

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config['FREEZER_DESTINATION'] = './docs/'
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=5007)


app.run(host='0.0.0.0', port=5005)
