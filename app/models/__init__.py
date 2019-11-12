from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)

    def __repr___(self):
        return '<Entry {}>'.format(id)


class Fortune(db.Model):
    __tablename__ = 'fortunes'
    __table_args__ = (db.UniqueConstraint('date', 'sign', name='unique_idx_date_sign'), {})

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    sign = db.Column(db.String(), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(), nullable=False)
    item = db.Column(db.String(), nullable=False)
    money = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Integer, nullable=False)
    love = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<Fortune {}>'.format(id)
