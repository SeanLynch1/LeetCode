class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_set = set()
        atlantic_set = set()
        output = []

        def search_pacific(x, y, curr):
            
            if x < 0 or y < 0 or x == len(heights) or y == len(heights[0]):
                return

            if heights[x][y] < curr:
                return

            if (x,y) in pacific_set:
                return

            pacific_set.add((x,y))

            # left
            search_pacific(x,y-1,heights[x][y])
            # down
            search_pacific(x+1,y,heights[x][y])
            # right
            search_pacific(x,y+1,heights[x][y])
            # up
            search_pacific(x-1,y,heights[x][y])

            return    

        def search_atlantic(x, y, curr):
            
            if x < 0 or y < 0 or x == len(heights) or y == len(heights[0]):
                return

            if heights[x][y] < curr:
                return

            if (x,y) in atlantic_set:
                return

            atlantic_set.add((x,y))

            # left
            search_atlantic(x,y-1,heights[x][y])
            # down
            search_atlantic(x+1,y,heights[x][y])
            # right
            search_atlantic(x,y+1,heights[x][y])
            # up
            search_atlantic(x-1,y,heights[x][y])

            return        

        for i in range(len(heights[0])):
            search_pacific(0,i,float('-inf'))
        for i in range(len(heights)):
            search_pacific(i,0,float('-inf'))

        for i in range(len(heights[0])):
            search_atlantic(len(heights)-1,i,float('-inf'))
        for i in range(len(heights)):
            search_atlantic(i,len(heights[0])-1,float('-inf'))

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if (x,y) in pacific_set and (x,y) in atlantic_set:
                    output.append((x,y))

        return output