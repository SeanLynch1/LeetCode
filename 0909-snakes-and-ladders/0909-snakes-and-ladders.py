class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        no_tiles = n**2

        if no_tiles < 6:
            return 1
            
        

        mapping = {}


        tile = 1
        for i in range(len(board)-1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                for j in range(len(board[i])):
                    mapping[tile] = board[i][j]
                    tile += 1
            else:
                for j in range(len(board[i])-1, -1, -1):
                    mapping[tile] = board[i][j]
                    tile += 1
        
        for i in range(len(board)):
            print(board[i])
        
        visited = set()
        queue = deque([1])
        visited.add(1)

        steps = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == no_tiles:
                    return steps
                
                # add next 6 from
                for j in range(curr + 1, min(curr + 7, no_tiles + 1)):
                    temp = j

                    if mapping[temp] != -1:
                        temp = mapping[temp]

                    if temp not in visited:
                        queue.append(temp)
                        visited.add(temp)
            
            steps += 1

        return -1