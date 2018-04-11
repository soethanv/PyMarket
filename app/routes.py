from flask import render_template, flash, redirect, url_for
from application import main_application
from app.forms import LoginForm

print('it ran')

@main_application.route('/', methods=['GET', 'POST'])
@main_application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)
