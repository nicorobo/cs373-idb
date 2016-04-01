from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db

comic_character = db.Table('comic_character',
    db.Column('comic_id', db.Integer, db.ForeignKey("comic.id"),
           primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey("character.id"),
           primary_key=True)
)

comic_creator = db.Table('comic_creator',
    db.Column('comic_id', db.Integer, db.ForeignKey("comic.id"),
           primary_key=True),
    db.Column('creator_id', db.Integer, db.ForeignKey("creator.id"),
           primary_key=True)
)

class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String(256))
    name = db.Column(db.String(256))
    description = db.Column(db.String(1000))
    number_of_comics = db.Column(db.Integer)
    number_of_stories = db.Column(db.Integer)
    number_of_series = db.Column(db.Integer)

    comics = db.relationship('Comic', secondary="comic_character",
                             backref="characters")

    def __repr__(self):
        id = self.id if self.id else None
        return '<%s %s>' % (self.__class__.__name__, id)


class Comic(db.Model):
    __tablename__ = 'comic'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String(256))
    title = db.Column(db.String(256))
    issue_num = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    page_count = db.Column(db.Integer)
    series = db.Column(db.String(256))
    number_of_creators = db.Column(db.Integer)
    number_of_characters = db.Column(db.Integer)
    number_of_stories = db.Column(db.Integer)

    creators = db.relationship('Creator', secondary="comic_creator",
                             backref="comics")

    def __repr__(self):
        id = self.id if self.id else None
        return '<%s %s>' % (self.__class__.__name__, id)


class Creator(db.Model):
    __tablename__ = 'creator'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String(256))
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    number_of_comics = db.Column(db.Integer)
    number_of_stories = db.Column(db.Integer)
    number_of_series = db.Column(db.Integer)

    def __repr__(self):
        id = self.id if self.id else None
        return '<%s %s>' % (self.__class__.__name__, id)
