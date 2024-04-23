#!/usr/bin/node
// Prints the number of movies where "Wedge Antilles" is present

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  
  if (res.statusCode !== 200) {
    console.error('Invalid');
    return;
  }

  const films = JSON.parse(body).results;
  const count = films.reduce((acc, film) => {
    if (film.characters.some(character => character.includes('/18/'))) {
      return acc + 1;
    }
    return acc;
  }, 0);

  console.log(count);
});
