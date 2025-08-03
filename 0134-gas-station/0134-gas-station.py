class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        balance = 0
        start = -1
        gas_tank = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            balance += diff
            gas_tank += gas[i]
            gas_tank -= cost[i]

            if gas_tank >= 0:
                if start == -1:
                    start = i
            else:
                start = -1
                gas_tank = 0
        
        if balance < 0:
            start = -1
        
        return start

