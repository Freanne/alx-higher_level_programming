#!/usr/bin/node

const arg = process.argv[2];

if (typeof (arg) === Number) {
  console.log('My number: ${arg}');
} else {
  console.log('Not a number');
}
