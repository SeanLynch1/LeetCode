class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        

        rows = len(grid)
        cols = len(grid[0])

        queue = deque([[0, 0, k, 0]])
        visited = defaultdict(int)
        total = 0

        dirs = [(1,0),(0,1),(0,-1), (-1,0)]

        while queue:
            for i in range(len(queue)):
                x, y, bombs, total = queue.popleft()
                
                if (x, y) in visited and bombs <= visited[(x,y)]:
                    continue
                visited[(x, y)] = bombs

                if x == rows - 1 and y == cols -1:
                    return total 
                
                # down, right, left, up
                for v, h in dirs:
                    new_bombs = bombs - grid[x][y]
                    if new_bombs >= 0:
                        if x + v >= 0 and x + v < rows and y + h >= 0 and y + h < cols:
                            queue.append([x + v, y + h, new_bombs, total + 1])

        return -1