#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
    if (sortedDict[occurrences] === undefined) {
      sortedDict[occurrences] = [];
    }
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
