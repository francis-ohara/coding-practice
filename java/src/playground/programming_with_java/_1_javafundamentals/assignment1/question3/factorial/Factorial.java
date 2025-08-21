package programming_with_java._1_javafundamentals.assignment1.question3.factorial;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number whose factorial you want to calculate:");
        int n = input.nextInt();
        System.out.printf("%d! equals %d.", n, factorial(n));
    }

    static int factorial(int n) {
        if ((n == 0) || (n==1))
            return 1;
        else
            return n * factorial(n - 1);
    }
}