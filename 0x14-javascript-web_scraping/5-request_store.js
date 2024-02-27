#!/usr/bin/node
const fs = require('fs');
const https = require('https');

if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

const request = https.get(url, (response) => {
  let responseBody = '';

  response.setEncoding('utf8');

  response.on('data', (chunk) => {
    responseBody += chunk;
  });

  response.on('end', () => {
    fs.writeFile(filePath, responseBody, { encoding: 'utf8' }, (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        process.exit(1);
      }
      console.log('File saved successfully.');
    });
  });
});

request.on('error', (err) => {
  console.error('Error requesting URL:', err);
  process.exit(1);
});
