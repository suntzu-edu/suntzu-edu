
import sys

from flask import Flask, render_template, url_for

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



app.run(host='0.0.0.0', port=5005)
