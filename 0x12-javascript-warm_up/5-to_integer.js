#!/usr/bin/node

const arg = process.argv[2];
const num = parseInt(arg); // Try to convert the argument to an integer

// Check if the parsed number is an integer and not NaN
if (Number.isInteger(num) && !isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
