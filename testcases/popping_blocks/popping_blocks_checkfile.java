



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String str = sc.nextLine();
            if (str != null && str.length() > 0) {
                str = str.substring(0, str.length() - 1);
                str = str.substring(1, str.length());
            }
            String[] strArray = str.split(",");
            String[] res = this.popping_blocks(strArray);
            System.out.println(Arrays.toString(res));
        }

    }
}