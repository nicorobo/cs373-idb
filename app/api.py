from app import db, logger
from models import *

def add_character(json_data):
    id = json_data[u'data'][u'results'][0][u'id']
    thumbnail = json_data[u'data'][u'results'][0][u'thumbnail'][u'path']+'.' +json_data[u'data'][u'results'][0][u'thumbnail'][u'extension']
    name = json_data[u'data'][u'results'][0][u'name']
    description = json_data[u'data'][u'results'][0][u'description']
    number_of_comics = json_data[u'data'][u'results'][0][u'comics'][u'available']
    number_of_stories = json_data[u'data'][u'results'][0][u'stories'][u'available']
    number_of_series = json_data[u'data'][u'results'][0][u'series'][u'available']

    comic_ids = []
    for comic in json_data[u'data'][u'results'][0][u'comics'][u'items']:
        comic_ids.append(int(comic[u'resourceURI'].split('/comics/')[1]))

    character = Character(id=id, thumbnail=thumbnail, name=name, description=description,
    number_of_comics=number_of_comics, number_of_stories=number_of_stories, number_of_series=number_of_series)
    db.session.add(character)
    logger.debug('Added %s', character)

    # for comic_id in comic_ids:
        #TODO check if comic_character already in DB?
        # comic_character = ComicCharacter()
        # comic_character.comic=Comic(id=comic_id)
        # character.comics.append(comic_character)
        # db.session.add(comic_character)
        #TODO check if comic is in DB?

    db.session.commit()

def add_comic(json_data):
    id = json_data[u'data'][u'results'][0][u'id']
    thumbnail = json_data[u'data'][u'results'][0][u'thumbnail'][u'path']+'.' +json_data[u'data'][u'results'][0][u'thumbnail'][u'extension']
    title = json_data[u'data'][u'results'][0][u'title']
    issue_num = json_data[u'data'][u'results'][0][u'issueNumber']
    description = json_data[u'data'][u'results'][0][u'description']
    page_count = json_data[u'data'][u'results'][0][u'pageCount']
    series = json_data[u'data'][u'results'][0][u'series'][u'name']
    number_of_characters = json_data[u'data'][u'results'][0][u'characters'][u'available']
    number_of_creators = json_data[u'data'][u'results'][0][u'creators'][u'available']
    number_of_stories = json_data[u'data'][u'results'][0][u'stories'][u'available']

    comic = Comic(id=id, thumbnail=thumbnail, title=title, description=description,
    page_count=page_count, series=series, number_of_characters=number_of_characters,
    number_of_stories=number_of_stories)
    db.session.add(comic)
    logger.debug('Added %s', comic)

    character_ids = []
    for character in json_data[u'data'][u'results'][0][u'characters'][u'items']:
        character_ids.append(int(character[u'resourceURI'].split('/characters/')[1]))

    # for character_id in character_ids:
        #TODO check if comic_character already in DB?
        # comic_character = ComicCharacter()
        # comic_character.character=Character(id=character_id)
        # comic.characters.append(comic_creator)
        # db.session.add(comic_character)
        #TODO check if character is in DB?

    creator_ids = []
    for creator in json_data[u'data'][u'results'][0][u'creators'][u'items']:
        try:
            character_ids.append(int(character[u'resourceURI'].split('/creators/')[1]))
        except:
            pass

    # for creator_id in creator_ids:
        #TODO check if comic_creator already in DB?
        # comic_creator = ComicCreator()
        # comic_creator.creator=Creator(id=creator_id)
        # comic.creators.append(comic_creator)
        # db.session.add(comic_creator)
        #TODO check if creator is in DB?

    db.session.commit()

def add_creator(json_data):
    id = json_data[u'data'][u'results'][0][u'id']
    thumbnail = json_data[u'data'][u'results'][0][u'thumbnail'][u'path']+'.' +json_data[u'data'][u'results'][0][u'thumbnail'][u'extension']
    first_name = json_data[u'data'][u'results'][0][u'firstName']
    last_name = json_data[u'data'][u'results'][0][u'lastName']
    number_of_comics = json_data[u'data'][u'results'][0][u'comics'][u'available']
    number_of_stories = json_data[u'data'][u'results'][0][u'stories'][u'available']
    number_of_series = json_data[u'data'][u'results'][0][u'series'][u'available']

    creator = Creator(id=id, thumbnail=thumbnail, first_name=first_name, last_name=last_name,
    number_of_comics=number_of_comics, number_of_series=number_of_series,
    number_of_stories=number_of_stories)

    comic_ids = []
    for comic in json_data[u'data'][u'results'][0][u'comics'][u'items']:
        comic_ids.append(int(comic[u'resourceURI'].split('/comics/')[1]))

    # for comic_id in comic_ids:
        #TODO check if comic_creator already in DB?
        # comic_creator = ComicCreator()
        # comic_creator.comic=Comic(id=comic_id)
        # creator.comics.append(comic_creator)
        # creator.comics.append(comic_creator)
        # db.session.add(comic_creator)
        #TODO check if comic is in DB?

    db.session.add(creator)
    logger.debug('Added %s', creator)
    db.session.commit()
