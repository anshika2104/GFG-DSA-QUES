class Solution:
    def findUnique(self, arr):
        # code here 
        # arr.sort()
        # c=0
        # for i in range(len(arr)-1):
        #     if arr[i]==arr[i+1]:
        #         c+=1
        #     else:
        #         c=1
        # if c==1:
        #     return arr[i]
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
        ans = ob.findUnique(arr)
        print(ans)
        print("~")
# } Driver Code Ends