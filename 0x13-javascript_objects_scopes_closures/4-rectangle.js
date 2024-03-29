#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {}; // Empty object if width or height is not positive
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Exchange the width and height values
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Double the width and height values
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
