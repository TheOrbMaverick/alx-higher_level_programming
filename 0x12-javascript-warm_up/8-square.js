#!/usr/bin/node

const size = parseInt(process.argv[2]);

// Check if the size can be converted to a positive integer
if (Number.isInteger(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
