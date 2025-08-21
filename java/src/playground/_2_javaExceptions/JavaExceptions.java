/* Description: Test how to throw simple exceptions in java
 * Author: Francis O'Hara
 * Date: 02-24-2024
 * */

package practice._2_javaExceptions;

public class JavaExceptions {
    public static void main (String[] args) {
        // print hello
        System.out.println("Hello World!");

        // throw a simple exception
        try {
            throw new Exception("This is the string message associated with the Exception!");
        }
        catch (Exception e) {
            System.out.println(e);
        }

        // print goodbye
        System.out.println("Goodbye World!"); // ideally shouldn't run due to exception.
    }
}
