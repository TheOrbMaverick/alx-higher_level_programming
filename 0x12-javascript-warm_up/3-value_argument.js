#!/usr/bin/node

const arg = process.argv[2];

// Check if the argument is undefined (no argument passed)
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
