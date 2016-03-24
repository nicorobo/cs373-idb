#!/usr/bin/env python3

from unittest import main, TestCase
from models import Character, Comic, Creator

class TestModels (TestCase) :

    def test_character_query (self) :
        character = Character.query.filter(Character.name=='Black Panther')
        self.assertEqual(character.description, 'Some description')

    def test_comic_query (self) :
        comic = Comic.query.filter(Comic.title=='Avengers')
        self.assertEqual(comic.description, 'Some description')

    def test_creator_query (self) :
        creator = Creator.query.filter(and_(Creator.first_name=='Joe' and Creator.last_name=='Quesada'))
        self.assertEqual(creator.description, 'Some description')


if __name__ == "__main__" :
    main()
