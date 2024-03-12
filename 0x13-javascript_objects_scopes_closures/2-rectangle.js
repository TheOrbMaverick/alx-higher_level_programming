#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (arguments.length !== 1 || w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
