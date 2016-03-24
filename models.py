from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


comic_character = Table('association', Base.metadata,
                        Column('comic_id',     Integer, ForeignKey('comic.id')),
                        Column('character_id', Integer, ForeignKey('character.id'))
)


comic_creator = Table('assocation', Base.metadata,
                      Column('comic_id',   Integer, ForeignKey('comic.id')),
                      Column('creator_id', Integer, ForeignKey('creator.id'))
)


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    thumbnail = Column(String)
    name = Column(String)
    description = Column(String)
    number_of_comics = Column(Integer)
    comics = relationship('Comic',
                          secondary=comic_character,
                          back_populates='characters')


class Comic(Base):
    __tablename__ = 'comic'

    id = Column(Integer, primary_key=True)
    thumbnail = Column(String)
    title = Column(String)
    issue_num = Column(Integer)
    description = Column(String)
    page_count = Column(Integer)
    characters = relationship('Character',
                              secondary=comic_character,
                              back_populates='comics')
    creators = relationship('Creator',
                            secondary=comic_creator,
                            back_populates='comics')


class Creator(Base):
    __tablename__ = 'creator'

    id = Column(Integer, primary_key=True)
    thumbnail = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    comics = relationship('Comic',
                          secondary=comic_creator,
                          back_populates='creators')
