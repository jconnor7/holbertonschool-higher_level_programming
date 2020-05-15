#!/usr/bin/node
// A script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2] + '?completed=true';
const newDict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    for (const data of jsonBody) {
      if (data.userId in newDict) {
        newDict[data.userId] = newDict[data.userId] + 1;
      } else {
        newDict[data.userId] = 1;
      }
    }
  }
  console.log(newDict);
});
