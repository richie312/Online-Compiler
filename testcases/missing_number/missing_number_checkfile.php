

$hi = fopen('php://stdin', "r");
$ho = fopen('php://stdout', "w");

while($line = fgets($hi)){
    $array = explode(' ', $line, 2);
    $list_input1 = explode(',', $array[0]);
    print(implode(","missingNumbers($list_input1, number_format($array[1]))));
} 


?>
