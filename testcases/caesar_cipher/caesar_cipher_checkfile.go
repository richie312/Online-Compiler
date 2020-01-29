
func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    sys_input := strings.Split(scanner.Text(),"|")
    b, _ := strconv.Atoi(sys_input[1]) 
    
    fmt.Println(caesar_cipher(sys_input[0],b))
  }
}
