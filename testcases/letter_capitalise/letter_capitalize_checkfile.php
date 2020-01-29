
$hi = fopen('php://stdin', "r");
$ho = fopen('php://stdout', "w");

while($line = fgets($hi)){ 
    fwrite($ho,sprintf("%s\n", LetterCapitalize($line)));
} 


?>