/*
File Name:   _20_PatternSyntaxChecker.java
Author:      Francis O'Hara
Date:        2/4/25
Description: https://www.hackerrank.com/challenges/pattern-syntax-checker/problem?isFullScreen=true
How to Run:  java _20_PatternSyntaxChecker
*/
package hackerrank;

import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class _20_PatternSyntaxChecker {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < n; i ++){
            String regex = scanner.nextLine();
            try{
                Pattern.compile(regex);
                System.out.println("Valid");
            }
            catch (PatternSyntaxException e){
                System.out.println("Invalid");
            }
        }
    }
}