'''             0         5
    inorder =  [1,3,4,6,7,8,10,13,14]
    preorder = [8,3,1,6,4,7,10,14,13]

                8
               / \
              3  10     
    inorder = [1,3,4,6,7]               [10,13,14]
    preorder = [3,1,6,4,7]              [10,14,13]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (not preorder) or (not inorder):
            return None
        val = preorder[0]
        root = TreeNode(val)

        val_index = inorder.index(val)
        #get the preorder list and inorder list of the left tree
        preorder_left = preorder[1:val_index+1] # 1..till val_index
        inorder_left = inorder[:val_index] # 0..bef val_index
        root.left = self.buildTree(preorder_left, inorder_left)
        #get the preorder list and inorder list of the right tree
        preorder_right = preorder[val_index+1:] # val_index+1 till end of list
        inorder_right = inorder[val_index+1:] # val_index+1 till end of list
        root.right = self.buildTree(preorder_right, inorder_right)
        #
        return root