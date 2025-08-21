package programming_with_java._1_javafundamentals.assignment1.question2.javastdinandstdout;

import java.util.*;

public class JavaStdinAndStdout {

    public static void main(String[] args) {
        // Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution.
        int number1, number2, number3;
        Scanner input = new Scanner(System.in);

        number1 = input.nextInt();
        number2 = input.nextInt();
        number3 = input.nextInt();

        System.out.println(number1);
        System.out.println(number2);
        System.out.println(number3);

    }
}