package _2_problemsolving.binarysearch2;

import java.util.Scanner;
import java.util.Arrays;

public class BinarySearch2 {

    public static void main(String[] args) {
        // 1. Binary search - Query an array; ask user for target; give position of target or -1;
        // complexity - O(logN)

        int[] numbers = {3, 4, 5, 69, 42, 35, 67, 66, 87, 10};

        System.out.println("Unsorted Array: " + Arrays.toString(numbers));
        Arrays.sort(numbers);
        System.out.println("Sorted Array: " + Arrays.toString(numbers));

        int position = -1;
        int start = 0;
        int end = numbers.length - 1;
        int middle;
        int target;

        Scanner input = new Scanner(System.in);
        System.out.println("Enter target number:");
        target = input.nextInt();

        while (start <= end) {
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
            System.out.printf("Target found at index %d.\n", position);
        else
            System.out.println("Target not found.");
    }
}