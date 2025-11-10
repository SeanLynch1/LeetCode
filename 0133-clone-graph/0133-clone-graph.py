"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        print(f"node = {node.val}, neighbours = {node.neighbors}")

        visited = {}

        def helper(node: Optional['Node']) -> Node:

            if node.val in visited:
                return visited[node.val]
            
            new_node = Node(node.val)
            visited[node.val] = new_node

            for n in node.neighbors:
                new_node.neighbors.append(helper(n))

            return new_node

        root = helper(node)
        return root
        