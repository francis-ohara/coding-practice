/*
File Name:   TestingInterfaces.java
Author:      Francis O'Hara
Date:        3/26/2024
Description: Testing how interfaces can be instantiated.
How to Run:  java TestingInterfaces
*/
package practice._8_testing_interfaces;

public class TestingInterfaces {
    public static void main(String[] args){
        ExampleInterface instance1  = new ExampleInterface(){
            @Override
            public int add (int a, int b){
                return a + b;
            }

            @Override
            public int multiply (int a, int b){
                return a * b;
            }
        };

        // test the instance
        System.out.println(instance1.add(1, 2));  // 3
        System.out.println(instance1.multiply(3, 4));  // 12

        /* RESULTS
         * Interfaces are 100% abstract and cannot be instantiated.
         * There exists a syntax however for 'instantiating an interface' by simultaneously creating and instantiating a
         * nameless class that implements the interface and overrides all its abstract methods.
         * See above for an example.
         */

    }
}
