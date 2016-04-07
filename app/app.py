import os
import logging
import json
import subprocess

from flask import Flask, render_template, jsonify
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
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
CORS(app)

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

@app.route('/run-tests')
def run_tests():
    b_output = subprocess.check_output(['python3', 'tests.py'], stderr=subprocess.STDOUT)
    test_output = b_output.decode('ascii')
    return render_template('about.html', test_output=test_output)

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
