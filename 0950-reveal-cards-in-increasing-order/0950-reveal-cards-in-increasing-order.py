class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        

        #[2,3,5,7,11,13,17,19]
        
        #[]   -> [2,11,3,17,5,13,7,19]
        #[2]  -> [3,17,5,13,7,19,11]
        #[3]  -> [5,13,7,19,11,17]
        #[5]  -> [7,19,11,17,13]
        #[7]  -> [11,17,13,19]
        #[11] -> [13,19,17]
        #[13] -> [17,19]
        #[17] -> [19]
        #[19] -> []

        deck.sort(reverse = True)
        output = deque([])

        for val in deck:
            for i in range(len(output) - 1):
                output.append(output.popleft())
            
            output.appendleft(val)

        return list(output)
