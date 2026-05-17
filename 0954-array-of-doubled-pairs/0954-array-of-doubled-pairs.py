class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        # [4, -2, 2, -4]
        # 0 * 4 + 1 = [1] == -2
        # 2 * [2 * 0] == 8

        # [-2, -4, 2, 4]
        # arr[2 * 0 + 1] == -4
        # 2 * arr[2 * 0] == -4

        # i = 2
        # arr[2 * i + 1] == arr[5] # this will always be odd , i
        # 2 * arr[2 * i] == arr[4] # this will always be even, i - 1

        # i needs to be twice the value of i - 1

        # idxs
        # 1, 3, 5, 7, 9
        # 0, 2, 4, 6, 8

        # 2, 2, 4, 4, 4, 8

        counts = Counter(arr)
        counts = dict(sorted(counts.items(), reverse=True, key=lambda x: abs(x[0])))
        print(counts)

        for key, value in counts.items():
            if value > 0:
                needed = key / 2

                if needed in counts:
                    if counts[needed] >= value:
                        counts[needed] -= value
                        counts[key] = 0
                    else:
                        return False
                else:
                    return False

        return True