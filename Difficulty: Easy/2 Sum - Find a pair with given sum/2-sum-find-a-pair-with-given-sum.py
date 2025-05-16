#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


# } Driver Code Ends

#User function Template for python3
class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        # # Your code here
        # for i in range(len(arr)):
        #     for j in range(i+1,len(arr)):
        #         if arr[i]+arr[j]==target:
        #             return [arr[i],arr[j]]
        # return []
        s={}
        for i in arr:
            c=target-i
            if c in s:
                return [c,i]
            s[i]=True
        return []

            


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        target = int(input())
        ob = Solution()
        res = ob.twoSum(A, target)
        if len(res) == 0:
            print('[]', end="")
        else:
            # sort the output before printing
            res.sort()
            for i in range(len(res)):
                print(res[i], end=" ")        
        print("")
        print('~')
        T -= 1

if __name__ == "__main__":
    main()

# } Driver Code Ends