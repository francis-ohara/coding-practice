/*
File Name:   _21_JavaRegex.java
Author:      Francis O'Hara
Date:        2/6/25
Description: https://www.hackerrank.com/challenges/java-regex/problem?isFullScreen=true
How to Run:  java _21_JavaRegex
*/

package hackerrank;

import java.util.Scanner;
import java.util.regex.Pattern;

public class _21_JavaRegex {
    private static class MyRegex{
        String pattern = "(([0-1]{0,1}[0-9]{0,1}[0-9])|(2(([0-4][0-9])|(5[0-5]))))\\.(([0-1]{0,1}[0-9]{0,1}[0-9])|(2(([0-4][0-9])|(5[0-5]))))\\.(([0-1]{0,1}[0-9]{0,1}[0-9])|(2(([0-4][0-9])|(5[0-5]))))\\.(([0-1]{0,1}[0-9]{0,1}[0-9])|(2(([0-4][0-9])|(5[0-5]))))";
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()){
            String s = scanner.next();
            System.out.println(Pattern.matches(new MyRegex().pattern, s));
        }

    }
}
