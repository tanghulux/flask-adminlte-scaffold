from flask import render_template, redirect, request, url_for, flash

from . import auth
from .forms import LoginForm, RegisterForm
from app.models import User
from flask_login import login_user, logout_user, login_required

from ..main.views import common_edit


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.rememberme.data)
    if form.validate_on_submit():
        try:
            user = User.get(User.username == form.username.data)
            if user.verify_password(form.password.data):
                login_user(user, form.rememberme.data)
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash('用户名或密码错误')
        except:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            common_edit(User, RegisterForm(), 'register.html')
        except Exception as err:
            flash('Error: User already exists.')
            return redirect(url_for('auth.register'))
        flash('You are now registered and can log in!', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))
