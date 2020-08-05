from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Angelica'}
    posts = [
        {
            'author': {'username': 'Ana'},
            'body': 'Chocolate chip cookies changed my life'
        },
        {
            'author': {'username': 'Pedro'},
            'body': 'I love chicken katsu so much!'
				}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)