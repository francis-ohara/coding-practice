// Link: https://www.hackerrank.com/challenges/java-end-of-file/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _9_JavaEndOfFile {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int lineNumber = 1;

        while (scanner.hasNext()){
            System.out.println(lineNumber + " " + scanner.nextLine());
            lineNumber ++;
        }
    }
}
