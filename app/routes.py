from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    posts = [
        {
            'author': {'username': 'Diana'},
            'body': 'My city is so beautiful!'
        },
        {
            'author': {'username': 'Kevin'},
            'body': 'I like to play osu!'
        },
        {
            'author': {'username': 'Michael'},
            'body': 'I like to go to the beach!'
        }
    ]
    return render_template('index.html', title=username, user=username, posts=posts)