/*
File Name:   GeneratingRandomDoubles.java
Author:      Francis O'Hara
Date:        3/05/2024
Description: Test how to generate random doubles with the Random class.
How to Run:  java -ea GeneratingRandomDoubles
*/
package practice._6_generatingRandomDoubles;

import java.util.Random;
public class GeneratingRandomDoubles {
    /**
     * The main entry point into the program.
     * @param args An array of Strings denoting the command-line arguments passed to the program.
     */
    public static void main(String[] args){
        // Goal: generate random double between 0 and 1 using a Random object.
        Random random = new Random();
        double randomDouble = random.nextDouble(0.0, 1.0);

        System.out.println("The generated Number: " + randomDouble);
    }
}
