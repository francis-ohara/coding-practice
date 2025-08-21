package programming_with_java._1_javafundamentals.lesson1.question5;

import java.util.Scanner;

public class Question5 {
    public static void main(String[] args) {

        // Ask the user to enter 10 integers; Find ratio of positive integers to negative integers.

        Scanner input = new Scanner(System.in);
        int nPositive = 0;
        int nNegative = 0;
        int number;
        System.out.println("You are about to enter 10 integers.");
        for (int i = 0; i < 10; i++) {
            System.out.printf("Enter number %d:\t", i + 1);
            number = input.nextInt();
            if (number > 0) nPositive++;
            else if (number < 0) nNegative++;
        }
        if (nNegative == 0)
            System.out.println("Error! Enter at least 1 negative integer.");
        else if (nPositive == 0)
            System.out.println("Error! Enter at least 1 positive integer.");
        else {
            double ratio = nPositive / (double) nNegative;
            System.out.printf("The ratio is %.2f.", ratio);
        }
    }
}
