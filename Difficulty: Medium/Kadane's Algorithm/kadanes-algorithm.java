class Solution {
    int maxSubarraySum(int[] arr) {
        // Your code here
        int ms=arr[0];
        int me=arr[0];
        for(int i=1;i<arr.length;i++){
            me=Math.max(me+arr[i],arr[i]);
            ms=Math.max(me,ms);
        }
        return ms;
    }
}
