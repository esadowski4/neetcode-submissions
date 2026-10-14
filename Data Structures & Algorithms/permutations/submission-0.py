class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = [] # think of this like a backpack

        def backtrack():
            if len(nums) == len(perm):
                res.append(perm.copy())
                return
            
            # loop through every number in nums
            for n in nums:
                # say we have [1,2], we will skip 1 and 2, and then add 3 bc it is the only one we havent added yet
                if n in perm:
                    continue
                
                perm.append(n) # add n to current permutation

                # move to next slot in permutation
                backtrack()

                # go back and select a different number, bc the loop will go to the next num
                perm.pop()
        
        backtrack()
        return res