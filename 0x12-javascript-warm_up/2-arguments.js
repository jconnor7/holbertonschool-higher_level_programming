#!/usr/bin/node
// Prints a message depending of the number of arguments passed

let len_argv = process.argv.length;

if (len_argv > 3) {
  console.log('Arguments found');
} else if (len_argv == 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
