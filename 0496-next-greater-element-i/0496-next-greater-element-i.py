class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapping = defaultdict(int)
        ans = [-1] * len(nums1)
        stack = []

        for idx, num in enumerate(nums1):
            mapping[num] = idx

        for i in range(len(nums2)):
            if not stack:
                curr = nums2[i]
                if curr not in mapping:
                    continue

                stack.append(curr)
                continue

            nxt = nums2[i]

            if nxt <= stack[-1]:
                stack.append(nxt)
            else:
                while stack and nxt > stack[-1]:
                    element = stack.pop()
                    idx = mapping[element]
                    ans[idx] = nxt
                
                if nxt in mapping:
                    stack.append(nxt)
            
        return ans