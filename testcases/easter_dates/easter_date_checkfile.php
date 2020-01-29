
$hi = fopen('php://stdin', "r");
$ho = fopen('php://stdout', "w");

while(fscanf($hi, "%d", $n1)){ 
    fwrite($ho,sprintf("%d\n", easter_date($n1)));
} 


?>








