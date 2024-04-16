#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function check (error, response) {
  if (error) {
    console.error(error);
  }
}
request(url, (error, response, body) => {
  check(error, response);

  const data = JSON.parse(body);

  const char = data.characters;

  char.forEach(x => {
    request(x, (error, response, body) => {
      check(error, response);
      x = JSON.parse(body);
      console.log(x.name);
    });
  });
});
