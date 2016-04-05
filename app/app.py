import os
import logging
import json

from flask import Flask, render_template, jsonify
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

import mapper

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Welcome")


SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username='admin',
        password='password',
        hostname='cs373idb_db',
        database='marvel')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app)

from api import *
from models import *

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/characters', methods=["GET"])
def characters():
    return jsonify({'characters': list(map(mapper.character_to_dict, Character.query.all()))})

@app.route('/api/character/<character_id>', methods=["GET"])
def character(character_id):
    return jsonify({'character': mapper.character_detail_to_dict(Character.query.filter_by(id=character_id).first())})

@app.route('/api/comics', methods=["GET"])
def comics():
    return jsonify({'comics': list(map(mapper.comic_to_dict, Comic.query.all()))})

@app.route('/api/comic/<comic_id>', methods=["GET"])
def comic(comic_id):
    return jsonify({'comic': mapper.comic_detail_to_dict(Comic.query.filter_by(id=comic_id).first())})

@app.route('/api/creators', methods=["GET"])
def creators():
    return jsonify({'creators': list(map(mapper.creator_to_dict, Creator.query.all()))})

@app.route('/api/creator/<creator_id>', methods=["GET"])
def creator(creator_id):
    return jsonify({'creator': mapper.creator_detail_to_dict(Creator.query.filter_by(id=creator_id).first())})

# Serves the initial website (the catch-all is to facilitate react-router routes)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@manager.command
def create_db():
    logger.debug("create_db")
    app.config['SQLALCHEMY_ECHO'] = True
    db.create_all()

@manager.command
def create_dummy_data():
    logger.debug("create_test_data")
    app.config['SQLALCHEMY_ECHO'] = True
    json_data = {"status": "Ok", "code": 200, "copyright": "\u00a9 2016 MARVEL", "attributionText": "Data provided by Marvel. \u00a9 2016 MARVEL", "etag": "6adc0e607132bfd1d963960d942b170c62b2c996", "attributionHTML": "<a href=\"http://marvel.com\">Data provided by Marvel. \u00a9 2016 MARVEL</a>", "data": {"count": 1, "total": 1, "limit": 20, "results": [{"resourceURI": "http://gateway.marvel.com/v1/public/creators/648", "suffix": "", "firstName": "Simone", "middleName": "", "lastName": "Bianchi", "modified": "2015-10-01T15:55:17-0400", "thumbnail": {"path": "http://i.annihil.us/u/prod/marvel/i/mg/f/30/4bc5a8bb82ff1", "extension": "jpg"}, "comics": {"available": 175, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/comics/38524", "name": "Age of X: Universe (2011) #1"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/38523", "name": "Age of X: Universe (2011) #2"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/51249", "name": "All-New Captain America: Fear Him (2015) #1"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/51250", "name": "All-New Captain America: Fear Him (2015) #2"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/51251", "name": "All-New Captain America: Fear Him (2015) #3"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/51252", "name": "All-New Captain America: Fear Him (2015) #4"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/56490", "name": "Amazing Spider-Man (2015) #1.1"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/56493", "name": "Amazing Spider-Man (2015) #1.3"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/56494", "name": "Amazing Spider-Man (2015) #1.4"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/51325", "name": "Amazing Spider-Man (2014) #15 (Bianchi Variant)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/53014", "name": "Amazing Spider-Man (2014) #16.1 (Bianchi Variant)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/20961", "name": "Amazing Spider-Man (1999) #555 (VARIANT)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/28227", "name": "Amazing Spider-Man (1999) #622"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/51334", "name": "Amazing Spider-Man Annual (2014) #1 (Bianchi Variant)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/38462", "name": "Astonishing Spider-Man & Wolverine: Another Fine Mess (2011) #1"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/21511", "name": "Astonishing X-Men (2004) #25"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/21714", "name": "Astonishing X-Men (2004) #26"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/21941", "name": "Astonishing X-Men (2004) #27"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/23087", "name": "Astonishing X-Men (2004) #28"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/23937", "name": "Astonishing X-Men (2004) #29"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/creators/648/comics"}, "stories": {"available": 274, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/stories/2243", "type": "cover", "name": "1 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/2244", "type": "interiorStory", "name": "1 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/7641", "type": "cover", "name": "2 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/7642", "type": "interiorStory", "name": "2 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/7643", "type": "cover", "name": "3 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/7644", "type": "interiorStory", "name": "3 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8111", "type": "cover", "name": "3 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8112", "type": "interiorStory", "name": "3 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8113", "type": "cover", "name": "4 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8114", "type": "interiorStory", "name": "4 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8115", "type": "cover", "name": "4 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8116", "type": "interiorStory", "name": "4 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8586", "type": "cover", "name": "5 of 6 - Evolution / No Cover or Interior Ads! UPC on Cv4!"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8587", "type": "interiorStory", "name": "5 of 6 - Evolution / No Cover or Interior Ads! UPC on Cv4!"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8588", "type": "cover", "name": "5 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/8589", "type": "interiorStory", "name": "5 of 6 - Evolution"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/32309", "type": "cover", "name": "THE INITIATIVE BANNER"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/32526", "type": "cover", "name": "6 of 6 - Evolution / No Cover or Interior Ads! UPC on Cv4!"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/32527", "type": "interiorStory", "name": "6 of 6 - Evolution / No Cover or Interior Ads! UPC on Cv4!"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/32528", "type": "cover", "name": "6 of 6 - Evolution"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/creators/648/stories"}, "urls": [{"url": "http://marvel.com/comics/creators/648/simone_bianchi?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "detail"}], "series": {"available": 84, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/series/13896", "name": "Age of X: Universe (2011)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/19344", "name": "All-New Captain America: Fear Him (2015)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/19253", "name": "All-New Captain America: Fear Him (2015 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/454", "name": "Amazing Spider-Man (1999 - 2013)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/17285", "name": "Amazing Spider-Man (2014 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/20694", "name": "Amazing Spider-Man (2015 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/18900", "name": "Amazing Spider-Man Annual (2014 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/13864", "name": "Astonishing Spider-Man & Wolverine: Another Fine Mess (2011)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/744", "name": "Astonishing X-Men (2004 - 2013)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/8916", "name": "Astonishing X-Men: Ghost Box (2009)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/5998", "name": "Astonishing X-Men: Ghost Boxes (2008)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/16452", "name": "Avengers (2012 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/18398", "name": "Avengers World (2014 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/15691", "name": "Black Panther: The Man Without Fear (2010 - 2011)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/13165", "name": "Black Panther: The Man Without Fear - Fear Itself TPB (2010 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/16907", "name": "Cable and X-Force (2012 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/16516", "name": "Captain America (2012 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/6599", "name": "Dark Avengers (2009 - 2010)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/8798", "name": "Dark Avengers/Uncanny X-Men: Exodus (2009)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/8799", "name": "Dark Avengers/Uncanny X-Men: Utopia (2009)"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/creators/648/series"}, "events": {"available": 7, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/events/303", "name": "Age of X"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/318", "name": "Dark Reign"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/302", "name": "Fear Itself"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/317", "name": "Inhumanity"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/255", "name": "Initiative"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/319", "name": "Original Sin"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/327", "name": "Star Wars"}], "returned": 7, "collectionURI": "http://gateway.marvel.com/v1/public/creators/648/events"}, "fullName": "Simone Bianchi", "id": 648}], "offset": 0}}
    add_creator(json_data)
    json_data = {"status": "Ok", "code": 200, "copyright": "\\u00a9 2016 MARVEL", "attributionText": "Data provided by Marvel. \\u00a9 2016 MARVEL", "etag": "faa0eda439e8b5ef162cc96335481147c0bfc22a", "attributionHTML": "<a href=\"http://marvel.com\">Data provided by Marvel. \\u00a9 2016 MARVEL</a>", "data": {"count": 1, "total": 1, "limit": 20, "results": [{"isbn": "", "pageCount": 32, "series": {"resourceURI": "http://gateway.marvel.com/v1/public/series/744", "name": "Astonishing X-Men (2004 - 2013)"}, "modified": "-0001-11-30T00:00:00-0500", "variantDescription": "", "collectedIssues": [], "images": [{"path": "http://i.annihil.us/u/prod/marvel/i/mg/9/10/4bb4f72d0471e", "extension": "jpg"}], "id": 24501, "digitalId": 12718, "title": "Astonishing X-Men (2004) #30", "ean": "", "collections": [], "thumbnail": {"path": "http://i.annihil.us/u/prod/marvel/i/mg/9/10/4bb4f72d0471e", "extension": "jpg"}, "description": "\"GHOST BOX,\" PART 6\r\nSome boxes are best left unopened.  It's the final chapter of the opening epic by the superstar team of Warren Ellis and Simone Bianchi.\r\nRated T  ...$2.99", "format": "Comic", "diamondCode": "APR090528", "characters": {"available": 8, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009175", "name": "Beast"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009257", "name": "Cyclops"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009310", "name": "Emma Frost"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009508", "name": "Kitty Pryde"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009504", "name": "Professor X"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009629", "name": "Storm"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009718", "name": "Wolverine"}, {"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009726", "name": "X-Men"}], "returned": 8, "collectionURI": "http://gateway.marvel.com/v1/public/comics/24501/characters"}, "prices": [{"price": 2.99, "type": "printPrice"}, {"price": 1.99, "type": "digitalPurchasePrice"}], "variants": [], "resourceURI": "http://gateway.marvel.com/v1/public/comics/24501", "dates": [{"date": "2009-06-24T00:00:00-0400", "type": "onsaleDate"}, {"date": "2009-06-04T00:00:00-0400", "type": "focDate"}, {"date": "2010-01-01T00:00:00-0500", "type": "unlimitedDate"}, {"date": "2011-02-01T00:00:00-0500", "type": "digitalPurchaseDate"}], "issn": "", "textObjects": [{"text": "\"GHOST BOX,\" PART 6\r\nSome boxes are best left unopened.  It's the final chapter of the opening epic by the superstar team of Warren Ellis and Simone Bianchi.\r\nRated T  ...$2.99", "type": "issue_solicit_text", "language": "en-us"}], "upc": "5960605543-03011", "events": {"available": 0, "items": [], "returned": 0, "collectionURI": "http://gateway.marvel.com/v1/public/comics/24501/events"}, "stories": {"available": 2, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/stories/54035", "type": "cover", "name": "Cover #54035"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/54036", "type": "interiorStory", "name": "Interior #54036"}], "returned": 2, "collectionURI": "http://gateway.marvel.com/v1/public/comics/24501/stories"}, "issueNumber": 30, "urls": [{"url": "http://marvel.com/comics/issue/24501/astonishing_x-men_2004_30?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "detail"}, {"url": "http://comicstore.marvel.com/Astonishing-X-Men-30/digital-comic/12718?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "purchase"}, {"url": "http://marvel.com/digitalcomics/view.htm?iid=12718&utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "reader"}, {"url": "http://applink.marvel.com/issue/12718?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "inAppLink"}], "creators": {"available": 5, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/creators/648", "role": "colorist", "name": "Simone Bianchi"}, {"resourceURI": "http://gateway.marvel.com/v1/public/creators/774", "role": "colorist", "name": "Morry Hollowell"}, {"resourceURI": "http://gateway.marvel.com/v1/public/creators/5003", "role": "colorist", "name": "Simone Peruzzi"}, {"resourceURI": "http://gateway.marvel.com/v1/public/creators/452", "role": "other", "name": "Chris Eliopoulos"}, {"resourceURI": "http://gateway.marvel.com/v1/public/creators/676", "role": "writer", "name": "Warren Ellis"}], "returned": 5, "collectionURI": "http://gateway.marvel.com/v1/public/comics/24501/creators"}}], "offset": 0}}
    add_comic(json_data)
    json_data = {"status": "Ok", "code": 200, "copyright": "\u00a9 2016 MARVEL", "attributionText": "Data provided by Marvel. \u00a9 2016 MARVEL", "etag": "0f457d8464a59515d1695dd371f46970f7471cbd", "attributionHTML": "<a href=\"http://marvel.com\">Data provided by Marvel. \u00a9 2016 MARVEL</a>", "data": {"count": 1, "total": 1, "limit": 20, "results": [{"resourceURI": "http://gateway.marvel.com/v1/public/characters/1009629", "description": "Ororo Monroe is the descendant of an ancient line of African priestesses, all of whom have white hair, blue eyes, and the potential to wield magic.", "comics": {"available": 602, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/comics/43498", "name": "A+X (2012) #3"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/17701", "name": "Age of Apocalypse: The Chosen (1995) #1"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/12676", "name": "Alpha Flight (1983) #17"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/12694", "name": "Alpha Flight (1983) #33"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/12725", "name": "Alpha Flight (1983) #61"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/12668", "name": "Alpha Flight (1983) #127"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/21511", "name": "Astonishing X-Men (2004) #25"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/21941", "name": "Astonishing X-Men (2004) #27"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/23087", "name": "Astonishing X-Men (2004) #28"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/23937", "name": "Astonishing X-Men (2004) #29"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/24501", "name": "Astonishing X-Men (2004) #30"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/24505", "name": "Astonishing X-Men (2004) #34"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/38318", "name": "Astonishing X-Men (2004) #38"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/39318", "name": "Astonishing X-Men (2004) #44"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/40803", "name": "Astonishing X-Men (2004) #51"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/42732", "name": "Astonishing X-Men (2004) #51 (Djurdjevic Variant)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/17491", "name": "Avengers (1998) #10"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/7138", "name": "Avengers (1963) #267"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/1311", "name": "Avengers Assemble (Hardcover)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/comics/41191", "name": "Avengers Vs. X-Men (2012) #2"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009629/comics"}, "series": {"available": 155, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/series/16450", "name": "A+X (2012 - Present)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/3614", "name": "Age of Apocalypse: The Chosen (1995)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/2116", "name": "Alpha Flight (1983 - 1994)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/744", "name": "Astonishing X-Men (2004 - 2013)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/354", "name": "Avengers (1998 - 2004)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/1991", "name": "Avengers (1963 - 1996)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/1340", "name": "Avengers Assemble (2004)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/15305", "name": "Avengers Vs. X-Men (2012)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/1537", "name": "Avengers: Kang Time and Time Again (2005)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/2115", "name": "Black Panther (1998 - 2003)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/784", "name": "Black Panther (2005 - 2008)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/2226", "name": "Black Panther: Civil War (2007)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/1726", "name": "Black Panther: The Bride (2006)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/15691", "name": "Black Panther: The Man Without Fear (2010 - 2011)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/9120", "name": "Black Widow & the Marvel Girls (2009 - 2010)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/1995", "name": "Cable (1993 - 2002)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/4002", "name": "Cable (2008 - 2010)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/693", "name": "Cable & Deadpool (2004 - 2008)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/3874", "name": "Clandestine Classic Premiere (2008)"}, {"resourceURI": "http://gateway.marvel.com/v1/public/series/3751", "name": "Classic X-Men (1986 - 1990)"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009629/series"}, "modified": "2013-10-24T14:17:31-0400", "id": 1009629, "stories": {"available": 698, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/stories/497", "type": "interiorStory", "name": "Interior #497"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/648", "type": "cover", "name": "1 of 2- Black Panther crossover"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/650", "type": "cover", "name": "2 of 2- Black Panther crossover"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/2190", "type": "cover", "name": "6 of 6 - Enemy of the State"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3206", "type": "cover", "name": "Cover #3206"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3713", "type": "cover", "name": "1 of 5 - 5XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3717", "type": "cover", "name": "3 of 5 - 5XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3752", "type": "cover", "name": "1 of 3 - Hath No Fury"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3846", "type": "cover", "name": "5 of 5 - Bride of the Panther"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3848", "type": "cover", "name": "Cover #3848"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3858", "type": "cover", "name": "1 of 3 - Civil War"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/3860", "type": "cover", "name": "2 of 3 - Civil War"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/4917", "type": "cover", "name": "1 of 4 - 4XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5473", "type": "interiorStory", "name": "2 of 6 - 6XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5474", "type": "cover", "name": "3 of 6 - 6XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5475", "type": "interiorStory", "name": "3 of 6 - 6XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5477", "type": "interiorStory", "name": "4 of 6 - 6XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5479", "type": "interiorStory", "name": "5 of 6 - 6XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5480", "type": "cover", "name": "6 of 6 - 6XLS"}, {"resourceURI": "http://gateway.marvel.com/v1/public/stories/5481", "type": "interiorStory", "name": "6 of 6 - 6XLS"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009629/stories"}, "urls": [{"url": "http://marvel.com/characters/57/storm?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "detail"}, {"url": "http://marvel.com/universe/Storm?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "wiki"}, {"url": "http://marvel.com/comics/characters/1009629/storm?utm_campaign=apiRef&utm_source=f28cee0df52d38e16d477eea4fe0ac6d", "type": "comiclink"}], "events": {"available": 21, "items": [{"resourceURI": "http://gateway.marvel.com/v1/public/events/116", "name": "Acts of Vengeance!"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/227", "name": "Age of Apocalypse"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/303", "name": "Age of X"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/233", "name": "Atlantis Attacks"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/310", "name": "Avengers VS X-Men"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/238", "name": "Civil War"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/240", "name": "Days of Future Present"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/245", "name": "Enemy of the State"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/246", "name": "Evolutionary War"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/248", "name": "Fall of the Mutants"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/249", "name": "Fatal Attractions"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/252", "name": "Inferno"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/29", "name": "Infinity War"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/255", "name": "Initiative"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/37", "name": "Maximum Security"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/299", "name": "Messiah CompleX"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/263", "name": "Mutant Massacre"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/154", "name": "Onslaught"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/270", "name": "Secret Wars"}, {"resourceURI": "http://gateway.marvel.com/v1/public/events/271", "name": "Secret Wars II"}], "returned": 20, "collectionURI": "http://gateway.marvel.com/v1/public/characters/1009629/events"}, "thumbnail": {"path": "http://i.annihil.us/u/prod/marvel/i/mg/6/40/526963dad214d", "extension": "jpg"}, "name": "Storm"}], "offset": 0}}
    add_character(json_data)

@manager.command
def test_dummy_data():
    logger.debug("test dummy data")
    app.config['SQLALCHEMY_ECHO'] = True
    creator = Creator.query.first()
    logger.debug(creator.first_name)
    logger.debug(creator.comics)
    comic = Comic.query.first()
    logger.debug(comic.title)
    logger.debug(comic.characters)
    logger.debug(comic.creators)
    character = Character.query.first()
    logger.debug(character.name)
    logger.debug(character.comics)

@manager.command
def drop_db():
    logger.debug("drop_db")
    app.config['SQLALCHEMY_ECHO'] = True
    db.drop_all()

@manager.command
def add_characters():
    logger.debug("add characters")
    app.config['SQLALCHEMY_ECHO'] = True
    with open("characters.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                add_character(json_data)

@manager.command
def add_comics():
    logger.debug("add comics")
    app.config['SQLALCHEMY_ECHO'] = True
    with open("comics1.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                add_comic(json_data)
    with open("comics2.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                add_comic(json_data)

@manager.command
def add_creators():
    logger.debug("add creators")
    app.config['SQLALCHEMY_ECHO'] = True
    with open("creators.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                add_creator(json_data)

@manager.command
def update_characters():
    logger.debug("update characters")
    app.config['SQLALCHEMY_ECHO'] = True
    with open("characters.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                update_character(json_data)


@manager.command
def update_comics():
    logger.debug("update comics")
    app.config['SQLALCHEMY_ECHO'] = True
    with open("comics1.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                update_comic(json_data)
    with open("comics2.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                update_comic(json_data)

@manager.command
def update_creators():
    logger.debug("update creators")
    app.config['SQLALCHEMY_ECHO'] = True
    with open("creators.json") as data_file:
        data = json.load(data_file)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                json_data = data[i][j]
                update_creator(json_data)

@manager.command
def test_all_data():
    logger.debug("test all data")
    app.config['SQLALCHEMY_ECHO'] = True
    creators = Creator.query.all()
    for creator in creators:
        logger.debug(creator.first_name)
        logger.debug(creator.comics)
    comics = Comic.query.all()
    for comic in comics:
        logger.debug(comic.title)
        logger.debug(comic.characters)
        logger.debug(comic.creators)
    characters = Character.query.all()
    for character in characters:
        logger.debug(character.name)
        logger.debug(character.comics)

if __name__ == '__main__':
    manager.run()
