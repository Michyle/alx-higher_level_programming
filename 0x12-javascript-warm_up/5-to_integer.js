#!/usr/bin/node

const num = process.argv[2];

if (!isNaN(parseInt(num))){
	console.log('My number is : ${parseInt(num)}');
} else {
	console.log('Not a number');
}
