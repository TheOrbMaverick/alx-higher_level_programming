#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments are provided
if (arg1 !== undefined && arg2 !== undefined) {
  console.log(add(arg1, arg2));
} else {
  console.log('NaN');
}
