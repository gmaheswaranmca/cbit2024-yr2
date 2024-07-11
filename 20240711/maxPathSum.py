# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_path_sum = float('-inf') #init with least value
#1. to find the path sum of given node, 2. to update the path_sum as max_path_sum if so
def find_path_sum(node): # read / write # we have three tasks | violated Single Responsibility Principle
    global max_path_sum 
    if not node:
        return 0
    #calc max path sum with left child
    left_max = max(find_path_sum(node.left),0)
    #calc max path sum with right child 
    right_max = max(find_path_sum(node.right),0)

    #left tree max path + node + right tree max path #2 longest path max sum includes the node  
    node_path_sum = left_max + node.val + right_max

    #check node_path_sum with global max_path_sum and update it if max
    if node_path_sum > max_path_sum: #3
        max_path_sum = node_path_sum

    #return node-to-leaf max path #1
    return node.val + max(left_max, right_max) 

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = find_path_sum(root)        
        return max_path_sum