class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return 

        i = len(nums1) - 1
        m -= 1
        n -= 1

        while i >= 0:

            var_1 = nums1[m]
            var_2 = nums2[n]

            if m >= 0 and var_1 > var_2:
                nums1[i] = var_1
                m -= 1

            else:
                nums1[i] = var_2
                n -= 1

                if n < 0:
                    return

            i -= 1
            print("Hi")
            print(nums1)



