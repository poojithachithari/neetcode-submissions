# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(root):
            if root is None:
                return [None]
            else:
                return [root.val]+preorder(root.left)+preorder(root.right)

        
        val1 = preorder(p)
        val2 = preorder(q)

        if val1 == val2:
            return True
        else:
            return False
        

        
        