

$hi = fopen('php://stdin', "r");

while($line = fgets($hi)){
    $list_input1 = explode('|', $line);
    print(implode(",",caesar_cipher($list_input1)));
} 
