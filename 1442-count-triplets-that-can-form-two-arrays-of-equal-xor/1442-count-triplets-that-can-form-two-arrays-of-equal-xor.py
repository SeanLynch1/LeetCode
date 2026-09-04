class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        prefix = [0]
        for x in arr:
            prefix.append(prefix[-1] ^ x)

        ans = 0

        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    ans += k - i

        return ans