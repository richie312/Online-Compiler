

$hi = fopen('php://stdin', "r");

while($line = fgets($hi)){
    $list_input1 = explode(',', $line);
    print(implode(",",popping_blocks($list_input1)));
} 


?>