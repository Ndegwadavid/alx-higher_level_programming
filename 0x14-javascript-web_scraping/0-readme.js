#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, 'utf-8', function (err, data) {
    if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
})