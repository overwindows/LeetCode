"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None 
        visited = {}

        def _cloneGraph(node):
            if node.val in visited:
                return visited[node.val]

            clone_node = Node(node.val)
            visited[node.val] = clone_node
            for neighbor in node.neighbors:
                clone_neighbor = _cloneGraph(neighbor)
                clone_node.neighbors.append(clone_neighbor)
            return clone_node
        # print(node.val)
        clone_graph = _cloneGraph(node)

        return clone_graph