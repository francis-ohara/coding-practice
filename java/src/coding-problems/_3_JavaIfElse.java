// link: https://www.hackerrank.com/challenges/java-if-else/problem?isFullScreen=true
package hackerrank;

import java.util.Scanner;

public class _3_JavaIfElse {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        if (number % 2 == 1){
            System.out.println("Weird");
        }
        else{
            if (number >= 6 && number <= 20){
                System.out.println("Weird");
            }
            else
                System.out.println("Not Weird");
        }
    }
}
