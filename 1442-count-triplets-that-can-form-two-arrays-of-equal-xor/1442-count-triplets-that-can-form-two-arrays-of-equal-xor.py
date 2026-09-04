class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        # [2,3,1,6,7,3]
        # [0,2,1,0,6,1,2]
        # [0,3,2,4,3,0]
        # [0,1,7,0,3]

        output = 0

        for i in range(len(arr)):
            xor = 0

            for j in range(i, len(arr)):
                num = arr[j]
                xor ^= num

                if xor == 0:
                    output += j - i 

        return output