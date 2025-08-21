package programming_with_java._1_javafundamentals.assignment1.question1.binarysearch;

import java.util.Arrays;
import java.util.Scanner;

public class BinarySearch {
    public static void main(String[] Args) {
        int[] numbers = {64, -3, 2, 0, 48, 26, -13, 98, 54, 77};
        int position = -1;
        int start = 0;
        int end = numbers.length - 1;
        int middle;
        int target;

        System.out.println("Unsorted Array: " + Arrays.toString(numbers));
        System.out.println("----Sorting----");
        Arrays.sort(numbers);
        System.out.println("Sorted Array: " + Arrays.toString(numbers));

        Scanner input = new Scanner(System.in);
        System.out.println("Enter target number:");
        target = input.nextInt();
        input.close();

        while (start < end) {
            middle = (start + end) / 2;
            if (target == numbers[middle]) {
                position = middle;
                break;
            } else if (target > numbers[middle])
                start = middle + 1;
            else
                end = middle - 1;
        }

        if (position != -1)
            System.out.println("Target found at position " + position);
        else
            System.out.println("Target not found.");
    }
}

