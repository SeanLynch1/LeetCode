class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        balance = 0
        start = 0
        gas_tank = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            balance += diff
            gas_tank += diff

            if gas_tank < 0:
                start = i + 1
                gas_tank = 0
        
        if balance < 0:
            start = -1
        
        return start

