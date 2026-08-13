class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapping = defaultdict(int)
        ans = [-1] * len(nums1)
        stack = []

        for idx, num in enumerate(nums1):
            mapping[num] = idx

        for i in range(len(nums2)):
            nxt = nums2[i]

            while stack and nxt > stack[-1]:
                element = stack.pop()
                idx = mapping[element]
                ans[idx] = nxt
            
            if nxt in mapping:
                stack.append(nxt)
            
        return ans