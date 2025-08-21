package programming_with_java._1_javafundamentals.lesson1.question3;
import java.util.Scanner;

public class Question3 {
    public static void main (String[] args) {

        // Write a program that accepts two numbers; prints which is greater or if both are equal.

        Scanner input = new Scanner(System.in);
        int firstNumber;
        int secondNumber;
        System.out.println("Enter first number:");
        firstNumber = Integer.parseInt(input.next());
        System.out.println("Enter second number:");
        secondNumber = Integer.parseInt(input.next());

        if (firstNumber > secondNumber) {
            System.out.printf("%d is greater than %d.", firstNumber, secondNumber);
        } else if (secondNumber > firstNumber) {
            System.out.printf("%d is greater than %d.", secondNumber, firstNumber);
        } else System.out.println("Both numbers are equal.");
    }
}
