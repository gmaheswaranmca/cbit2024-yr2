# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, ar,low,high):
    if not root:
        return 
    inorder(root.left, ar,low,high)
    if root.val >= low and root.val <= high:
        ar.append(root.val)
    inorder(root.right,ar,low,high)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ar = []
        inorder(root,ar,low,high)
        return sum(ar)