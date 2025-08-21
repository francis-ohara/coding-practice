package programming_with_java._1_javafundamentals.assignment1.question1.mergesort;

import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] numbers = {-3, 4, 56, -6, -7, 42, 18, 61, 9, 23, 14, 42};

        System.out.println("Unsorted Array: " + Arrays.toString(numbers));

        System.out.println("----Sorting----");
        mergeSort(numbers, numbers.length);

        System.out.println("Sorted Array: " + Arrays.toString(numbers));

    }

    static void mergeSort(int[] array, int n) {
        if (n < 2) {
            return;
        }
        int middle = n / 2;
        int[] left = new int[middle];
        int[] right = new int[n - middle];

        for (int i = 0; i < middle; i++) {
            left[i] = array[i];
        }
        for (int i = middle; i < n; i++) {
            right[i - middle] = array[i];
        }
        mergeSort(left, middle);
        mergeSort(right, n - middle);

        merge(array, left, right, middle, n - middle);
    }

    static void merge(
            int[] a, int[] l, int[] r, int left, int right) {

        int i = 0, j = 0, k = 0;
        while (i < left && j < right) {
            if (l[i] <= r[j]) {
                a[k++] = l[i++];
            } else {
                a[k++] = r[j++];
            }
        }
        while (i < left) {
            a[k++] = l[i++];
        }
        while (j < right) {
            a[k++] = r[j++];
        }
    }
}