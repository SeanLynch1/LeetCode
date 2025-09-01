class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2
        sorted(nums1)

        # define three variables
        i = m - 1 # last digit in nums1
        j = n - 1 # last digit in nums2
        k = m + n - 1 # last position in nums1

        # idea:
        # compare last digits in both lists and move backwards accordingly, a total of m + n comparisons should be made

        # loop backwards
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        
        # if i was fully iterated through but j was not that means all remaining elements in j have to be less than all elements in i
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
