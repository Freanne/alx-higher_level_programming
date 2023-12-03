#!/usr/bin/node

const nbr = process.argv[2];
let i;
if (nbr === undefined) {
  console.log('Missing number of occurrences');
}

for (i = 0; i < nbr; i++) {
  console.log('C is fun');
}
