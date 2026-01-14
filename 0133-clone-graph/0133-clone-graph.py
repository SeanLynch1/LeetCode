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
        if node is None:
            return None

        mapping = {}

        # dfs graph
        def dfs(original: Node) -> Node:
            
            if original in mapping:
                return mapping[original]

            mapping[original] = Node(original.val)
            clone = mapping[original]

            for n in original.neighbors:
                clone.neighbors.append(dfs(n))

            return clone
        
        return dfs(node)

