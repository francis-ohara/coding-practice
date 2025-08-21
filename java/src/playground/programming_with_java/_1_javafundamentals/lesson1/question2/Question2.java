package programming_with_java._1_javafundamentals.lesson1.question2;

import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
          /*
          Write a program that accepts two integer inputs from the keyboard and performs the following:
          i. addition
          ii. subtraction
          iii. multiplication
          iv. division first number / second number
                explain your answer
                correct if necessary
          v. first number raised to second number
          vi. square root of sum of first and second number
          */

        Scanner input = new Scanner(System.in);
        int num1, num2;
        System.out.println("Enter number 1:");
        num1 = Integer.parseInt(input.next());
        System.out.println("Enter number 2:");
        num2 = Integer.parseInt(input.next());

        // i
        int sum = num1 + num2;
        System.out.printf("The sum of %d and %d is %d.\n", num1, num2, sum);

        // ii
        int difference = num1 - num2;
        System.out.printf("The difference between %d and %d is %d.\n", num1, num2, difference);

        // iii
        int product = num1 * num2;
        System.out.printf("The product of %d and %d is %d.\n", num1, num2, product);

        // iv
        double quotient = num1 / (double) num2;
        System.out.printf("The quotient of %d and %d is %f.\n", num1, num2, quotient);

        // v
        int power = (int) Math.pow(num1, num2);
        System.out.printf("%d raised to the power %d is %d.\n", num1, num2, power);


        // vi
        double root = Math.pow(num1 + num2, 0.5); //or Math.sqrt
        System.out.printf("The square root of the sum of %d and %d is %.2f.\n", num1, num2, root);

    }
}
