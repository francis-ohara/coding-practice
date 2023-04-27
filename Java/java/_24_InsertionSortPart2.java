package hackerrank;

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class _24_Result {

    /*
     * Complete the 'insertionSort2' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void arrPrint(List<Integer> arr){
        for (int value: arr) System.out.print(value + " ");
    }

    public static void insertionSort2(int n, List<Integer> arr){
        for (int i = 1; i < n; i ++){
            int target = arr.get(i);
            for (int j = i; j >= 0; j--){
                if (j==0){
                    arr.set(j, target);
                    arrPrint(arr);
                    System.out.println();
                }
                else if (arr.get(j-1) < target){
                    arr.set(j, target);
                    arrPrint(arr);
                    System.out.println();
                    break;
                }
                else
                    arr.set(j, arr.get(j-1));

            }
        }
    }

}

public class _24_InsertionSortPart2 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        _24_Result.insertionSort2(n, arr);

        bufferedReader.close();
    }
}
