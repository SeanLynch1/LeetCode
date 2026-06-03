class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        output = 0

        for i in range(len(arr)):
            length = 0
            curr = 0
            while i + length < len(arr):
                curr += sum(arr[i:i + length + 1])
                length += 2
            
            output += curr

        return output