#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Get arguments from command line
const [, , url, filePath] = process.argv;

// Function to fetch webpage content and store it in a file
function fetchAndStore (url, filePath) {
  // Make request to the URL
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error occurred while fetching the webpage:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to fetch webpage. Status code:', response.statusCode);
      return;
    }

    // Write body content to file
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error('Error occurred while writing to file:', err);
      }
      // console.log('Webpage content successfully stored in', filePath);
    });
  });
}

// Call function to fetch and store webpage content
fetchAndStore(url, filePath);
