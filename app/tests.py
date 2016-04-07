#!/usr/bin/env python3

from app import db, app
from unittest import main, TestCase
from models import *


class TestModels (TestCase) :

    def test_character_add (self) :
        character = Character(id=3, name='Dummy Char')
        num_chars = len(db.session.query(Character).all())
        db.session.add(character)
        self.assertEqual(len(db.session.query(Character).all()), num_chars + 1)
        db.session.rollback()

    def test_character_query (self) :
        character = Character(id=3, name='Dummy Char')
        db.session.add(character)
        character = Character.query.filter_by(id=3).first()
        self.assertEqual(character.name, 'Dummy Char')
        db.session.rollback()

    def test_comic_add (self) :
        comic = Comic(id=3, title="Dummy Comic")
        num_comics = len(db.session.query(Comic).all())
        db.session.add(comic)
        self.assertEqual(len(db.session.query(Comic).all()), num_comics + 1)
        db.session.rollback()

    def test_comic_query (self) :
        comic = Comic(id=3, title='Dummy Comic')
        db.session.add(comic)
        comic = Comic.query.filter_by(id=3).first()
        self.assertEqual(comic.title, 'Dummy Comic')
        db.session.rollback()

    def test_creator_add (self) :
        creator = Creator(id=3, first_name='Dummy', last_name='Creator')
        num_creators = len(db.session.query(Creator).all())
        db.session.add(creator)
        self.assertEqual(len(db.session.query(Creator).all()), num_creators + 1)
        db.session.rollback()

    def test_creator_query (self) :
        creator = Creator(id=3, first_name='Dummy', last_name='Creator')
        db.session.add(creator)
        creator = Creator.query.filter_by(id=3).first()
        self.assertEqual(creator.first_name, 'Dummy')
        db.session.rollback()

if __name__ == "__main__" :
    main()
