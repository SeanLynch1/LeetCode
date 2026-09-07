class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #[
        #[1,2,2,3,5],
        #[3,2,3,4,4],
        #[2,4,5,3,1],
        #[6,7,1,4,5],
        #[5,1,1,2,4]]
        #]

        #[
        #[0,4],
        #[1,3],
        #[1,4],
        #[2,2],
        #[3,0],
        #[3,1],
        #[4,0]
        #]

        output = []
        successes = set()

        def search (x, y, curr, visited) -> int:
            
            # pacific
            if x == -1 or y == -1:
                return 1
            
            # atlantic
            if x == len(heights) or y == len(heights[0]):
                return 2

            if heights[x][y] > curr:
                return 0

            if (x,y) in successes:
                return 3

            if (x,y) in visited:
                return 0

            visited.add((x,y))

            curr = heights[x][y]
            total = 0

            #left
            left = search(x,y-1,curr,visited)
            total |= left
            #up
            up = search(x-1,y,curr,visited)
            total |= up
            #down
            down = search(x+1,y,curr,visited)
            total |= down
            #right
            right = search(x,y+1,curr,visited)
            total |= right
            if total == 3:
                return total

            return total
        
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                visited = set()
                if search(x,y,float('inf'),visited) == 3:
                    output.append([x,y])
                    successes.add((x,y))

        return output