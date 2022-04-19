from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)