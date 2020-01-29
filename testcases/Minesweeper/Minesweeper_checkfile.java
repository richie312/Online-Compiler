



    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);

        // String input
        while (sc.hasNextLine()){
            String str = sc.nextLine();
            str=str.replace("[","");//replacing all [ to ""
             str=str.substring(0,str.length()-2);//ignoring last two ]]
             String s1[]=str.split("],");//separating all by "],"

             String matrix[][] = new String[s1.length][s1.length];//declaring two dimensional matrix for input

             for(int i=0;i<s1.length;i++){
                 s1[i]=s1[i].trim();//ignoring all extra space if the string s1[i] has
                 String single_int[]=s1[i].split(", ");//separating integers by ", "

                 for(int j=0;j<single_int.length;j++){
                     matrix[i][j]=single_int[j];//adding single values
                 }
             }

            System.out.println(this.num_grid(matrix));
        }

    }
}