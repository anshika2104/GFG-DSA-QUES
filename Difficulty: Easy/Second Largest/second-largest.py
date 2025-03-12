#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # for i in range(len(arr)-2,-1):
        #     if arr[i]!=lar:
        #         sec=arr[i]
        #         # break
        # return arr[i]
        l=float('-inf')
        sl=float('-inf')
        
        for i in arr:
            if i>l:
                sl=l
                l=i
            elif i>sl and i!=l:
                sl=i
            
            
            # return sl
        if sl!=float("-inf"):
            return sl
        else:
            return -1





#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends