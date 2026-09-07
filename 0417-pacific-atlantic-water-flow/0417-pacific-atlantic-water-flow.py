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
        

        def total_adder(direction, total) -> list:
            total[0] = max(direction[0], total[0])
            total[1] = max(direction[1], total[1])
            return total

        def search (x, y, curr, visited) -> list:
            
            # pacific
            if x == -1 or y == -1:
                return [0,1]
            
            # atlantic
            if x == len(heights) or y == len(heights[0]):
                return [1,0]

            if heights[x][y] > curr:
                return [0,0]

            if (x,y) in visited:
                return [0,0]
            visited.add((x,y))

            curr = heights[x][y]
            total = [0,0]

            #left
            left = search(x,y-1,curr,visited)
            total = total_adder(left, total)
            if sum(total) == 2:
                return total
            #up
            up = search(x-1,y,curr,visited)
            total = total_adder(up, total)
            if sum(total) == 2:
                return total
            #down
            down = search(x+1,y,curr,visited)
            total = total_adder(down, total)
            if sum(total) == 2:
                return total
            #right
            right = search(x,y+1,curr,visited)
            total = total_adder(right, total)
            if sum(total) == 2:
                return total

            return total
        
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                visited = set()
                if sum(search(x,y,float('inf'),visited)) == 2:
                    output.append([x,y])

        return output