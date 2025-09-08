class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        bucket = 0
        water = 0

        l_height = height[left]
        r_height = height[right]

        print("l_height = ", l_height)
        print("r_height = ", r_height)

        while left < right:
            
            if height[left] < height[right]:
                
                if height[left] > l_height:
                    water += bucket
                    print(f"emptying bucket full of {bucket} to water, water = {water}")

                    l_height = height[left]
                    bucket = 0
                    print("upgrading l_height to ", l_height)
                else:
                    bucket += l_height - height[left]
                    print(f"filling bucket, bucket = {bucket}")

                print("l_height = ", l_height)
                print("\n")
                left += 1
            else:
                if height[right] > r_height:
                    water += bucket
                    print(f"emptying bucket full of {bucket} to water, water = {water}")

                    r_height = height[right]
                    bucket = 0
                    print("upgrading r_height to ", r_height)

                else:
                    bucket += r_height - height[right]
                    print(f"filling bucket, bucket = {bucket}")


                print("r_height = ", r_height)
                right -= 1
        water += bucket
        
        return water