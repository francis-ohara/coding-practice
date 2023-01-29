/*
Harry Potter needs help identifying what each house means.

Read a string representing a house and output the following:

* if it is "gryffindor", output "bravery";
* if it is "hufflepuff", output "loyalty";
* if it is "slytherin", output "cunning";
* if it is "ravenclaw", output "intellect";
* otherwise, output "not a valid house".

The problem was taken from the course Introduction to JavaScript and React by Ken McGrady and adapted for our educational platform.

*/
package JBA;
import java.util.HashMap;
import java.util.Scanner;


public class _2_HarryPotter {
    public static void main(String[] args) {
        // mapping of houses to meanings
        HashMap<String, String> houses = new HashMap<>();
        houses.put("gryffindor", "bravery");
        houses.put("hufflepuff", "loyalty");
        houses.put("slytherin", "cunning");
        houses.put("ravenclaw", "intellect");

        Scanner input = new Scanner(System.in);
        String query = input.next(); // house whose meaning is to be searched.

        String answer = houses.getOrDefault(query, "not a valid house"); // meaning if house in mappings, "not a valid house" otherwise.
        System.out.println(answer);
    }
}
