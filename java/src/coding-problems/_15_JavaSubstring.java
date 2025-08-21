// Link: https://www.hackerrank.com/challenges/java-substring/problem?isFullScreen=true
package hackerrank;

import java.util.Scanner;

public class _15_JavaSubstring {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        int start = scanner.nextInt();
        int end = scanner.nextInt();
        System.out.println(word.substring(start, end));
    }
}
