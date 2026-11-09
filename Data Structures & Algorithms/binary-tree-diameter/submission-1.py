# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0     
        def get_height(node):
            if node is None:
                return 0
            else:
                left_height = get_height(node.left)
                right_height = get_height(node.right)
                self.max_diam = max(self.max_diam, left_height + right_height)
                return 1 + max(left_height,right_height)
        get_height(root)
        return self.max_diam
            