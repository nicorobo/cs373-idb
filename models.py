from app import db
from sqlalchemy import orm, ForeignKey


class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_comics = db.Column(db.Integer)
    num_stories = db.Column(db.Integer)
    num_series = db.Column(db.Integer)
    comics = orm.relationship('Comic', secondary='character_comic')
    creators = orm.relationship('Creator', secondary='character_creator')

class Comic(db.Model):
    __tablename__ = 'comic'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String)
    title = db.Column(db.String)
    issue_num = db.Column(db.Integer)
    description = db.Column(db.String)
    page_count = db.Column(db.Integer)
    num_stories = db.Column(db.Integer)
    characters = orm.relationship('Character', secondary='character_comic')
    creators = orm.relationship('Creator', secondary='comic_creator')


class Creator(db.Model):
    __tablename__ = 'creator'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    num_stories = db.Column(db.Integer)
    characters = orm.relationship('Character', secondary='character_creator')
    comics = orm.relationship('Comic', secondary='comic_creator')


class CharacterComic(db.Model):
    __tablename__ = 'character_comic'

    character_id = db.Column(db.Integer, ForeignKey('character.id'), primary_key=True)
    comic_id = db.Column(db.Integer, ForeignKey('comic.id'), primary_key=True)


class ComicCreator(db.Model):
    __tablename__ = 'comic_creator'

    comic_id = db.Column(db.Integer, ForeignKey('comic.id'), primary_key=True)
    creator_id = db.Column(db.Integer, ForeignKey('creator.id'), primary_key=True)


class CharacterCreator(db.Model):
    __tablename__ = 'character_creator'

    character_id = db.Column(db.Integer, ForeignKey('character.id'), primary_key=True)
    comic_id = db.Column(db.Integer, ForeignKey('comic.id'), primary_key=True)
