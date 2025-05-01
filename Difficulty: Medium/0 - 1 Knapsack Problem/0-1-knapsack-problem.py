class Solution:
    def knapsack(self, W, val, wt):
        # code here
        def traverse(indi , weight):
            if indi == 0 : 
                if weight>= wt[0]: return val[indi]
                else: return 0
            if dp[indi][weight] != -1 : return dp[indi][weight]
            take = 0
            nottake = 0
            nottake = traverse(indi-1 , weight)
            if wt[indi] <= weight:
                take = val[indi] + traverse(indi-1  , weight - wt[indi])
            dp[indi][weight] = max(take,nottake)
            return max(take , nottake)
        dp = [[-1 for i in range(W+1)] for j in range(len(val))]
        return traverse(len(val)-1  , W)


#{ 
 # Driver Code Starts
test_cases = int(input())
for _ in range(test_cases):
    capacity = int(input())
    values = list(map(int, input().strip().split()))
    weights = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.knapsack(capacity, values, weights))
    print("~" )
# } Driver Code Ends