from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from .Models.Manager_Model import Manager

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = Manager.query.filter_by(username=username).all()
        for user in users:
            if user and user.verify_password(password):
                login_user(user)
                session['username'] = username
                flash('Logged in successfully.')
                return redirect(url_for('main.home'))
        error = 'ユーザーネームかパスワードが違います'
    return render_template('login.html', error=error)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
