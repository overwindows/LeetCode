"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if not root:
            return root
        if not root.left and not root.right:
            return root
        queue.append(root)
        queue.append('#')
        pre_node = None
        while queue:
            #print(queue)
            node = queue.pop(0)                
            if node == '#':
                pre_node.next = None
                pre_node = None
                if queue:
                    queue.append('#')
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if pre_node:
                    pre_node.next = node
                pre_node = node
        return root