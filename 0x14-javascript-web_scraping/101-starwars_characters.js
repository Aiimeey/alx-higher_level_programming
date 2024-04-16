#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function check (error, response) {
  if (error) {
    console.error(error);
  }
}
request(url, async (error, response, body) => {
  check(error, response);

  JSON.parse(body).characters.forEach(x => {
    request(x, async (error, response, body) => {
      check(error, response);
      x = JSON.parse(body);
      console.log(x.name);
    });
  });
});

