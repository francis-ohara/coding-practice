package _2_problemsolving.linearsearch2;

import java.util.Scanner;
import java.util.Arrays;

public class LinearSearch2 {
    public static void main(String[] args) {
        //2. Linear search
        // complexity - n
        Scanner input = new Scanner(System.in);
        int[] numbers = {2, 3, 1, 5, 6, 7, 8, 4, 10, 9};
        int target;
        int position = -1;

        System.out.println("Array :" + Arrays.toString(numbers));

        System.out.println("Enter target number:");
        target = input.nextInt();

        for (int i = 0; i < numbers.length; i++) {
            if (target == numbers[i]) {
                position = i;
                break;
            }
        }

        if (position != -1)
            System.out.printf("Target found at index %d.\n", position);
        else
            System.out.println("Target not found.");
    }
}