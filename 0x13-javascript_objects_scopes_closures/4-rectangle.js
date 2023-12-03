#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check if w or h is not a positive integer
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // Create an empty object
      return {};
    }

    // Initialize the instance attributes width and height
    this.width = w;
    this.height = h;
  }

  // Instance method to print the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method to exchange the width and height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method to multiply the width and height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
