// Link: https://www.hackerrank.com/challenges/java-string-reverse/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _17_JavaStringReverse {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        String result = "Yes";

        for (int i = 0; i < (word.length() / 2); i ++){
            if (word.charAt(i) != word.charAt(word.length() - 1 - i)){
                result = "No";
                break;
            }
        }
        System.out.println(result);
    }
}