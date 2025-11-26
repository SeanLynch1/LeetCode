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
            return

        visited = {}

        def helper(node) -> Node:
            if node in visited:
                return visited[node]

            root = Node(node.val)

            visited[node] = root

            # explore neighbors
            for n in node.neighbors:
                root.neighbors.append(helper(n))

            return root

        return helper(node)