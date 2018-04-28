#!/usr/bin/env bash

if ! [ -d "./venv/" ];
then
    virtualenv venv --python=python3
    source ./venv/bin/activate
    pip install -r requirements.txt
fi


if [[ -z "$VIRTUAL_ENV" ]];
then
    echo "No VIRTUAL_ENV set. Entering venv."
    source ./venv/bin/activate
fi


export FLASK_APP=application.py
