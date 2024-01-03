#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const args = process.argv;
const text = args[2];
const file = args[3];
fs.writeFile(file, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
