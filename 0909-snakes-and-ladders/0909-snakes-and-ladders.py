class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        mapping = {}

        n = len(board)
        no_tiles = n * n
        tile = no_tiles

        even_odd = n % 2

        for row in range(len(board)):
            for col in range(len(board)):

                if row % 2 == even_odd:
                    val = board[row][col]
                else:
                    val = board[row][n - col - 1]

                if val != -1:
                    mapping[tile] = val
                else:
                    mapping[tile] = tile
            
                tile -= 1

        print(mapping)
        queue = deque([1])
        visited = {1}
        move = 0

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == no_tiles:
                    return move

                # add next 6
                for j in range(curr + 1, min(curr+7, no_tiles + 1)):

                    if mapping[j] not in visited:
                        queue.append(mapping[j])
                        visited.add(mapping[j])
                
            move += 1

        
        return -1
