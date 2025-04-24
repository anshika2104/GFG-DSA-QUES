#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
		f={}
		l=[]
        for i in arr:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for key,values in f.items():
            if values==1:
                l.append(key)
                l.sort()
        return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends