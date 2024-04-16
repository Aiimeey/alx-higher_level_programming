#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
/*
for (let i = 0; i < process.argv.length; i++) {
  console.log(`Argument ${i}: ${process.argv[i]}`);
  URL to request : ./2-statuscode.js https://alx-intranet.hbtn.io/status
}
*/
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
