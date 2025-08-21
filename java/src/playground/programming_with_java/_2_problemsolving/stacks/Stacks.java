package programming_with_java._2_problemsolving.stacks;


public class Stacks {
    public static void main(String[] args) {

/*
    Stacks (Brief intro to classes)
    --------------------------------
         * data members (c++) == fields ~== instance variables ~== properties
         * member functions (c++) == methods

         * every object inherits from the Object class which has methods toString, ...etc.

         * Stack operations(methods) - pop, push, peek

         * instantiation
           - creating an object from a class.

         * instantiation e.g.
            Stack stack = new Stack();
            Stack stack1 = new Stack(9);
            Stack stack2 = new Stack(9, new int[] {1,2,3,4,5,6,7,8,9});
*/
        // instantiate stack
        Stack stack = new Stack();
        Stack stack1 = new Stack(5);
        Stack stack2 = new Stack(10, new int[]{1, 2, 3, 4, 5, 6, 7});

        // peek
        System.out.println("Stack peek: " + stack.peek());  // Error 0
        System.out.println("Stack1 peek: " + stack1.peek());  // Error 0
        System.out.println("Stack2 peek: " + stack2.peek());  // 7

        // push
        stack.push(42);
        System.out.println("Stack peek: " + stack.peek());  // 42

        // pop
        stack2.pop();
        System.out.println("Stack2 peek: " + stack2.peek());  // 6
        stack2.pop();
        System.out.println("Stack2 peek: " + stack2.peek());  // 5
    }
}

class Stack {
/* PSEUDOCODE
 Stack
 ------
    * Properties
       - data
       - size
       - top - 1

    * Methods
       - constructors(w/ overloading)
       - push()
       - pop()
       - peek()

    *  Implementation
       - implement with Java Array of length `size`.
       - top property has default value of -1
       - stack is empty when top is -1
           - check if stack is not empty before pop()
           - check if stack is not empty before peek()
       - stack is full when top == size - 1
           - check if stack is not full before push()
*/

    // fields
    private int[] data;
    private int size;
    private int top = -1;

    // constructors
    public Stack() {
        size = 10;
        data = new int[10];
    }

    public Stack(int n) {
        size = n;
        data = new int[size];
    }

    public Stack(int size, int[] elements) {
        if (elements.length > size)
            System.out.println("Error! Number of elements can not be greater than size of the stack!");
        else {
            top = elements.length - 1;
            this.size = size;
            data = new int[size];
            for (int i = 0; i < elements.length; i++) {
                data[i] = elements[i];
            }

        }
    }

    // push
    public void push(int element) {
        if (top == size - 1)
            System.out.println("Error! Stack is full!");
        else {
            top = top + 1;
            data[top] = element;
        }
    }

    // peek
    public int peek() {
        if (top == -1) {
            System.out.println("Error! Stack is Empty!");
            return 0;
        } else
            return data[top];
    }

    // pop
    public int pop() {
        if (top == -1) {
            System.out.println("Error! Stack is Empty!");
            return 0;
        } else {
            int popped_element = data[top];
            top = top - 1;
            return popped_element;
        }
    }


}




