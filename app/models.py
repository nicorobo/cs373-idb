from sqlalchemy import create_engine


class Character:
    __tablename__ = 'character'

    id = db.Column(db.BigInteger)
    thumbnail = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_comics = db.Column(db.Integer)
    num_stories = db.Column(db.Integer)
    num_series = db.Column(db.Integer)

class Comic:
    __tablename__ = 'comic'

    id = db.Column(db.BigInteger)
    thumbnail = db.Column(db.String)
    title = db.Column(db.String)
    issue_num = db.Column(db.Integer)
    description = db.Column(db.String)
    page_count = db.Column(db.Integer)
    num_stories = db.Column(db.Integer)

class Creator:
    __tablename__ = 'creator'

    id = db.Column(db.BigInteger)
    thumbnail = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    num_stories = db.Column(db.Integer)
