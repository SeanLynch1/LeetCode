class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # O(n)
        # loop through from first index, if we run out of gas reset everything to zero, begin a 
        # next index, set this index to the start point, if we keep failing, 
        # last index will be the solution

        tank = 0
        diff = 0 # combines gas and cost
        start_index = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            diff += gas[i] - cost[i]

            if tank < 0:
                start_index = i + 1
                tank = 0

        return start_index if diff >= 0 else -1