class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # [0, 1, 8, 11, 17, 22, 28]
        # [28, 27, 20, 17, 11, 6, 0]

        prefixes = [0]

        for num in nums:
            prefixes.append(num+ prefixes[-1])
        
        print(prefixes)
        suffixes = []

        for val in prefixes:
            suffixes.append(prefixes[-1] - val)
        print(suffixes)

        suffix = 0
        for i in range(len(nums)):
            if prefixes[i] == suffixes[i + 1]:
                return i


        return -1