// User function Template for Java
import java.util.*;
class Solution {
    static int majorityElement(int arr[]) {
        // code here
        HashMap<Integer,Integer>map=new HashMap<>();
        int n=arr.length;
        for(int i:arr){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        for(int key:arr){
            if(map.get(key)>n/2){
                return key;
            }
        }
        return -1;
        
    }
}