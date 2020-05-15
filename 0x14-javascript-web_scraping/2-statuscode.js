#!/usr/bin/node
// A script that writes a string to a file

const Request = require('request');
const url = process.argv[2];

Request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        console.log('code:', response.statusCode);
    }
});