#!/usr/bin/env python3

from unittest import main, TestCase
from models import Character, Comic, Creator
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Session = sessionmaker()
engine = create_engine('postgresql://...')

class TestModels (TestCase) :

    def set_up():
        self.connection = engine.connect()
        self.trans = self.connection.begin()
        self.session = Session(bind=self.connection)

    def test_character_query_1 (self) :
        character = self.session.query(Character).filter(Character.name=="Storm").first()
        self.assertEqual(character.description, "Ororo Monroe is the descendant of an ancient line of African priestesses, all of whom have white hair, blue eyes, and the potential to wield magic.")

    def test_character_query_2 (self) :
        character = self.session.query.filter(Character.name=="Hulk").first()
        self.assertEqual(character.thumbnail, "http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0.jpg")

    def test_character_add (self) :
        character = Character(thumbnail='http://i.annihil.us/u/prod/marvel/i/mg/9/c0/527bb7b37ff55.jpg', name='Iron Man')
        self.session.add(character)
        self.session.commit()
        query_character = self.session.query.filter(Character.name=='Iron Man').first()
        self.assertEqual(query_character.thumbnail, 'http://i.annihil.us/u/prod/marvel/i/mg/9/c0/527bb7b37ff55.jpg')

    def test_comic_query_1 (self) :
        comic = self.session.query(Comic).filter(Comic.title=="Adam: Legend of the Blue Marvel (2008) #2").first()
        self.assertEqual(comic.description, "In the wake of Anti-Man's devastating attack on New York City, the Mighty Avengers are neutralized, and Iron Man's on a quest for answers! Who was the Blue Marvel?\r\nWhy did he disappear over 40 years ago? And...what alarming secrets will Iron Man discover about the U.S. government and his own agency of S.H.I.E.L.D.? There are no easy answers in the story of Marvel's newest super hero...created by Kevin Grevioux (NEW WARRIORS) and Mat Broome (The End League)!\r\nRated T  ...$3.99")

    def test_comic_query_2 (self) :
        comic = self.session.query(Comic).filter(Comic.title=="Adam: Legend of the Blue Marvel (2008) #1").first()
        self.assertEqual(comic.issue_num, 1)

    def test_comic_add (self) :
        comic = Comic(issue_num=2, title='Adam: Legend of the Blue Marvel (2008) #2')
        self.session.add(comic)
        self.session.commit()
        query_comic = self.session.query.filter(Comic.title=='Adam: Legend of the Blue Marvel (2008) #2').first()
        self.assertEqual(query_comic.issue_num, 2)

    def test_creator_query_1 (self) :
        creator = self.session.query(Creator).filter(Creator.id=='2289').first()
        self.assertEqual(creator.first_name, Alexandrov)

    def test_creator_query_2 (self) :
        creator = self.session.query(Creator).filter(Creator.first_name=='Alexandrov').first()
        self.assertEqual(creator.id, 2289)

    def test_creator_add (self) :
        creator = Creator(name='Amash', thumbnail='http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available.jpg')
        self.session.add(creator)
        self.session.commit()
        query_creator = self.session.query.filter(Creator.name=='Amash').first()
        self.assertEqual(thumbnail, 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available.jpg')

    def tearDown(self):
        self.session.close()
        self.trans.rollback()
        self.connection.close()

if __name__ == "__main__" :
    main()
