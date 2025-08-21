package programming_with_java._1_javafundamentals.assignment1.question1.insertionsort;

import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] Args) {
        int[] numbers = {-3, 4, 56, -7, 42, 18, 61, 9, 23, 14};
        int temp;

        System.out.println("Unsorted Array: " + Arrays.toString(numbers));
        System.out.println("----Sorting----");

        for (int i = 1; i < numbers.length; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (numbers[j] > numbers[j + 1]) {
                    temp = numbers[j + 1];
                    numbers[j + 1] = numbers[j];
                    numbers[j] = temp;
                } else break;
            }
        }

        System.out.println("Sorted Array: " + Arrays.toString(numbers));
    }
}