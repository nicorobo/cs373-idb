// marvel.js

const request = require('request');
const API = 'http://sweague.me/api/';

// Retrieve the character with the given ID
function getCharacter(id, cb){
	request(API+'character/'+id, (error, response, body) => {
		cb(error, JSON.parse(body));
	})
}

//Retrieve characters
function getCharacters(limit, offset, cb){
	request(`${API}characters?limit=${limit}&offset=${offset}`, (error, response, body) => {
		cb(error, JSON.parse(body));
	})
}

//Retrieve comic with given ID
function getComic(id, cb){
	request(API+'comic/'+id, (error, response, body) => {
		cb(error, JSON.parse(body));
	})
}

//Retrieve comics
function getComics(limit, offset, cb){
	request(`${API}comics?limit=${limit}&offset=${offset}`, (error, response, body) => {
		cb(error, JSON.parse(body));
	})
}

//Retrieve creator with given ID
function getCreator(id, cb){
	request(API+'creator/'+id, (error, response, body) => {
		cb(error, JSON.parse(body));
	})
}

//Retrieve creators
function getCreators(limit, offset, cb){
	request(`${API}creators?limit=${limit}&offset=${offset}`, (error, response, body) => {
		cb(error, JSON.parse(body));
	})
}

module.exports = {
	getCharacter: getCharacter,
	getCharacters: getCharacters,
	getComic: getComic,
	getComics: getComics,
	getCreator: getCreator,
	getCreators: getCreators
}