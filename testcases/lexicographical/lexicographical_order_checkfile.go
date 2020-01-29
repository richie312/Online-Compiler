



func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    fmt.Println(SortLexo(scanner.Text()))
  }
}

