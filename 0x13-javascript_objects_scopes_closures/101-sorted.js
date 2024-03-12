#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const key in dict) {
  if (Object.prototype.hasOwnProperty.call(dict, key)) {
    const value = dict[key];
    newDict[value] = newDict[value] || [];
    newDict[value].push(key);
  }
}

console.log(newDict);
