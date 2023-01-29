/*
A detector compares the size of parts produced by a machine with the reference standard.

If the size of the part is larger, it can be sent to be fixed, and the detector prints the number 1.
If the size of the part is smaller, it is removed as a reject, and the detector prints the number -1.
If the part is perfect, it is sent to the box with products, that are ready to ship, and the detector prints 0.

Write a program, which takes the number of parts n as input, and then the sequence of detector prints. The program should output numbers in a single line containing the number of parts ready to be shipped, the number of parts to be fixed, and the number of rejects.
*/

package JBA;
import java.util.Scanner;

public class _3_SizeOfParts {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int nFix = 0;
        int nReject = 0;
        int nShip = 0;

        for (int i = 0; i < n; i++) {
            int print = scanner.nextInt();
            if (print == 0)
                nShip ++;
            else if (print == 1)
                nFix ++;
            else
                nReject ++;
        }

        System.out.println(nShip + " " + nFix + " " + nReject);
    }
}
