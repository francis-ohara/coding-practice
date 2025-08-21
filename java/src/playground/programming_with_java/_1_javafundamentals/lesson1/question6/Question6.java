package programming_with_java._1_javafundamentals.lesson1.question6;

import java.util.Scanner;

public class Question6 {
    public static void main(String[] args) {

        // Ask the user for a positive integer; sum the digits in the number; e.g. 56 == 11

        Scanner input = new Scanner(System.in);
        int number;
        int sum = 0;
        System.out.println("Enter a positive integer:");
        number = input.nextInt();
        while (number > 0) {
            sum += number % 10;
            number = number / 10;
        }
        System.out.printf("The result is %d.", sum);

    }
}
