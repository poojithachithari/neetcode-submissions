# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not  inorder:
            return None
        
        inorder_index = {}
        for i,val in enumerate(inorder):
            inorder_index[val] = i
        
        self.pre_index = 0

        def bintree(start,end):
            if start > end:
                return None
            
            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)

            self.pre_index +=1

            io_idx = inorder_index[root_val]

            root.left = bintree(start,io_idx-1)
            root.right = bintree(io_idx +1 , end)
            return root
        return bintree(0,len(inorder)-1)

        