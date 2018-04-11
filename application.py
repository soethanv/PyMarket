from app import create_app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

main_application = create_app()


@main_application.route('/', methods=['GET', 'POST'])
@main_application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)


# run the app
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # main_application.debug = True
    main_application.run()
