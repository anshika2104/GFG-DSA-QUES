class Solution:
	def minJumps(self, arr):
	    n=len(arr)
	    maxi,j,c=0,0,0
	    for i in range(n-1):
	        maxi=max(maxi,arr[i]+i)
	        if i==c:
	            c=maxi
	            j+=1
	    if c>=n-1:
	        return j
	    return -1
	    # code here
	   # j=0
	   # n=len(arr)
	   # if arr[0]==0:
	   #    return -1
	   # i = 0
    #     j = 0  # number of jumps

    #     while i < n - 1:
    #         if arr[i] == 0:
    #             return -1
    #         i += arr[i]
    #         j += 1

    #         if i >= n - 1:
    #             return j
        
    #     return j
	        