class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        

        rows = len(grid)
        cols = len(grid[0])

        queue = deque([[0, 0, k, 0]])
        visited = set()
        total = 0

        while queue:

            for i in range(len(queue)):
                x, y, bombs, total = queue.popleft()
                
                if x < 0 or x == rows:
                    continue

                if y < 0 or y == cols:
                    continue

                if grid[x][y] == 1:
                    bombs -= 1

                    if bombs < 0:
                        continue

                if (x, y, bombs) in visited:
                    continue

                visited.add((x, y, bombs))

                if x == rows - 1 and y == cols -1:
                    return total 
                
                # down
                queue.append([x + 1, y, bombs, total + 1])
                
                # right
                queue.append([x, y + 1, bombs, total + 1])

                # left
                queue.append([x, y - 1, bombs, total + 1])

                # up
                queue.append([x - 1, y, bombs, total + 1])

        return -1