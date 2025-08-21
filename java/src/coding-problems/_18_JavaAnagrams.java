/*
File Name:   _18_JavaAnagrams.java
Author:      Francis O'Hara
Date:        2/2/25
Description: https://www.hackerrank.com/challenges/java-anagrams/problem?isFullScreen=true
How to Run:  `java _18_JavaAnagrams`
*/
package hackerrank;

import java.util.Scanner;
public class _18_JavaAnagrams {
    static boolean isAnagram(String a, String b){
        a = a.toLowerCase();
        b = b.toLowerCase();
        for (int i = 0; i < a.length(); i ++){
            if (b.isEmpty())
                return false;
            for (int j = 0; j < b.length(); j++){
                if (a.charAt(i) == b.charAt(j)){
                    if (b.length() == 1){
                        b = "";
                    } else
                        b = b.substring(0, j) + b.substring(j+1);
                    break;
                }
            }
        }
        return b.isEmpty();
    }

    public static void main(String[] args){
        System.out.println(isAnagram("rose", "rose"));
    }
}
