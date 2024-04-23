#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = argv[2];

request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
