# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def travalTree(root, _path, paths):
            if not root:
                return
    
            if root.left:
                _path.append(str(root.val))
                travalTree(root.left, _path, paths)
                _path.pop()
            
            if root.right:
                _path.append(str(root.val))
                travalTree(root.right, _path, paths)
                _path.pop()
            
            if not root.left and not root.right:
                _path.append(str(root.val))
                paths.append("->".join(_path))
                _path.pop()
        
        paths = []
        travalTree(root, [], paths)

        return paths