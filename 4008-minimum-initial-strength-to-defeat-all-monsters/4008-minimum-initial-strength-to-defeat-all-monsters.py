class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        
        # costs = [5, 10, 15] = 30

        # bonus = [0, 10, 0 ]
        # bonus = [0, 15, 15]

        # must spend what you have
        # balance always is >= 0

        bonus = defaultdict(int)
        n = len(monsters)
        curr = [0] * (n + 1)
        for l,r,v in boosts:
            curr[l] += v
            curr[r + 1] -= v

        pres = 0

        for i, val in enumerate(curr):
            pres += val
            bonus[i] += pres

        need = 0

        for i in range(n - 1, -1, -1):
            if need == 0:
                need = max(0, monsters[i] - bonus[i])
            else:
                need += monsters[i]

        return need