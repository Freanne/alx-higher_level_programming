#!/usr/bin/node
const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  constructor (size) {
    // Call the constructor of the parent class (Square)
    super(size);
  }

  // Instance method to print the square using the character c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = SquareWithCharPrint;
