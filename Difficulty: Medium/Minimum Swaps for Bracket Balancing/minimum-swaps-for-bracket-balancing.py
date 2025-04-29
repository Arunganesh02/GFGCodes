#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,s):
        # code here 
        st = []
        st.append(s[0])
        c = 0 
        for i in range(1,len(s)):
            if s[i] == ']':
                if len(st)!= 0 and st[-1] == '[':
                        st.pop()
                else:
                    st.append(s[i])
            else:
                if len(st) != 0 and st[-1] == ']':
                    c += len(st)
                    st.pop()
                else:
                    st.append(s[i])
        return c        
                
                
                
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
        print("~")

# } Driver Code Ends