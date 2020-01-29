str = readline();
str = str.substring(1, str.length);

strArr = str.split("]");
intArr = strArr[0].split(",");
range = parseInt(strArr[1].trim());

for(i=0; i<intArr.length; i++){
	intArr[i] = parseInt(intArr[i]);
}

console.log("[" + missingNumbers(intArr, range) + "]");
