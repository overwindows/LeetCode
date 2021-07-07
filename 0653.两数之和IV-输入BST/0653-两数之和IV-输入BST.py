# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        def _inOrder(root, arr):
            if not root:
                return arr
            _inOrder(root.left, arr)
            arr.append(root.val)
            _inOrder(root.right,arr)

        in_order = []
        _inOrder(root, in_order)
        if len(in_order) < 2:
            return False

        s,e = 0, len(in_order)-1
        # print(in_order)
        while s < e:
            if in_order[s] + in_order[e] == k:
                return True
            elif in_order[s] + in_order[e] > k:
                e -= 1
            else:
                s+= 1
           
        return False
