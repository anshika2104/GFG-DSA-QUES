#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        # bruteforce approach
        # n=len(arr)
        # for i in range(n):
        #     c=0
        #     for j in range(i,n):
        #         c+=arr[j]
        #         if c==target:
        #             return[i+1,j+1]
        # return [-1]
        i=0
        cs=0
        for j in range(len(arr)):
            cs+=arr[j]
            while cs>target and i<j:
                cs-=arr[i]
                i+=1
            if cs==target:
                return[i+1,j+1]
        return [-1]
        