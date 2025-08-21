package _2_problemsolving.bubblesort;

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {

        //bubble sort
        int[] numbers = {7, 4, 2, 18, -3, 45, 54, 23, 66, -109};
        System.out.println("---Bubble sort---");
        System.out.println("Unsorted Array: " + Arrays.toString(numbers));

        for (int i = 0; i < numbers.length; i++)
            for (int j = 0; j < (numbers.length - 1 - i); j++)
                if (numbers[j] > numbers[j + 1]) {
                    int current = numbers[j];
                    numbers[j] = numbers[j + 1];
                    numbers[j + 1] = current;
                }


        System.out.println("Sorted Array: " + Arrays.toString(numbers));


        // more efficient bubble sort
        int[] numbers2 = {7, 4, 2, 18, -3, 45, 54, 23, 66, -109};
        System.out.println("\n---More efficient bubble sort---");
        System.out.println("Unsorted Array: " + Arrays.toString(numbers2));

        for (int i = 0; i < numbers2.length; i++) {
            boolean hasSwapped = false;
            for (int j = 0; j < (numbers2.length - 1 - i); j++) {
                if (numbers2[j] > numbers2[j + 1]) {
                    int current = numbers2[j];
                    numbers2[j] = numbers2[j + 1];
                    numbers2[j + 1] = current;
                    hasSwapped = true;
                }
            }
            if (!hasSwapped)
                break;
        }

        System.out.println("Sorted Array: " + Arrays.toString(numbers2));

    }
}

// static meaning - static methods can only be called inside other static methods.
