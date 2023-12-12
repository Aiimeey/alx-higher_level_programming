#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0]);

function Factorial (Number) {
  if (Number === 1) {
    return 1;
  }
  return Number * Factorial(Number - 1);
}

if (isNaN(num)) {
  console.log('1');
} else {
  console.log(Factorial(num));
}
