#!/usr/bin/node

const nombreArguments = process.argv.length - 2;

if (nombreArguments === 0) {
  console.log('No argument');
} else if (nombreArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
