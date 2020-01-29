$hi = fopen('php://stdin', "r");
$ho = fopen('php://stdout', "w");

while(fscanf($hi, "%d %d", $n1, $n2)){ 
    fwrite($ho,sprintf("%d\n", Indices($n1,$n2)));
} 


?>