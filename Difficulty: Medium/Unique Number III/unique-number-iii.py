#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        f={}
        for i in arr:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for keys,values in f.items():
            if values==1:
                return keys


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends