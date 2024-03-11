#!/usr/bin/node

const Mynumber = process.argv[2]
if (isNaN(Mynumber)) {
  console.log('Not a number');
} else {
  console.log('My number is ' + parseInt(Mynumber))
}
