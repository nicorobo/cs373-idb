// marvel.js

const request = require('request');
const API = 'http://sweague.me/api/';

// Retrieve the character with the given ID
function getCharacter(id, cb){
	request(API+'character/'+id, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}

//Retrieve characters
function getCharacters(limit, offset, cb){
	request(`${API}characters?limit=${limit}&offset=${offset}`, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}

//Retrieve comic with given ID
function getComic(id, cb){
	request(API+'comic/'+id, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}

//Retrieve comics
function getComics(limit, offset, cb){
	request(`${API}comics?limit=${limit}&offset=${offset}`, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}

//Retrieve creator with given ID
function getCreator(id, cb){
	request(API+'creator/'+id, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}

//Retrieve creators
function getCreators(limit, offset, cb){
	request(`${API}creators?limit=${limit}&offset=${offset}`, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}

//Search
function search(term, cb){
	request(API+'search/'+term, (error, response, body) => {
		error = error || (isJson(body) ? null : 'API response is not valid JSON (perhaps HTML)');
		if (!error) body = JSON.parse(body);
		cb(error, body);
	})
}
function isJson(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}

module.exports = {
	getCharacter: getCharacter,
	getCharacters: getCharacters,
	getComic: getComic,
	getComics: getComics,
	getCreator: getCreator,
	getCreators: getCreators,
	search: search
}
