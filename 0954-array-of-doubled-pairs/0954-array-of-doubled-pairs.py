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

        # sliding window?
        arr.sort(reverse = True, key = lambda x: abs(x))
        print(arr)

        mid = int(len(arr) / 2)
        counts = Counter(arr)

        print(counts)

        for key in arr:
            print(f"key = {key}")
            needed = key / 2

            print(f"needed = {needed}")
            while counts[key] > 0: 
                counts[needed] -= 1
                counts[key] -= 1
            
            if counts[needed] < 0:
                return False

        return True