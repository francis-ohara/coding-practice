/*
File Name:   usingVariablesBeforeAssignment.java
Author:      Francis O'Hara
Date:        3/05/2024
Description: Testing how variables behave when declared without assigning a value in Java.
How to Run:  java -ea usingVariablesBeforeAssignment
*/
package practice._4_usingVariablesBeforeAssignment;

public class UsingVariablesBeforeAssignment {
    public static void main(String[] args){
        // declare int and String variables
        int var1;
        String var2;

        // print variables without assignment
//        System.out.println(var1);
//        System.out.println(var2);

        // RESULTS
        /* build fails: variable might not have been initialized.
           Fails to compile but JShell console outputs `0` for integer and `null` for float.
        */


    }
}
