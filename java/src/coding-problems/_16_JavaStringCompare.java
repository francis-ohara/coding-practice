// Link: https://www.hackerrank.com/challenges/java-string-compare/problem?isFullScreen=false

package hackerrank;


public class _16_JavaStringCompare {
    public static void main(String[] args){
        System.out.println(getSmallestAndLargest("ASDFHDSFHsdlfhsdlfLDFHSDLFHsdlfhsdlhkfsdlfLHDFLSDKFHsdfhsdlkfhsdlfhsLFDLSFHSDLFHsdkfhsdkfhsdkfhsdfhsdfjeaDFHSDLFHDFlajfsdlfhsdlfhDSLFHSDLFHdlfhs", 144));
    }

    public static String getSmallestAndLargest(String s, int k){
        String smallest = s.substring(0, k);
        String biggest = smallest;

        for (int i = 0; i < s.length() - k + 1; i++){
            String substring = s.substring(i, i + k);
            if (lexicographicallyGreaterThan(substring, biggest)){
                biggest = substring;
            }
            if (lexicographicallyLessThan(substring, smallest)) {
                smallest = substring;
            }
        }
        return smallest + "\n" + biggest;
    }

    private static boolean lexicographicallyGreaterThan(String a, String b){
        for (int i = 0; i < Math.min(a.length(), b.length()); i ++ ){
            if (a.charAt(i) > b.charAt(i)){
                return true;
            }
            else if (a.charAt(i) < b.charAt(i)){
                return false;
            }
        }
        return false;
    }

    private static boolean lexicographicallyLessThan(String a, String b){
        for (int i = 0; i < Math.min(a.length(), b.length()); i ++ ){
            if (a.charAt(i) < b.charAt(i)){
                return true;
            }
            else if (a.charAt(i) > b.charAt(i)){
                return false;
            }
        }
        return false;
    }
}