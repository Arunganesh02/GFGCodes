
from typing import List


class Solution:
    def countPartitions(self, arr, d):
        # code here
        def traverse(indi , tar):

            if indi == 0 :
                if tar == 0 and arr[0] == 0 : return 2
                if tar == 0 or tar - arr[indi] == 0 : return 1
                return 0
            # print(indi , tar)
            # if tar == 0 : return 1
            if dp[indi][tar] != -1 : return dp[indi][tar]
            take = 0
            nottake = traverse(indi -1 , tar)
            if arr[indi] <= tar:
                take = traverse(indi-1 , tar - arr[indi])

            dp[indi][tar] = take+nottake
            return take + nottake
        
        su = sum(arr)

        if (su - d < 0  or (su-d)%2 == 1): return 0
        dp = [[-1 for i in range(((su-d)//2)+1)] for j in range(len(arr))]
        return  traverse(len(arr)-1 , (su-d)//2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countPartitions(A, D)
        print(ans)
        print("~")

# } Driver Code Ends