package programming_with_java._1_javafundamentals.assignment1.question2.java1darray;

import java.io.*;
import java.util.*;

public class Java1DArray {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = input.nextInt();
        for (int number : a)
            System.out.println(number);
    }
}