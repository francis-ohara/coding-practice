/*
Write a program that reads an array of ints and outputs the maximum product of two adjacent elements in the given array of non-negative numbers.

Input data format

The first line of the input contains the number of elements in the array.

The second line contains the elements of the array separated by spaces.

The array always has at least two elements.*/

package JBA;
import java.util.Scanner;

public class _1_MaxProduct {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt(); // no. of elements
        Integer[] numbers = new Integer[n]; //array of elements
        int maxProduct = 0;  // maximum product

        for (int i = 0; i < n; i++)
            numbers[i] = input.nextInt();

        for (int i = 0; i < n-1; i++){
            int product = numbers[i] * numbers[i+1];
            maxProduct = Math.max(product, maxProduct);
        }

        System.out.println("The Maximum Product is: " + maxProduct);
    }
}
