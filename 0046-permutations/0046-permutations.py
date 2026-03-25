class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        def backtrack(path, remaining):
            
            if not remaining:
                output.append(path)
                return

            for i in range(len(remaining)):
                backtrack(
                    path + [remaining[i]], 
                    remaining[:i] + remaining[i+1:]
                )

        backtrack([], nums)
        return output