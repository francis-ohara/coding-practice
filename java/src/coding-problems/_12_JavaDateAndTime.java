// Link: https://www.hackerrank.com/challenges/java-date-and-time/problem?isFullScreen=true

package hackerrank;

import java.util.Calendar;

public class _12_JavaDateAndTime {
    public static void main(String[] args){
        Calendar calendar = new Calendar.Builder().setDate(2020, 10, 25).build();
        System.out.println(findDay(1, 23, 2025));
    }

    public static String findDay(int month, int day, int year){
         String[] weekDayStrings = {"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
        Calendar calendar = new Calendar.Builder().setDate(year, month - 1, day).build();
        return weekDayStrings[calendar.get(Calendar.DAY_OF_WEEK) - 1];
    }
}
