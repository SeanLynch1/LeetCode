class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        #[9, 16, 11, 18]

        #[2,2,3,4,6, 6, 7, 8,   ]
        #[0,2,4,7,11,17,23,30,38]

        #[1,2,2,5,5, 6, 7, 8,   ]
        #[0,1,3,5,10,15,21,28,36]

        nums.sort()
        prefixes = [0]
        ans = []
        for i in range(len(nums)):
            prefixes.append(prefixes[-1] + nums[i])
        print(prefixes)
        
        for q in queries:
            ans.append(bisect_right(prefixes,q)-1)
        return ans