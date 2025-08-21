/*
File Name:   _24_TagContentExtractor.java
Author:      Francis O'Hara
Date:        2/13/25
Description: https://www.hackerrank.com/challenges/tag-content-extractor/problem?isFullScreen=true
How to Run:  java _24_TagContentExtractor
*/
package hackerrank;

import java.util.Scanner;
import java.util.regex.Pattern;
public class _24_TagContentExtractor {
    public static void main(String[] args){
        String regex = "<[A-Za-z]]";
        Pattern pattern = Pattern.compile(regex);
        pattern.matcher("dfdf").group();
    }
}
