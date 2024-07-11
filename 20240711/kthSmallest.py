def inorder(root, ar):
    if not root:
        return 
    inorder(root.left, ar)
    ar.append(root.val)
    inorder(root.right,ar)
    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ar = []  
        inorder(root,ar)
        return ar[k-1]  