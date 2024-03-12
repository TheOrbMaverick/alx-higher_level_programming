#!/usr/bin/node

function secondBiggest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sort in descending order
  if (sortedNumbers.length < 2) {
    return 0;
  }
  return sortedNumbers[1]; // Second biggest element
}

const args = process.argv.slice(2).map(Number); // Convert arguments to numbers

console.log(secondBiggest(args));
