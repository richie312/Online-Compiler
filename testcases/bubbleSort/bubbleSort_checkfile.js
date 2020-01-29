str = readline();

// clean brackets
str = str.substring(0, str.length - 1);
str = str.substring(1, str.length);

intArr = str;
for(i=0; i<intArr.length; i++){
    intArr[i] = parseInt(intArr[i]);
}

console.log("[" + bubbleSort(intArr) + "]");
