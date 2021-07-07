# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        root_t = t

        def _isSameTree(s,t):
            if not s and not t:
                return True
            return s and t and s.val == t.val and _isSameTree(s.left, t.left) and _isSameTree(s.right, t.right)
        
        def _isSubtree(s,t):
            if s and t:
                return _isSameTree(s,t) or _isSubtree(s.left,t) or _isSubtree(s.right,t)
            else:
                if not s and not t:
                    return True
                return False
        
        return _isSubtree(s,t)