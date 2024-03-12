#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

function incr() {
  this.value++;
}

module.exports = { addMeMaybe, incr };
