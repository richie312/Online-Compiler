



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String str = sc.nextLine();
            String[] strArray = str.split(",");
            int num = Integer.parseInt(strArray[0]);
            int exp = Integer.parseInt(strArray[1]);
//             int jump = Integer.parseInt(strArray[2]);
            System.out.println(this.indices(num, exp));
        }

    }
}