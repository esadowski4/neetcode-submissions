class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxRight = height[r]
        maxLeft = height[l]
        water = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                water += maxRight - height[r]
            
        return water