package hackerrank;
import java.util.List;
import java.util.ArrayList;
public class _28_SherlockAndArray {

    public static void main(String[] args){
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(5);
        numbers.add(1);
        System.out.println(balancedSums(numbers));
    }
    public static String balancedSums(List<Integer> arr){
        for (int i = 0; i < arr.size(); i ++){
            int leftArraySum = 0;
            int rightArraySum = 0;
            for (int j = 0; j < i; j++)
                leftArraySum += arr.get(j);
            for (int k = i + 1; k < arr.size(); k ++)
                rightArraySum += arr.get(k);

            if (leftArraySum == rightArraySum)
                return "YES";
        }
        return "NO";
    }
}
