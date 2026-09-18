class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for num in nums:
            res.add(num)

        if len(res) != len(nums):
            return True

        return False