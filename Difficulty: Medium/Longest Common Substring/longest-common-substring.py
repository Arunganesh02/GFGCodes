#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        text1 = s1
        text2 = s2
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(1 , len(text1)+1):
            for j in range(1 , len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
        ma = float('-inf')
        for i in range(len(dp)):
            ma = max(ma , max(dp[i]))
        return ma