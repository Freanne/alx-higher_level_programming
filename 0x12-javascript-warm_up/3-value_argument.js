#!/usr/bin/node

const nbrArg = process.argv[2];

if (nbrArg === undefined) {
  console.log('No argument');
} else {
  console.log(nbrArg);
}
