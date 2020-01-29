



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String str = sc.nextLine();
            try {
                if (str != null && str.length() > 0) {
                    str = str.substring(0, str.length() - 1);
                    str = str.substring(1, str.length());
                }
                String[] strArray = str.split(",");
                int[] intArray = new int[strArray.length];
                for(int i = 0; i < strArray.length; i++) {
                    intArray[i] = Integer.parseInt(strArray[i]);
                }
                int[] res = this.bubbleSort(intArray);
               System.out.println(Arrays.toString(res));
            }
            catch (Exception e)
            {
               System.out.println("Exception caught. " + e.toString());
            }

        }

    }
}