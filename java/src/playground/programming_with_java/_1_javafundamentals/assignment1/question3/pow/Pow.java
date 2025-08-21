package programming_with_java._1_javafundamentals.assignment1.question3.pow;

import java.util.Scanner;

public class Pow {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the base number:");
        int base = input.nextInt();
        System.out.println("Enter the exponent number:");
        int exponent = input.nextInt();
        System.out.printf("%d raised to the power %d is %f.", base, exponent, power(base, exponent));
    }

    static double power(double base, int exponent) {
        if (exponent == 0)
            return 1;
        else if (exponent == 1)
            return base * exponent;
        else
            return base * power(base, exponent-1);
    }
}
