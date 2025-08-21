// Link: https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem?isFullScreen=true
package hackerrank;

import java.util.Scanner;

public class _2_JavaStdinAndStdout1 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        System.out.println(a + "\n" + b + "\n" + c);
    }
}
