/*
File Name:   GettingSystemTime.java
Author:      Francis O'Hara
Date:        5/4/24
Description: Test how to obtain system time in Java for tracking how long it takes to execute program instructions.
How to Run:  java GettingSystemTime
*/
package practice._11_getting_system_time;

public class GettingSystemTime {
    public static void main(String[] args) throws Exception {
        long time1 = System.currentTimeMillis();
        Thread.sleep(500);
        long time2 = System.currentTimeMillis();
        System.out.println("Time 1 is " + time1 + " milliseconds.");
        System.out.println("Time 2 is " + time2 + " milliseconds.");
        System.out.println("Time elapsed is " + (time2 - time1) + " milliseconds.");
    }
}

/* CONCLUSIONS
 * 1. The `System.currentTimeMillis()` method can be used to obtain the current system time (unix time) in milliseconds.
 * 2. `System.currentTimeMillis()` returns a long, which means that different times can be subtracted from each other
 *    to obtain the time elapsed between each call to the method in milliseconds.
 */


