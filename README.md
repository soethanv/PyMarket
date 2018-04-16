# PyMarket


### Prerequisites

To set up virtual environment via bash script:
```
. project_init.sh

Take note of the '.'
```

To create the python virtual environment:
```
virtualenv venv
```

To enter the python env:
```
source ./venv/bin/activate
```

To install the project requirements:
```
pip install -r requirements.txt
```

To exit the env:
```
deactivate
```

To update the requirements.txt:
```
pip freeze > requirements.txt
```

To run the flask application:
```
export FLASK_APP=application.py

flask run
```

or

```
python application.py
```

Init and upgrade database
```
flask db init

flask db upgrade
```

To add stuff to database (for now):
```
flask shell

user = User(username='username', email='user@example.com')
user.set_password('mypassword')

db.session.add(user)
db.session.commit()
```
