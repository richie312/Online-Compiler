



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String line = sc.nextLine();
            try {
               int num = Integer.parseInt(line);
               System.out.println(this.FirstFactorial(num));
            }
            catch (NumberFormatException e)
            {
               System.out.println("Not a valid integer.");
            }

        }

    }
}