/*
File Name:   InstanceOf.java
Author:      Francis O'Hara
Date:        3/05/2024
Description: Test how to use the instanceof operator in Java. Specifically, can it help differentiate initialized
             variables from uninitialized or does it simply check that the type of the variable matches a specific
             class but not the reference stored in the variable.
How to Run:  java -ea InstanceOf
*/
package practice._7_instanceOf;

public class InstanceOf {
    public static void main(String[] args){
        Integer integer;

        // assert integer instanceof Integer;

        /* RESULTS
         * `instanceof` can't be used to check for null vs non-null variables. The only thing you can do with null variables
         * is use the inequality operators to compare them with the `null` literal.
         *
         * This is the most appropriate way to check if a variable is null.
         *
         * `instanceof` is mostly useful for determining if only the superclass of an object is known, and one wants to know
         * the specific subclass of the superclass that the object is an instance of.
        * */
    }
}
