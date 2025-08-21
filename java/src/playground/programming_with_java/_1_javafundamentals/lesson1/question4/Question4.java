package programming_with_java._1_javafundamentals.lesson1.question4;

import java.util.Scanner;

public class Question4 {
    public static void main(String[] args) {

         /*
         Write a program that accepts 3 integers, start, stop, and step, and prints all integers between start inclusive and stop exclusive with an interval of step.
             1. Implement with for loop.
             2. Implement with while loop.
         */

        int start, stop, step;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter start integer:");
        start = input.nextInt();
        System.out.println("Enter stop integer:");
        stop = input.nextInt();
        System.out.println("Enter step integer:");
        step = input.nextInt();

        // i
        for (int i = start; i < stop; i += step) {
            System.out.print(i + " ");
        }

        System.out.println();

        // ii
        while (start < stop) {
            System.out.print(start + " ");
            start += step;
        }
    }
}
