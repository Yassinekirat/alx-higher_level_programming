#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharacters(characters, 0);
  } else {
    console.error(error || 'Invalid request');
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacters(characters, index + 1);
    } else {
      console.error(error || 'Invalid request');
    }
  });
}
