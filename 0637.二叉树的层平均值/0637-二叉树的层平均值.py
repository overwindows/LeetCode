# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        avg = []
        bfs = []

        bfs.append(root)
        bfs.append(None)
        buf = []

        while bfs:
            node = bfs.pop(0)
            if node:
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
                buf.append(node.val)
            else:
                if len(bfs) > 0:
                    avg.append(sum(buf)*1.0/len(buf))
                    bfs.append(None)
                    buf = []
                else:
                    break
        
        if buf:
            avg.append(sum(buf)*1.0/len(buf))
        
        return avg
        
            