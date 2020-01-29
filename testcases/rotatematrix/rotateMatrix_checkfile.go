

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
    
    elements_2 := strings.Split(sys_input[1],",")
    elem_count_2 := len(elements_2)
    // remove the [ character from first and last elements
    elements_2[0] = strings.Replace(elements_2[0], "[", "", -1)
    elements_2[elem_count_2 -1] = strings.Replace(elements_2[elem_count_2 -1], "]", "",-1)
    
    // convert each elements to integer
    
    for j := 0; j < 4; j, _ = strconv.Atoi(elements_2[j]) {
   }
    
    fmt.Println(rotateMatrix(elements,elements_2))
  }
}

