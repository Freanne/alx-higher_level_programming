#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

// Populate the new dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  if (newDict[occurrences] === undefined) {
    newDict[occurrences] = [userId];
  } else {
    newDict[occurrences].push(userId);
  }
}

console.log(newDict);
