#!/usr/bin/node
const dic = require('./101-data').dict;

const newList = {};
for (const key in dic) {
  if (newList[dic[key]] === undefined) {
    newList[dic[key]] = [];
  }
  newList[dic[key]].push(key);
}
console.log(newList);
