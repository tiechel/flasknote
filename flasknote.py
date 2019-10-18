from flask import render_template
from app import create_app
from app.models import Entry

app = create_app()


@app.route('/')
def hello_world():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)
