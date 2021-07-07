# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = 0
        if not root:
            return 0 
        def _diameter(root):
            if not root.left and not root.right:
                return 1,1
            lf_dep,lf_dia,rt_dia,rt_dep = 0,0,0,0
            if root.left:
                lf_dep, lf_dia = _diameter(root.left)
            if root.right:
                rt_dep, rt_dia = _diameter(root.right)
            
            return max(lf_dep,rt_dep)+1, max(lf_dep+rt_dep+1, lf_dia, rt_dia)

        _, max_diameter = _diameter(root)

        return max_diameter-1