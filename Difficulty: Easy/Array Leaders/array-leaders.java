import java.util.*;

class Solution {
    public ArrayList<Integer> leaders(int[] arr) {
        ArrayList<Integer> result = new ArrayList<>();
        int n = arr.length;
        int maxFromRight = Integer.MIN_VALUE;

        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] >= maxFromRight) {
                maxFromRight = arr[i];
                result.add(maxFromRight);
            }
        }

        // Reverse the result to maintain original left-to-right order
        Collections.reverse(result);
        return result;
    }
}
