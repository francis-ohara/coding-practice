package programming_with_java._1_javafundamentals.assignment1.question2.javaoutputformatting;


import java.util.*;

public class JavaOutputFormatting {

    public static void main(String[] args) {
        // Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution.
        Scanner input = new Scanner(System.in);
        String string;
        int number;

        System.out.println("================================");

        for (int i = 0; i < 3; i++) {
            string = input.next();
            number = input.nextInt();
            System.out.printf("%-15s%03d\n", string, number);
        }

        System.out.println("================================");

    }
}