class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapping = defaultdict(int)
        ans = [-1] * len(nums1)

        for idx, num in enumerate(nums1):
            mapping[num] = idx

        for i in range(len(nums2)):
            first_num = nums2[i]

            if first_num not in mapping:
                continue

            for j in range(i + 1, len(nums2)):
                second_num = nums2[j]
                if second_num > first_num:
                    ans[mapping[first_num]] = second_num
                    break

        return ans