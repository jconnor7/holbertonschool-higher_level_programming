#!/usr/bin/node
// Searches for the second biggest integer in the list of arguments

const arrayLen = process.argv.length;
const newArray = [];
let max2 = 0;

if (process.argv.length <= 3) {
  console.log('0');
} else {
  for (let i = 2; i < arrayLen; i++) {
    newArray.push(process.argv[i]);
  }
  newArray.sort();
  max2 = newArray[newArray.length - 2];
  console.log(max2);
}
