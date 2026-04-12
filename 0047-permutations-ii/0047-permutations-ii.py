class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        self.output = []
        counter = Counter(nums)

        def back_track(path: List) -> None:

            if len(path) == len(nums):
                self.output.append(path.copy())
                return

            for num in counter:

                if counter[num] == 0:
                    continue

                counter[num] -= 1
                path.append(num)

                back_track(path)

                counter[num] += 1
                path.pop()
                
            return

        back_track([])

        return self.output