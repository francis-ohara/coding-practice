package practice;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
    public static void main(String[] args) {
        /*String regex = "^Chapter";
        String haystack = "Chapter 1 is not the very first chapter here. 99 times have I tried!";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher =  pattern.matcher(haystack);
        System.out.println(matcher.matches());*/
        System.out.println("Hello world");

    }
    public static int[] twoSum(int[] nums, int target) {
        int[] output = new int[2];
        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1; j < nums.length; j++){
                if (nums[i] + nums[j] == target) {
                    output[0] = i;
                    output[1] = j;
                    break;
                }
            }
        }
        return output;
    }
}