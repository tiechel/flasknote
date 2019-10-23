from flask import Blueprint
from flask import render_template
from app.models import Entry

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)
