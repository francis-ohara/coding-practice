/*
File Name:   BuiltInStacks.java
Author:      Francis O'Hara
Date:        5/4/24
Description: Testing how to use Java's builtin LinkedList class as a Stack.
How to Run:  java BuiltInStacks
*/
package practice._10_builtin_stacks;

import java.util.LinkedList;

public class BuiltInStacks {
    public static void main(String[] args){
        LinkedList<Integer> stack = new LinkedList<>();
        stack.push(4);
        stack.push(2);
        stack.push(42);
        System.out.println("Push result: " + stack);
        stack.pop();
        System.out.println("Pop result: " + stack);
        stack.pop();
        System.out.println("Pop result: " + stack);
    }
}

/* CONCLUSIONS
    1. The built-in LinkedList class in Java implements a Stack through the peek(), pop(), and push() methods.
    2. The head of the LinkedList serves as the top of the stack on which new items are added, and from which items are removed.
* */
