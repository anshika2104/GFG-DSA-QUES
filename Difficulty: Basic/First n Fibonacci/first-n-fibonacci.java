// User function Template for Java

class Solution {
    // Function to return list containing first n fibonacci numbers.
    public static int[] fibonacciNumbers(int n) {
        // Your code herefib
        int[]fib=new int[n];
        if(n>=1){
        fib[0]=0;
        }
        if(n>=2){
            fib[1]=1;
        }
        for(int i=2;i<n;i++){
            fib[i]=fib[i-1]+fib[i-2];
        }
        return fib;
        
        // if(n<=1){
        //     return n;
        // }
        //  return fibonacciNumbers(n - 1) + fibonacciNumbers(n - 2);
    }
}