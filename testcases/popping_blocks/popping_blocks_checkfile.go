


func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    sys_input := strings.Split(scanner.Text()," ")
    fmt.Println(popping_blocks(sys_input[0]))
  }
}
