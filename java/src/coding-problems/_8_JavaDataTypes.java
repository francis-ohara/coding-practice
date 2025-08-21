// Link: https://www.hackerrank.com/challenges/java-datatypes/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _8_JavaDataTypes {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < n; i ++) {
            boolean[] supportedTypes = {true, true, true, true};
            String number = scanner.nextLine();
            try {
                byte result = Byte.parseByte(number);
            }
            catch(IllegalArgumentException e){
                supportedTypes[0] = false;
            }
            try {
                short result = Short.parseShort(number);
            }
            catch(IllegalArgumentException e){
                supportedTypes[1] = false;
            }
            try{
                int result = Integer.parseInt(number);
            }
            catch(IllegalArgumentException e){
                supportedTypes[2] = false;
            }
            try{
                long result = Long.parseLong(number);
            }
            catch(IllegalArgumentException e){
                supportedTypes[3] = false;
            }

            if (supportedTypes[3]){
                System.out.println(number + " can be fitted in:");
               if (supportedTypes[0])
                   System.out.println("* byte");
               if (supportedTypes[1])
                   System.out.println("* short");
               if (supportedTypes[2])
                   System.out.println("* int");
               System.out.println("* long");
            }
            else
                System.out.println(number + " can't be fitted anywhere.");
        }
    }
}
