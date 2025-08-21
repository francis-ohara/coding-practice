/*
File Name:   HashedStructures.java
Author:      Francis O'Hara
Date:        4/20/24
Description: Exploration of how to implement a hashed data structure.
How to Run:  java HashedStructures
*/
package practice._9_hashed_structures;

public class HashedStructures {
    public static void main(String[] args){
        // declare variables of different types
        int num = 3;
        Integer num1 = 5;
        String str = "Hello";

        // test hashCode() method for each variable
        // System.out.println(num.hashCode()); // Doesn't work for primitive types.
        System.out.println("Value: \"Hello\"\tHashcode: " + str.hashCode());
        System.out.println("Value: 5\tHashCode: " + num1.hashCode());


        // testing whether the modulo operator can return negative values
        int result1 = 37 % 7;     // ==> 2
        int result2 = 7 % 37;     // ==> 7
        int result3 = (-37) % 7;  // ==> ??
        int result4 = (-7) % 37;  // ==> ??

        System.out.println("37 % 7 = " + result1);
        System.out.println("7 % 37 = " + result2);
        System.out.println("-37 % 7 = " + result3);
        System.out.println("-7 % 37 = " + result4);
    }
}

/* CONCLUSIONS
    1. For integer values, the hashcode is likely the integer value itself.
    2. Primitive types only have hashCode(), or any method for that matter, only when declared with their corresponding wrapper classes.
       hashCode() is likely one of the public methods of the Object class, so it can't be called on non-objects.
    3. The modulo operator can evaluate to a negative value if its first operand (the dividend) is also negative.
    4. The hashCode() method can return a negative result for extremely large hash values.
       hashCode() values are ordinarily supposed to be of type INT(32-bit) so if the resulting hash value exceeds the largest possible
       value that can be represented with an integer, the value will overflow into the negatives and give you a negative result.
       As a result, it is advised to use the absolute value of the result when working with the hashCode() method.
* */