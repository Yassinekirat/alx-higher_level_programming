#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const fetchCharacterNames = (characterUrls) => {
    characterUrls.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, characterBody) => {
        if (error) {
          console.error(error);
          return;
        }

        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
      });
    });
  };

  fetchCharacterNames(characters);
});
