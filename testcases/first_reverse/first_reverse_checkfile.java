



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String name = sc.nextLine();
            System.out.println(this.FirstReverse(name));
        }

    }
}