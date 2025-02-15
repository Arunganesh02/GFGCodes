#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def __init__(self):
        self.ans = []
    def inorderSuccessor(self, root, x):
        # Code here
        # def successor(root):
        #     if root.left:
        #         # print(root.data)
        #         return successor(root.left)
        #     else:
        #         # print(root.data)
        #         return root.data
        # def traverse(root , k ,prev):
        #     if root:
        #         traverse(root.left , k , root)
        #         if root.data == k:
        #             if not root.right:
        #                 self.ans = prev.data
        #             else:
        #                 self.ans = successor(root.right)

        #         traverse(root.right , k , root)
        # traverse(root , k , root)
        # return self.ans
        def traverse(root):
            if root:
                traverse(root.left)
                self.ans.append(root.data)
                traverse(root.right)
        
        traverse(root)
        for i in range(len(self.ans)):
            if self.ans[i] == k:
                if i+1 < len(self.ans):
                    return self.ans[i+ 1]
                else:
                    return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        k = int(input())
        print(Solution().inorderSuccessor(root, Node(k)))
        print("~")

# } Driver Code Ends