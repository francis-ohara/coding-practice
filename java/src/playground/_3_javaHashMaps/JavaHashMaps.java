/* Description: Test how to use HashMaps in Java.
 * Author: Francis O'Hara
 * Date: 2/24/2024
 */
package practice._3_javaHashMaps;

import java.util.HashMap;

public class JavaHashMaps {
    public static void main(String[] args){
        // instantiate hash map
        HashMap<Integer, String> map = new HashMap<>();

        // add key-value pairs to hash map
        map.put(1, "Hydrogen");
        map.put(2, "Helium");
        map.put(3, "Lithium");

        // print size of hash map
        System.out.println(map.size());

        // get individual values from hash map
        System.out.println(map.get(1)); // --> Hydrogen
        System.out.println(map.get(3)); // --> Lithium

        // print entire hash map
        System.out.println(map);

        // print all keys in hash map
        System.out.println(map.keySet());

        // print all values in hash map
        System.out.println(map.values());

        // overwrite values for existing keys
        System.out.println("Before: " + map.get(3));
        map.replace(3, "Silicon");
        System.out.println("After: " + map.get(3));

        // remove key-value pair from hash map
        System.out.println("Before: " + map);
        map.remove(3);
        System.out.println("After: " + map);
    }
}
