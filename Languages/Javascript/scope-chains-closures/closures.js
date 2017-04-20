function foo(){
	var bar;
	quux = 'Global';
	function zip(){
		var quux = 'Scoped to zip()';
		bar = true;
		
	}
	return zip;
}
