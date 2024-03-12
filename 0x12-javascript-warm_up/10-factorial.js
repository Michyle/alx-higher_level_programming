#!/usr/bin/node

function fact(n) {
	if (isNaN(n)) {
		return 1;
	} else if ( n === 0) {
		return 1;
	} else {
		return n * fact(n - 1);
	}
}

const x = parseInt(process.argv[2]);
console.log(fact(x));
