/*
File Name:   _19_JavaStringTokens.java
Author:      Francis O'Hara
Date:        2/3/25
Description: https://www.hackerrank.com/challenges/java-string-tokens/problem?isFullScreen=true
How to Run: java _19_JavaStringTokens
*/
package hackerrank;

import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;

public class _19_JavaStringTokens {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        s.trim();

        String[] tokens = s.split("[^A-Za-z]+");

        List<String> final_tokens = new ArrayList<>();

        for (String token: tokens){
            if (!token.isEmpty()){
                final_tokens.add(token);
            }
        }

        System.out.println(final_tokens.size());

        for (String token: final_tokens){
            System.out.println(token);
        }
    }
}
