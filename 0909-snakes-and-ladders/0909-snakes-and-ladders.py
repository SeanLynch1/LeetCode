class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        no_tiles = n**2

        if no_tiles < 6:
            return 1
        visited = set()
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
        
        queue = deque()

        # initialize queue
        for i in range(2, 8):
            curr = i
            # for ladders that lead to another ladder

            if mapping[curr] != -1 and mapping[curr] != curr:
                curr = mapping[curr]

            if curr not in visited:
                queue.append(curr)
                if mapping[curr] == -1:
                    visited.add(curr)
            
        print(f"queue = {queue}")
        print(f"visited = {visited}","\n")
        steps = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == no_tiles:
                    return steps + 1
                
                # add next 6 from
                for j in range(curr + 1, min(curr + 7, no_tiles + 1)):
                    temp = j

                    if temp not in visited and mapping[temp] not in visited:
                        if mapping[temp] != -1 and mapping[temp] != temp:
                            visited.add(temp)
                            temp = mapping[temp]
                            #visited.add(temp)

                        if temp not in visited:
                            queue.append(temp)
                            if mapping[temp] == -1:
                                visited.add(temp)
            
            steps += 1
            print(f"queue = {queue}")
            print(f"visited = {visited}", "\n")


        return -1