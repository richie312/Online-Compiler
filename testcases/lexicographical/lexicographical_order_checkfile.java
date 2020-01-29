



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String str = sc.nextLine();
            String[] res = this.sortLexo(str);
            System.out.println(Arrays.toString(res));
        }

    }
}