package programming_with_java._1_javafundamentals.assignment1.question2.javaloops1;

import java.io.*;

public class JavaLoops1 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        bufferedReader.close();

        for (int i = 1; i <= 10; i++)
            System.out.println(N + " x " + i + " = " + N * i);

    }
}