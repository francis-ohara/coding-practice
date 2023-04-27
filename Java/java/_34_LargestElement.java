/*
* Given a sequence of positive integer numbers (which ends with the number 0). Find the largest element of the sequence.
* The number 0 itself is included in the sequence but serves only as a sign of the sequence's end.
*/

package JBA;
import java.util.Scanner;

public class _4_LargestElement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int largest = 0;

        while (true) {
            int number = scanner.nextInt();
            if (number > 0)
                largest = Math.max(number, largest);
            else
                break;
        }
        System.out.println("Largest: " + largest);
    }
}
