class Solution {
    public int getSecondLargest(int[] arr) {
        // code here
        int n=arr.length;
        int l=-1;
        int sl=-1;
        for(int i=0;i<n;i++){
            if(arr[i]>l){
                sl=l;
                l=arr[i];
            }
            else if(l>arr[i]&&arr[i]>sl){
                sl=arr[i];
            }
            
        }
        return sl;
    }
}