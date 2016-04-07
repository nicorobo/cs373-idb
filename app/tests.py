#!/usr/bin/env python3

from app import db, app
from unittest import main, TestCase
from models import Character, Comic, Creator
from flask.ext.testing import TestCase

TEST_SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username='admin',
        password='password',
        hostname='cs373idb_db',
        database='marvel_test')


class TestModels (TestCase) :

    def create_app (self) :
        app.config['SQLALCHEMY_DATABASE_URI'] = TEST_SQLALCHEMY_DATABASE_URI
        return app

    def set_up (self) :
        db.create_all()
        character = Character(id=1, name="Dummy Name")
        db.session.add(character)
        db.session.commit()

    def test_character_add (self) :
        characters = Character.query.all()
        assert len(characters) == 1

    def test_character_query_1 (self) :
        character = Character.query.filter_by(Character.name=="Storm").first()
        self.assertEqual(character.description, "Ororo Monroe is the descendant of an ancient line of African priestesses, all of whom have white hair, blue eyes, and the potential to wield magic.")

    def test_character_query_2 (self) :
        character =  Character.query.filter_by(Character.name=="Hulk").first()
        self.assertEqual(character.thumbnail, "http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0.jpg")

    def test_character_query3 (self) :
        character = Character.query.filter_by(Character.name=='Iron Man').first()
        self.assertEqual(character.thumbnail, 'http://i.annihil.us/u/prod/marvel/i/mg/9/c0/527bb7b37ff55.jpg')

    def test_comic_query_1 (self) :
        comic = Comic.query.filter_by(Comic.title=="Adam: Legend of the Blue Marvel (2008) #2").first()
        self.assertEqual(comic.description, "In the wake of Anti-Man's devastating attack on New York City, the Mighty Avengers are neutralized, and Iron Man's on a quest for answers! Who was the Blue Marvel?\r\nWhy did he disappear over 40 years ago? And...what alarming secrets will Iron Man discover about the U.S. government and his own agency of S.H.I.E.L.D.? There are no easy answers in the story of Marvel's newest super hero...created by Kevin Grevioux (NEW WARRIORS) and Mat Broome (The End League)!\r\nRated T  ...$3.99")

    def test_comic_query_2 (self) :
        comic = Comic.query.filter_by(Comic.title=="Adam: Legend of the Blue Marvel (2008) #1").first()
        self.assertEqual(comic.issue_num, 1)

    def test_comic_query3 (self) :
        comic = Comic.query.filter_by(Comic.title=='Adam: Legend of the Blue Marvel (2008) #2').first()
        self.assertEqual(comic.issue_num, 2)

    def test_creator_query_1 (self) :
        creator = Creator.query.filter_by(Creator.id=='2289').first()
        self.assertEqual(creator.first_name, Alexandrov)

    def test_creator_query_2 (self) :
        creator = Creator.query.filter_by(Creator.first_name=='Alexandrov').first()
        self.assertEqual(creator.id, 2289)

    def test_creator_query3 (self) :
        creator = Creator.query.filter_by(Creator.name=='Amash').first()
        self.assertEqual(creator.thumbnail, 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available.jpg')

    def tear_down(self):
        db.session.remove()
        db.drop_all()

if __name__ == "__main__" :
    main()
