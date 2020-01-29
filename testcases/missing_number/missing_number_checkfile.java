



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String str = sc.nextLine();
            String[] strArray = str.split(" ");
            String intArray = strArray[0];
            int num = Integer.parseInt(strArray[1]);
            if (intArray != null && intArray.length() > 0) {
                intArray = intArray.substring(0, intArray.length() - 1);
                intArray = intArray.substring(1, intArray.length());
            }
            intArray = intArray.split(",");
            int[] arr = new int[intArray.length];
            int i=0;
            for(String s:intArray){
                arr[i] = Integer.parseInt(s);
                i++;
            }


            System.out.println(this.missingNumbers(arr, num));
        }

    }
}