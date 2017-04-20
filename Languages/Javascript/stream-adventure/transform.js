var through = require('through2');
var stream = through(write,end);


//If `write` is not specified, the default implementation passes the input 
//data to the output unmodified.
function write(buffer, encoding, next){
	this.push(buffer.toString().toUpperCase());
	next();

}

//If `end` is not specified, the default implementation calls `this.push(null)`
//to close the output side when the input side ends.

function end(done){
	done();
}

process.stdin.pipe(stream).pipe(process.stdout);



