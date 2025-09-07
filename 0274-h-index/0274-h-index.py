class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations = sorted(citations)

        print(citations)

        count = 1
        h_index = citations[-1] 

        if h_index == 0:
            return 0

        for i in range(len(citations) - 2, -1 , -1):
            print("h_index = ", h_index, "count = ", count)
            
            if citations[i] <= h_index and count < h_index:
                
                h_index = citations[i]

                if h_index > count:
                    count += 1



        return count