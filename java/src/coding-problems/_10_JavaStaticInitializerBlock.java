// Link: https://www.hackerrank.com/challenges/java-static-initializer-block/problem?isFullScreen=true

package hackerrank;

import java.util.Scanner;

public class _10_JavaStaticInitializerBlock {
    private static int B;
    private static int H;
    private static boolean flag = false;

    static {
        Scanner scanner = new Scanner(System.in);
        B = scanner.nextInt();
        H = scanner.nextInt();
        if (B < 1 || H < 1){
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else
            flag = true;
    }
    public static void main(String[] args){
        if(flag){
            int area=B*H;
            System.out.print(area);
        }
    }
}
