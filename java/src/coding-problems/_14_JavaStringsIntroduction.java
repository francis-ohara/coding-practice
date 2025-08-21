// Link: https://www.hackerrank.com/challenges/java-strings-introduction/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _14_JavaStringsIntroduction {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String A = scanner.next();
        String B = scanner.next();

        System.out.println(A.length() + B.length());

        if (isLexicographicallyGreater(A, B)){
            System.out.println("Yes");
        }
        else
            System.out.println("No");

        System.out.println((char) (A.charAt(0) - 32) + A.substring(1 ) + " " + (char) (B.charAt(0) - 32) + B.substring(1 ));
    }

    public static boolean isLexicographicallyGreater(String a, String b){
        int length = a.length() < b.length()? a.length(): b.length();
        for (int i = 0; i < length; i++){
             if (a.charAt(i) > b.charAt(i)){
                 return true;
             }
             else if (a.charAt(i) < b.charAt(i)){
                 return false;
             }
        }
        return false;
    }
}
