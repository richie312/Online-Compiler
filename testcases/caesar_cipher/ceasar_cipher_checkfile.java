



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
                String[] strArray = str.split("|");
                String text = strArray[0];
                text = text.substring(0, str.length() - 1);
                text = text.substring(1, str.length());
                int key = Integer.parseInt(strArray[1]);
               System.out.println(this.caesar_cipher(text, key));
            }
            catch (Exception e)
            {
               System.out.println("Exception caught. " + e.toString());
            }

        }

    }
}