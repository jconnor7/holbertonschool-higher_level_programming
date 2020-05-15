#!/usr/bin/node
// A script that display the status code of a GET request

const Request = require('request');
const url = process.argv[2];

Request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        console.log('code:', response.statusCode);
    }
});