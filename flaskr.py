# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import with_statement
import os

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# configuration
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'default'
SECRET_KEY = 'development key'

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# postgres
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Name %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    content = db.Column(db.String(4096))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Title %r>' % self.title

@app.route('/makedb')
def init_post():
    db.create_all()

    for oldadmin in User.query.all():
        db.session.delete(oldadmin)

    user = User('admin', 'default')
    db.session.add(user)
    db.session.commit()

    return "done"


@app.route('/')
def show_entries():
    entries = Post.query.order_by(Post.id)
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    post = Post(request.form['title'], request.form['text'])
    db.session.add(post)
    db.session.commit()
    
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/adduser', methods=['GET', 'POST'])
def add_user():
    if not session.get('logged_in'):
        abort(401)

    if request.method == 'POST':
        user = User(request.form['username'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Added user' + user.username)
        return redirect(url_for('show_entries'))
    
    return render_template('adduser.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'] ).first()

        if user == None:
            error = 'Invalid username'
        elif user.password != request.form['password']:
            error = 'Invalid password.' # Should be ' + user.password
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    # OTHERWISE HEROKU WON'T RUN IT
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True)
