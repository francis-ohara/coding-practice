// link: https://www.hackerrank.com/challenges/java-stdin-stdout/problem?isFullScreen=true
package hackerrank;

import java.util.Scanner;

public class _4_JavaStdinAndStdout2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        double b = scanner.nextDouble();
        scanner.nextLine();
        String c = scanner.nextLine();

        System.out.println("String: " + c);
        System.out.println("Double: " + b);
        System.out.println("Int: " + a);
    }
}