class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        mapping = {}
        n = len(board)
        total_squares = n * n
        tile_no = total_squares

        order = n % 2
        for i in range(n):
            for j in range(n):
                if i % 2 == order:
                    if board[i][j] == -1:
                        mapping[tile_no] = tile_no
                    else:
                        mapping[tile_no] = board[i][j]
                else:
                    if board[i][ (n - 1) - j] == -1:
                        mapping[tile_no] = tile_no
                    else:
                        mapping[tile_no] = board[i][ (n - 1) - j]

                tile_no -= 1

        print(mapping)
                
        # Breadth First Search

        moves = 0
        queue = deque([1])
        visited = {1}

        while(queue):
            for j in range(len(queue)):
                curr = queue.popleft()

                if curr == total_squares:
                    print("SQUARE FOUND")
                    return moves

                for i in range(curr + 1, min(curr + 7, total_squares + 1)):
                    
                    print(mapping[i])
                    
                    if mapping[i] not in visited:
                        visited.add(mapping[i])
                        queue.append(mapping[i])
                
            print(f"queue = {queue} \n")
                
            moves += 1

        return -1
