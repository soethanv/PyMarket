from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm



@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)
