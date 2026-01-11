class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        # build map
        mapping = {}

        n = len(board)
        tiles = n * n
        squares = tiles
        offset = n % 2 == 0

        def left_to_right(x,y):
            if board[x][y] != - 1:
                mapping[tiles] = board[x][y]
            else:
                mapping[tiles] = -1

        for i in range(n):
            for j in range(n):
                
                if offset:
                   left_to_right(i,j)
                else:
                    left_to_right(i,n - j - 1)

                tiles -= 1
            
            offset = not offset
        
        queue = deque([1])
        visited = set()
        moves = 0

        while queue:

            # add next 6 tiles

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == squares:
                    return moves

                for i in range(curr + 1, min(curr + 7, squares + 1)):

                    val = i
                    if mapping[val] != -1:
                        val = mapping[val]

                    if val not in visited:
                        queue.append(val)
                        visited.add(val)

            moves += 1

        return -1