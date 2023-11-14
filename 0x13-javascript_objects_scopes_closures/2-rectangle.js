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
}

module.exports = Rectangle;
