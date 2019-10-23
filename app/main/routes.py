from flask import Blueprint
from flask import render_template, redirect, url_for
from app.models import db, Entry
from app.main.forms import EntryForm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    entries = Entry.query.all()
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry()
        entry.title = form.title.data
        entry.body = form.body.data
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('index.html', form=EntryForm(), entries=entries)
