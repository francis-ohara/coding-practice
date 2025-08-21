package programming_with_java._1_javafundamentals.assignment1.question2.javaifelse;

import java.util.*;

public class JavaIfElse {

    public static void main(String[] args) {
        // Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution.
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        if (n % 2 == 1)
            System.out.println("Weird");
        else if (n >= 2 && n <= 5)
            System.out.println("Not Weird");
        else if (n >= 6 && n <= 20)
            System.out.println("Weird");
        else
            System.out.println("Not Weird");
    }
}