#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    let json = JSON.parse(body);
    console.log(JSON.parse(body).title);
  }
});
