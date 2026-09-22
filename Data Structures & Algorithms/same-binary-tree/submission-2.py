# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        else: 
            return False
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def preorder(root):
        #     if root is None:
        #         return [None]
        #     else:
        #         return [root.val]+preorder(root.left)+preorder(root.right)

        
        # val1 = preorder(p)
        # val2 = preorder(q)

        # if val1 == val2:
        #     return True
        # else:
        #     return False
        

        
        