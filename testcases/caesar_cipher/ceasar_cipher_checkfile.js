while(line=readline()){
    var strArr = line.split("|");
    var txt = strArr[0];
    txt = txt.substring(1, txt.length -1);
    var key = parseInt(strArr[1]);
    print(caesar_cipher(txt, key))
}