#!/usr/bin/node
const fs = require('fs');
/*
console.log("Executable path:", process.argv[0]);
console.log("Script path:", process.argv[1]);
console.log("Command-line arguments:", process.argv[2]);
*/
if (process.argv.length > 2) {
  const filePath = process.argv[2];

  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
