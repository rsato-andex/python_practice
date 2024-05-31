from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required, current_user
from .Models.Manager_Model import Manager

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/top')
def login_trans():
    return redirect(url_for('auth.login'))

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    username = session.get('username', '')
    return render_template('home.html', username=username)

@main.route('/user/update', methods=['GET', 'POST'])
@login_required
def user_update():
    username = session.get('username', '')
    user_info = Manager.query.filter_by(username=username).first()
    return render_template('user_form.html', user_info=user_info)
