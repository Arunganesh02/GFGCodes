//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int traverse( int n , vector<int> &price , vector<int> &dp){
        if (n<=0 ) return dp[n] = 0;
        int maxi = 0;
        int ans;
        if (dp[n] != -1) return dp[n];
        for (int i = 1 ; i<=n ; i++){
            ans = price[i-1] + traverse(n-i , price , dp);
            maxi = max(maxi , ans);
            
        }
        return dp[n] = maxi;
    }
    int cutRod(vector<int> &price) {
        // code here
        vector<int> dp(price.size()+1 , -1);
        return traverse(price.size() , price , dp);
        
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        vector<int> a;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            a.push_back(number);
        }

        Solution ob;

        cout << ob.cutRod(a) << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends