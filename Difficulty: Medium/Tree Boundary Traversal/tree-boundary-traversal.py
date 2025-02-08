#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def __init__(self):
        self.preord = []
        self.left = []
        self.right = []
    def preorder(self,root):
        if root:
            if not root.left and not root.right:
                self.preord.append(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def leftview(self, root):
        if root:
            self.left.append(root.data)
            if root.left:
                self.leftview(root.left)
            elif not root.left and root.right:
                self.leftview(root.right)
    def rightview(self , root):
        if root:
            self.right.append(root.data)
            if root.right:
                self.rightview(root.right)
            elif not root.right and root.left:
                self.rightview(root.left)
    def boundaryTraversal(self, root):
        # Code here\
        self.preorder(root)
        if not root.left and not root.right:
            return [root.data]
    
        self.leftview(root.left)
        self.rightview(root.right)
        
        if not root : return []
        ans = [root.data]
        leftview = self.left[:]
        rightview = self.right[:]
        leaf = self.preord[:]
        ans += leftview
        se = set(ans)
        # print(leftview , rightview , leaf)
        for i in leaf:
            if i not in se:
                ans.append(i)
                se.add(i)
        rightview.reverse()
        for i in rightview:
            if i not in se:
                ans.append(i)
                se.add(i)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        res = obj.boundaryTraversal(root)
        for i in res:
            print(i, end=" ")
        print('')
        print("~")

# } Driver Code Ends