#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
        l = 1
        r = n
        while l<=r:
            mid = ((r-l)//2)+l
            k = math.floor(mid**2)
            if k == n:
                return mid
            elif k > n:
                r = mid -1
            else:
                l = mid+1
        
        return r
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends