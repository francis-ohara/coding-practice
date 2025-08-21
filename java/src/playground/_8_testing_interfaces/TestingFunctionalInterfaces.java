/*
File Name:   TestingFunctionalInterfaces.java
Author:      Francis O'Hara
Date:        3/26/24
Description: Tests the ExampleFunctionalInterface functional interface by using it in a lambda expression.
How to Run:  java TestingFunctionalInterfaces
*/
package practice._8_testing_interfaces;

public class TestingFunctionalInterfaces {
    public static void main(String[] args) {
        ExampleFunctionalInterface add = (ExampleFunctionalInterface) (a, b) -> a + b;
        System.out.println(add);

        /* CONCLUSIONS
        A FunctionalInterface is an interface that has only 1 abstract method not including methods that override the
        public methods of Java's Object class.
        Functional interfaces are used in lambda expressions. See above for example.
        */
    }
}
