



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String line = sc.nextLine();
            try {
               int range = Integer.parseInt(line);
               int[] res = this.fib_seq(range);
               String result = Arrays.toString(res);
                System.out.println(result);
            }
            catch (NumberFormatException e)
            {
               System.out.println("Not a valid integer.");
            }

        }

    }
}