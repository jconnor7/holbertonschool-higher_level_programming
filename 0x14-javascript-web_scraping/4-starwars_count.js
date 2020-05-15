#!/usr/bin/node}
// A script that prints the number of movies
// where the character Wedge Antilles is present

const Request = require('request');
const url = process.argv[2];
let number = 0;
Request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    let character = [];
    data.results.forEach(item => {
      for (character of item.characters) {
        if (character.endsWith('/18/')) {
          number++;
        }
      }
    });
    console.log(number);
  }
});
