#!/usr/bin/node

const { addMeMaybe, incr } = require('./103-object_fct');

const myObject = {
  type: 'object',
  value: 12,
  incr
};
console.log(myObject);

addMeMaybe(myObject.value, function (newVal) {
  myObject.value = newVal;
});

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
