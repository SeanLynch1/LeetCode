class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        output = 0

        for i in range(len(arr)):
            length = 0
            curr = 0
            while i + length < len(arr):
                curr += arr[i + length]

                if (len(arr) - (length)) % 2 != 0:
                    output += curr

                length += 1
            

        return output