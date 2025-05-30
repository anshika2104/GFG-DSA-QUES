class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    public void sort012(int[] arr) {
        // code here
        int l=0,mid=0,h=arr.length-1;
        while(mid<=h){
            switch(arr[mid]){
                case 0:
                    int t=arr[l];
                    arr[l]=arr[mid];
                    arr[mid]=t;
                    l++;
                    mid++;
                    break;
                case 1:
                    mid++;
                    break;
                case 2:
                    int t2=arr[mid];
                    arr[mid]=arr[h];
                    arr[h]=t2;
                    h--;
                    break;
            }
        }
    }
}