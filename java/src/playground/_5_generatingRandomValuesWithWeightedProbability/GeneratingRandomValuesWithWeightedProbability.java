/*
File Name:   GeneratingRandomValuesWithWeightedProbability.java
Author:      Francis O'Hara
Date:        3/05/2024
Description: Test how to generate random values such that some outcomes are more likely than others.
             The goal is to generate 100 bits with a 70 % chance of each bit being a 1.
How to Run:  java -ea GeneratingRandomValuesWithWeightedProbability
*/
package practice._5_generatingRandomValuesWithWeightedProbability;

import java.util.Random;
import java.util.ArrayList;

public class GeneratingRandomValuesWithWeightedProbability {
    /**
     * The main entry point into the program.
     * @param args Array of Strings denoting the command-line arguments passed to the program.
     */
    public static void main(String[] args) {
        ArrayList<Integer> outcomes = new ArrayList<>();  // integer array of 0s and 1s for storing outcomes
        int countOfZeros = 0;  // number of 0-bit outcomes
        int countOfOnes = 0;  // number of 1-bit outcomes

        // add 100 bits to outcomes array with 70% chance of adding a 1 bit.
        Random random = new Random();
        for (int i = 0; i < 100; i++) {
            if (random.nextInt(1, 11) <= 7) {
                outcomes.add(1);
                countOfOnes++;
            } else {
                outcomes.add(0);
                countOfZeros++;
            }
        }

        System.out.println("Outcomes: " + outcomes);
        System.out.println("Number Of 0s: " + countOfZeros);  // should be close to 30
        System.out.println("Number Of 1s: " + countOfOnes);  // should be close to 70
    }
}
