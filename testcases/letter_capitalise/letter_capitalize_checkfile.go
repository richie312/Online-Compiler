

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    fmt.Println(LetterCapitalize(scanner.Text()))
  }
}
