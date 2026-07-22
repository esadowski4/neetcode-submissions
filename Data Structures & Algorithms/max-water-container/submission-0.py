class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            curr_height = min(heights[l], heights[r]) * (r - l)
            maxHeight = max(curr_height, maxHeight)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxHeight


