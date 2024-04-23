#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach(todo => {
      if (todo.completed) {
        completed[todo.userId] = (completed[todo.userId] || 0) + 1;
      }
    });

    console.log(completed);
  } else {
    console.error('Error:', error);
  }
});
