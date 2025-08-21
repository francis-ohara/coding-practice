package programming_with_java._1_javafundamentals.assignment1.question1.selectionsort;

import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] numbers = {-3, 4, 56, -6, -7, 42, 18, 61, 9, 23, 14, 42};
        int current;

        System.out.println("Unsorted Array: " + Arrays.toString(numbers));
        System.out.println("----Sorting----");

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[j] < numbers[i]) {
                    current = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = current;
                }
            }
        }

        System.out.println("Sorted Array: " + Arrays.toString(numbers));
    }
}