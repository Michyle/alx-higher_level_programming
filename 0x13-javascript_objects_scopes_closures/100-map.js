#!/usr/bin/node
const list = require('./100-data').lists;
console.log(list);
console.log(list.map((x, i) => x * i));
