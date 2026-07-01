class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {} # num->index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev: # in looks at the key
                return [prev[diff], i]
            prev[n] = i