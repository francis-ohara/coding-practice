// Link: https://www.hackerrank.com/challenges/java-loops-i/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _6_JavaLoopsI {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();

        for(int i = 1; i < 11; i++){
            System.out.println(number + " x " + i + " = " + (number * i));
        }
    }
}
