//cheated

var through = require('through');
var split = require('split');

var even = false;

var transform = through(function(line) {
	line = line.toString();
	if (even) {
		line = line.toUpperCase();
	}
	else {
		line = line.toLowerCase();
	}
	even = !even;
	this.queue(line + "\n");

});

process.stdin
	.pipe(split())
	.pipe(transform)
	.pipe(process.stdout);


//original solution

// var through = require('through2');
// var split = require('split');

// var stream = through(write,end);

// process.stdin.pipe(split()).pipe(stream)
// ;
// //functions
// 	//through functions
// function write (line, _, next) {

// 	//console.dir(line.toString());
// 	data.push(line.toString());
// 	next();
// }

// function end(done){
// 	i = 0;
// 	for (line in data){
		
// 		if ((i+1) % 2 === 0){
// 			console.dir(data[line].toUpperCase())
// 		}
// 		else {console.dir(data[line].toLowerCase())}
	
// 		i++;
// 	}

// 	done();
// }

// data = [];

