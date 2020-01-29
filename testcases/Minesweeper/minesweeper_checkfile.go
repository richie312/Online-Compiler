

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    sys_input := strings.Split(scanner.Text()," ")
    elements := strings.Split(sys_input[0]," ")
   // elements_2 := strings.Split(sys_input[1],",")
    fmt.Println(num_grid(elements))
  }
}
