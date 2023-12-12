#!/usr/bin/node
const args = process.argv.slice(2);
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

function add (a, b) {
  console.log(a + b);
}
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  add(num1, num2);
}
