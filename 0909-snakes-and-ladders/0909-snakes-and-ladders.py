class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        

        mapping = defaultdict(int)
        
        n_rows = len(board[0])
        tiles = n_rows **2
        squares = tiles + 1
        toggle = n_rows % 2 == 0
        for i in range(n_rows):
            for j in range(n_rows):
                if toggle:
                    if board[i][j] != -1:
                        mapping[tiles] = board[i][j]
                    else:
                        mapping[tiles] = -1
                else:
                    start_right = n_rows - j - 1
                    if board[i][start_right] != -1:
                        mapping[tiles] = board[i][start_right]
                    else:
                        mapping[tiles] = -1

                tiles -= 1

            toggle = not toggle

        queue = deque([1])
        visited = set()
        moves = 0
        while queue:
            
            for val in range(len(queue)):
                curr = queue.popleft()
                for k in range(curr + 1, min(curr + 7,squares)):

                    if mapping[k] != -1:
                        k = mapping[k]

                    print(f"k = {k}")

                    if k == squares-1:
                        return moves + 1

                    if k not in visited:
                        queue.append(k)
                        visited.add(k)

                    
                    
            moves += 1

        return -1

