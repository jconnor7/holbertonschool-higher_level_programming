#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const Request = require('request');
const url = 'http://swapi-api.hbtn.io/api/people/';
const movieId = process.argv[2];

function reqRecursive (url) {
  Request(url, (err, response, body) => {
    if (!err) {
      const data = JSON.parse(body);
      data.results.forEach(item => {
        for (const film of item.films) {
          if (film.match(movieId)) {
            console.log(item.name);
          }
        }
      });
      if (data.next) {
        reqRecursive(data.next);
      }
    }
  });
}

reqRecursive(url);
