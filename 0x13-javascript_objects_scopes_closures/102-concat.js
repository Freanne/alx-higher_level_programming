#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = args[0];
const fileBPath = args[1];
const fileCPath = args[2];

// Read the contents of fileA
const fileAContent = fs.readFileSync(fileAPath, 'utf8');

// Read the contents of fileB
const fileBContent = fs.readFileSync(fileBPath, 'utf8');

// Concatenate the contents of fileA and fileB
const concatenatedContent = fileAContent + fileBContent;

// Write the concatenated content to fileC
fs.writeFileSync(fileCPath, concatenatedContent);
