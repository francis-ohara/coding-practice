// link: https://www.hackerrank.com/challenges/java-output-formatting/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _5_JavaOutputFormatting {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i ++){
            String[] input = scanner.nextLine().split(" ");
            String string = input[0];
            int number = Integer.parseInt(input[1]);
            System.out.printf("%-15s%03d%n",string, number);
        }
        System.out.println("================================");
    }
}
