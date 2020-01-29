

$hi = fopen('php://stdin', "r");

while($line = fgets($hi)){
    $list_input1 = explode(',', $line);
    print(implode(",",bubbleSort($list_input1)));
} 


?>