class Solution:
    def missingNum(self, arr):
        # code here
        	# Code here
	    n = len(arr) + 1
        ttl = sum(arr)
        exp = n * (n + 1) // 2
        return exp - ttl



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends