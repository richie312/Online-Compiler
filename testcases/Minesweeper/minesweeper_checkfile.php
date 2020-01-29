


$hi = fopen('php://stdin', "r");
$ho = fopen('php://stdout', "w");

while($line = fgets($hi)){
    $list_input1 = explode(',', $line);
    print(implode(",",num_grid($list_input1)));
} 


?>