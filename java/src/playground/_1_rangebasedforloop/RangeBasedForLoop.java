package practice._1_rangebasedforloop;

// how to write a range-based for loop in Java.
public class RangeBasedForLoop {
    public static void main(String[] args){

        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        for (int number: numbers){
            System.out.printf("%d ", number * 2);
        }
    }

}
