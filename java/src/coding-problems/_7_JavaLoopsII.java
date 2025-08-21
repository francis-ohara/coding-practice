// Link: https://www.hackerrank.com/challenges/java-loops/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _7_JavaLoopsII {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int n = scanner.nextInt();
            int term = a;

            for (int j = 0; j < n; j ++){
                term +=  (int) (b * Math.pow(2, j));
                System.out.print(term + " ");
            }
            System.out.println();
        }
    }
}