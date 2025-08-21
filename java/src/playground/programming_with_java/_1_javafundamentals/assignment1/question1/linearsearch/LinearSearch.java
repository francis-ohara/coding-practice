package programming_with_java._1_javafundamentals.assignment1.question1.linearsearch;

import java.util.Scanner;

public class LinearSearch {
    public static void main(String[] args) {

        Integer[] arr = {1, 2, 3, 5, 23, 11, 14, 7, 16, 91};  // array to be searched
        Integer target;  // number to be searched for in arr.
        int position = -1;  // location of target in arr.

        // Get target from user
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number you want to search for in the array:\t");
        target = input.nextInt();
        input.close();

        // linear search arr for target
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(target)) {
                position = i;
                break;
            }
        }

        if (position == -1)
            System.out.println("Target was not found in the array!");
        else
            System.out.printf("Target found at position %d.", position);
    }

}