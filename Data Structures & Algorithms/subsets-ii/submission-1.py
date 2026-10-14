class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # take i
            subset.append(nums[i])
            backtrack(i + 1)

            # skip i
            subset.pop()

            # skip duplicate entries
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            backtrack(i+1)
        
        backtrack(0)
        return res
