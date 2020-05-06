#!/usr/bin/node
// function that increments and calls a function.

const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
    console.log('New value: ' + nb);
});