# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def _sum(node, left):
            if not node:
                return 0
            
            if not node.left and not node.right and left:
                return node.val

            return _sum(node.left, True)+_sum(node.right, False)

        return _sum(root, False)

