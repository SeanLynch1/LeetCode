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
                
                if (x, y, bombs) in visited:
                    continue

                visited.add((x, y, bombs))

                if grid[x][y] == 1:
                    bombs -= 1

                    if bombs < 0:
                        continue

                if x == rows - 1 and y == cols -1:
                    return total 
                
                # down
                if x + 1 < rows:
                    if (x + 1, y, bombs) not in visited:
                        queue.append([x + 1, y, bombs, total + 1])
                
                # right
                if y + 1 < cols:
                    if (x, y + 1, bombs) not in visited:
                        queue.append([x, y + 1, bombs, total + 1])

                # left
                if y - 1 >= 0:
                    if (x, y - 1, bombs) not in visited:
                        queue.append([x, y - 1, bombs, total + 1])

                # up
                if x - 1 >= 0:
                    if (x - 1, y, bombs) not in visited:
                        queue.append([x - 1, y, bombs, total + 1])

        return -1