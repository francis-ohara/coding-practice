//Demonstrates how to use the String.split() and Integer.parseInt methods to extract integers from a string of delimited integers.

package JBA;

public class _0_ParsingStringOfIntegers {
    public static void main(String[] args){

        String string = "17 18 999"; // String of space-delimited integers

        String[] strings = string.split("\s"); // Splits string according to whitespace

        Integer[] input = new Integer[strings.length]; // Initializing array to store integer equivalent of values in strings array above.

        for (int i = 0; i < strings.length; i++)
            input[i] = Integer.parseInt(strings[i]); // Converts each string in strings into integer equivalent.

        for (Integer number: input) System.out.println(number); // output result

    }
}