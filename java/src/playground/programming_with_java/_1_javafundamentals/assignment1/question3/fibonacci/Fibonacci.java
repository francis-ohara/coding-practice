package programming_with_java._1_javafundamentals.assignment1.question3.fibonacci;
import java.util.Scanner;
public class Fibonacci {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the position of the number in the Fibonacci sequence you would like to know:");
        int n = input.nextInt();

        System.out.printf("The number at position %d in the Fibonacci sequence is %d.", n, fibonacci(n));
    }

    static int fibonacci(int n) {
        if (n == 0)
            return 0;
        else if (n == 1)
            return 1;
        else
            return fibonacci(n - 1) + fibonacci(n - 2);
    }
}