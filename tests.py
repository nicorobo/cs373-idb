#!/usr/bin/env python3

from unittest import main, TestCase
from models import Character, Comic, Creator

class TestModels (TestCase) :

    def test_character_query_1 (self) :
        character = Character.query.filter(Character.name=="Storm")
        self.assertEqual(character.description, "Ororo Monroe is the descendant of an ancient line of African priestesses, all of whom have white hair, blue eyes, and the potential to wield magic.")

    def test_character_query_2 (self) :
        character = Character.query.filter(Character.name=="Hulk")
        self.assertEqual(character.thumbnail, "http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0.jpg")

    def test_comic_query_1 (self) :
        comic = Comic.query.filter(Comic.title=="Adam: Legend of the Blue Marvel (2008) #2")
        self.assertEqual(comic.description, "In the wake of Anti-Man's devastating attack on New York City, the Mighty Avengers are neutralized, and Iron Man's on a quest for answers! Who was the Blue Marvel?\r\nWhy did he disappear over 40 years ago? And...what alarming secrets will Iron Man discover about the U.S. government and his own agency of S.H.I.E.L.D.? There are no easy answers in the story of Marvel's newest super hero...created by Kevin Grevioux (NEW WARRIORS) and Mat Broome (The End League)!\r\nRated T  ...$3.99")

    def test_comic_query_2 (self) :
        comic = Comic.query.filter(Comic.title=="Adam: Legend of the Blue Marvel (2008) #1")
        self.assertEqual(comic.issue_num, 1)

    def test_creator_query_1 (self) :
        creator = Creator.query.filter(Creator.id=='2289')
        self.assertEqual(creator.num_stories, 3)

    def test_creator_query_2 (self) :
        creator = Creator.query.filter(Creator.first_name=='Alexandrov')
        self.assertEqual(creator.id, 2289)


if __name__ == "__main__" :
    main()
