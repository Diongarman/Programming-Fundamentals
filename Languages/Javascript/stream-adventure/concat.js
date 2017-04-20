var concat = require('concat-stream');
var split = require('split');

var reverse = function(string) {
	return string.split('').reverse().join('');
}

process.stdin.pipe(concat(function(string) {
	return string.split('').reverse().join('');
})).pipe(process.stdout);