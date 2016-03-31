from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db


class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String(256))
    name = db.Column(db.String(256))
    description = db.Column(db.String(1000))
    number_of_comics = db.Column(db.Integer)
    number_of_stories = db.Column(db.Integer)
    number_of_series = db.Column(db.Integer)
    comics = relationship('ComicCharacter',
                          back_populates='character')

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
    characters = relationship('ComicCharacter',
                          back_populates='comic')
    creators = relationship('ComicCreator',
                          back_populates='comic')
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
    comics = relationship('ComicCreator',
                          back_populates='creator')

    def __repr__(self):
        id = self.id if self.id else None
        return '<%s %s>' % (self.__class__.__name__, id)


class ComicCharacter(db.Model):
    __tablename__ = 'comic_character'

    comic_id = db.Column(db.Integer, ForeignKey('comic.id'), primary_key=True)
    character_id = db.Column(db.Integer, ForeignKey('character.id'), primary_key=True)
    comic = relationship("Comic", back_populates="characters")
    character = relationship("Character", back_populates="comics")

    def __repr__(self):
        comic_id = self.comic_id if self.comic_id else None
        character_id = self.character_id if self.character_id else None
        return '<%s %s %s>' % (self.__class__.__name__, comic_id, character_id)


class ComicCreator(db.Model):
    __tablename__ = 'comic_creator'

    comic_id = db.Column(db.Integer, ForeignKey('comic.id'), primary_key=True)
    creator_id = db.Column(db.Integer, ForeignKey('creator.id'), primary_key=True)
    comic = relationship("Comic", back_populates="creators")
    creator = relationship("Creator", back_populates="comics")

    def __repr__(self):
        comic_id = self.comic_id if self.comic_id else None
        creator_id = self.creator_id if self.creator_id else None
        return '<%s %s %s>' % (self.__class__.__name__, comic_id, creator_id)
