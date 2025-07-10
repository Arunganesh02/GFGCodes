#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        
        def traverse(i , j , isTrue):
            nonlocal s
            if i > j : return 0
            if i == j : 
                if isTrue == 1: 
                    if s[i]=="T":
                        return 1
                    else: return 0
                else:
                    if s[i] == "F": return 1
                    else: return 0
            if dp[i][j][isTrue] != -1 : return dp[i][j][isTrue]
            
            count = 0
            for k in range(i+1 , j , 2):
                tl = traverse(i , k-1 ,1)
                tr = traverse(k+1 , j , 1)
                fl = traverse(i , k-1 , 0)
                fr = traverse(k+1 , j , 0)
                if s[k] == "&":
                    # print("hdd")
                    if (isTrue == 1):
                        count += tl * tr
                    else:
                        count += (tl*fr) + (tr * fl) + (fr * fl)
                elif s[k] == "|":
                    # print("hdd")
                    if (isTrue == 1):
                        count += (tl * fr) + (tr * fl) +(tl * tr)
                    else:
                        count += fl * fr
                elif s[k] == "^":
                    # print("hdd")
                    if (isTrue == 1):
                        count +=  (tl * fr) + (fl * tr)
                        
                    else:
                        count += (tl * tr) + (fl * fr)
            dp[i][j][isTrue] = count
            return count
        dp = [[[-1 for i in range(2)] for j in range(len(s))] for k in range(len(s))]
        return traverse(0 , len(s)-1 , 1)