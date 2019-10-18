import os
from app import create_app
from flask import render_template

app = create_app()

@app.route('/')
def hello_world():
    return render_template('index.html', username="John")
