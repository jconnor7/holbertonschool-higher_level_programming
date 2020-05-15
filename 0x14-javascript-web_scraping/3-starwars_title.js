#!/usr/bin/node
// A script that prints the title of a Star Wars movie
// where the episode number matches a given integer

const Request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
Request(url, (err, response, body) => {
    if (!err) {
        const data = JSON.parse(body);
        console.log(data.title);
    }
});