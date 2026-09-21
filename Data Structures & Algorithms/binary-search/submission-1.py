class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
    
    
    
    def binary_search(self, left: int, right:int, nums: List[int], target: int):
        if left > right:
            return -1

        m = (right+left) // 2
        if target < nums[m]:
            return self.binary_search(left, m-1, nums, target)
        elif target > nums[m]:
            return self.binary_search(m+1, right, nums, target)
        else:
            return m