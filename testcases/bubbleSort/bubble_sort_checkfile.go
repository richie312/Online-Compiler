

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  for scanner.Scan() {
    sys_input := strings.Split(scanner.Text()," ")
    elements := strings.Split(sys_input[0],",")
    elem_count := len(elements)
    // remove the [ character from first and last elements
    elements[0] = strings.Replace(elements[0], "[", "", -1)
    elements[elem_count-1] = strings.Replace(elements[elem_count-1], "]", "",-1)
    
    // convert each elements to integer
    
    for i := 0; i < 4; i, _ = strconv.Atoi(elements[i]) {
   }
    
    fmt.Println(bubbleSort(elements))
  }
}
