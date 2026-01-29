class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1,2,5,7,10,15,20,0,0,0] - > 2, 5, 6
        # [1,2,3,0,0,0] -> [2,5,6]

        if not nums2:
            return
        
        i = m - 1      # end of nums1’s valid section
        j = n - 1      # end of nums2
        k = m + n - 1  # end of nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

    
        print(nums1)
        