#!/usr/bin/env python3

from flask.ext.testing import TestCase
from unittest import main
from sqlalchemy import create_engine, and_, or_
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['TESTING'] = True

db = SQLAlchemy(app)
from test_models import *

class TestModels (TestCase) :


    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_character_add (self) :
        character = Character(id=1, name='Dummy Char', thumbnail='something.jpg', description='Some description',
                              number_of_comics=1, number_of_stories=2, number_of_series=3)
        num_chars = len(db.session.query(Character).all())
        db.session.add(character)
        self.assertEqual(len(db.session.query(Character).all()), num_chars + 1)

    def test_character_query (self) :
        character = Character(id=2, name='Dummy Char2')
        db.session.add(character)
        character = Character.query.filter_by(id=2).first()
        self.assertEqual(character.name, 'Dummy Char2')

    def test_comic_add (self) :
        comic = Comic(id=1, title='Dummy Comic', thumbnail='something.jpg', issue_num=1, description='Some description',
                      page_count=500, series='Some series', number_of_creators=5, number_of_characters=2, number_of_stories=2)
        num_comics = len(db.session.query(Comic).all())
        db.session.add(comic)
        self.assertEqual(len(db.session.query(Comic).all()), num_comics + 1)

    def test_comic_query (self) :
        comic = Comic(id=2, title='Dummy Comic2')
        db.session.add(comic)
        comic = Comic.query.filter_by(id=2).first()
        self.assertEqual(comic.title, 'Dummy Comic2')

    def test_creator_add (self) :
        creator = Creator(id=1, first_name='Dummy', last_name='Creator', thumbnail='something.jpg', number_of_comics=1,
                          number_of_stories=1, number_of_series=1)
        num_creators = len(db.session.query(Creator).all())
        db.session.add(creator)
        self.assertEqual(len(db.session.query(Creator).all()), num_creators + 1)

    def test_creator_query (self) :
        creator = Creator(id=2, first_name='Dummy', last_name='Creator2')
        db.session.add(creator)
        creator = Creator.query.filter_by(id=2).first()
        self.assertEqual(creator.first_name, 'Dummy')

    def test_character_add_comics (self) :
        comic = Comic(id=3, title='Dummy Comic3', issue_num=1)
        db.session.add(comic)
        character = Character(id=3, name='Dummy Char3', description='Some description')
        comic = Comic.query.filter_by(id=3).first()
        character.comics.append(comic)
        db.session.add(character)
        comic = Comic.query.filter_by(id=3).first()
        self.assertEqual(len(comic.characters), 1)

    def test_comic_add_characters (self) :
        character = Character(id=4, name='Dummy Char4', description='Some description')
        db.session.add(character)
        comic = Comic(id=4, title='Dummy Comic4', issue_num=2)
        character = Character.query.filter_by(id=4).first()
        comic.characters.append(character)
        db.session.add(comic)
        character = Character.query.filter_by(id=4).first()
        self.assertEqual(len(character.comics), 1)

    def test_comic_add_creators (self) :
        creator = Creator(id=4, first_name='Dummy', last_name='Creator4')
        db.session.add(creator)
        comic = Comic(id=5, title='Dummy Comic5', issue_num=3)
        creator = Creator.query.filter_by(last_name='Creator4').first()
        comic.creators.append(creator)
        db.session.add(comic)
        creator = Creator.query.filter_by(id=4).first()
        self.assertEqual(len(creator.comics), 1)

    def test_creator_add_comics (self) :
        comic = Comic(id=6, title='Dummy Comic6', issue_num=4)
        db.session.add(comic)
        creator = Creator(id=5, first_name='Dummy', last_name='Creator5')
        comic = Comic.query.filter_by(id=6).first()
        creator.comics.append(comic)
        db.session.add(creator)
        comic = Comic.query.filter_by(id=6).first()
        self.assertEqual(len(comic.creators), 1)

    def test_search_1 (self) :
        comic = Comic(id=7, title='Dummy Comic7', issue_num=4)
        db.session.add(comic)
        comic2 = Comic(id=8, title='Great Title', issue_num=4)
        db.session.add(comic2)
        search_term = 'Dummy Comic'
        comics = Comic.query.filter(or_(Comic.title.contains(search_term), Comic.id.contains(search_term), Comic.issue_num.contains(search_term))).all()
        self.assertEqual(len(comics), 1)

    def test_search_2 (self) :
        creator = Creator(id=7, first_name='Dummy', last_name='Creator6')
        db.session.add(creator)
        creator2 = Creator(id=8, first_name='Test', last_name='Search')
        db.session.add(creator2)
        search_term = 'Test This'
        search_terms = search_term.split(' ')
        creators = Creator.query.filter(and_(or_(*[or_(
                        Creator.first_name.contains(term), Creator.last_name.contains(term), Creator.id.contains(term)) for term in search_terms])),
                        and_(Creator.first_name.contains(search_term)==False, Creator.last_name.contains(search_term)==False,
                            (Creator.first_name+" "+Creator.last_name).contains(search_term)==False, Creator.id.contains(search_term)==False)
                    ).all()
        self.assertEqual(len(creators), 1)

if __name__ == "__main__" :
    main()
