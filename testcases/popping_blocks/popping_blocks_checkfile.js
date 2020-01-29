

while(line=readline()){
    line = line.substring(1, line.length - 1);
    var strArr = line.split(",")
    var i;
    var arr = [];
    for(i=0; i<strArr.length; i++){
        arr.push(strArr[i].substring(1, strArr[i].length - 1));
    }
    print(JSON.stringify(popping_blocks(arr)));

}

