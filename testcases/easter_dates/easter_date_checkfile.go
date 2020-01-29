
func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    sys_input, _ := strconv.Atoi(scanner.Text()) 
    fmt.Println(easter_date(sys_input))
  }
}
