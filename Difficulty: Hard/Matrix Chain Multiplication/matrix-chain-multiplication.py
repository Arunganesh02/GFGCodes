class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        def traverse(i , j):
            nonlocal arr , dp
            if i== j :
                return 0
            if dp[i][j] != -1 : return dp[i][j]
            mini = float('inf')
            for k in range(i , j):
                ops = (arr[i-1] * arr[k] * arr[j]) + traverse(i , k) + traverse(k+1 ,j)
                mini = min(mini , ops)
            dp[i][j] = mini
            return mini
        
        dp = [[-1 for i in range(len(arr))] for j in range(len(arr))]
        return traverse(1 , len(arr)-1)
            
        