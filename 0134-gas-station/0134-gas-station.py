class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # O(n)
        # loop through from first index, if we run out of gas reset everything to zero, begin a 
        # next index, set this index to the start point, if we keep failing, 
        # last index will be the solution

        tank = 0
        total_gas = 0
        total_cost = 0
        start_index = 0

        for i in range(len(gas)):
            tank += gas[i]
            total_cost += cost[i]
            total_gas += gas[i]

            if tank >= cost[i]:
                tank -= cost[i]
            else:
                start_index = i + 1
                tank = 0

        if total_cost <= total_gas:
            return start_index
        else:
            return -1
