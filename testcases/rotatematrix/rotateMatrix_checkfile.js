while(line=readline()){
// line = readline()
// print(line);
	line = line.substring(1, line.length);
	line = line.substring(0, line.length - 2);
	var chunks = line.split("]");
	// print(chunks.length);

	var i;
	var mat = [];
	for(i=0; i<chunks.length; i++){
		var intArr = chunks[i];
		// print(intArr);
		intArr = intArr.split("[")[1];
		intArr = intArr.split(",");

		var j;
		var arr = [];
		for(j=0; j<intArr.length; j++){
			arr.push(parseInt(intArr[j]));
		}
		mat.push(arr);
	}
    print(JSON.stringify(rotateMatrix(mat)));

}