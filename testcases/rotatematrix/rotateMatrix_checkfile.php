


$hi = fopen('php://stdin', "r");
$ho = fopen('php://stdout', "w");

while($line = fgets($hi)){
    $list_input1 = explode(',', $line);
    print(implode(",",rotateMatrix($list_input1)));
} 


?>