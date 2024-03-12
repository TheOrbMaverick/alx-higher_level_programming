#!/usr/bin/node

const num = parseInt(process.argv[2]);

// Check if the parsed number is a positive integer
if (Number.isInteger(num) && num > 0) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else if (num < 0) {
  process.exit();
} else {
  console.log('Missing number of occurrences');
}
