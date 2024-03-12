#!/usr/bin/node

function factorial (n) {
  // Check if n is NaN or less than 0, return 1 for NaN and negative numbers
  if (isNaN(n) || n < 0) {
    return 1;
  }

  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }

  // Recursive case: compute factorial using recursion
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));
