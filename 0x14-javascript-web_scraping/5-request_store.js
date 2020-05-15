#!/usr/bin/node
// A script that gets the contents of a WebPage and stores it in a file

const request = require('request');
const url = process.argv[2];

const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
