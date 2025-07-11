from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from app import db
from app.auth import auth_blueprint as bp_auth 
from app.auth.auth_forms import RegistrationForm, LoginForm
from app.main.models import User
import sqlalchemy as sqla

@bp_auth.route('/user/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    rform = RegistrationForm()
    if rform.validate_on_submit():
        user = User(username = rform.username.data)
        user.set_password(rform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have successfully registered!', 'success')
        return redirect(url_for('main.index'))
    if rform.is_submitted() and not rform.validate():
        for field, error_list in rform.errors.items():
            for error in error_list:
                flash(error, 'danger')
    return render_template('register.html', title="Registration" ,form=rform)


@bp_auth.route('/user/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    lform = LoginForm()
    if lform.validate_on_submit():
        query = sqla.select(User).where(User.username == lform.username.data)
        user = db.session.scalars(query).first()
        # If provided user doesn't exist or entered password is incorrect
        if (user is None):
            flash('Input username does not exist!', 'danger')
            return redirect(url_for('auth.login'))
        if (user.check_password(lform.password.data) == False):
            flash('Password incorrect, please try again!', 'danger')
            return redirect(url_for('auth.login'))
        # Else (successful login)
        login_user(user, remember=lform.remember_me.data)
        flash('Welcome back, {}!'.format(current_user.username), 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', title="Login", form = lform)

@bp_auth.route('/user/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))