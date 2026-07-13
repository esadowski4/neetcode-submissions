class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = n * [0]
        suff = n * [0]
        res = n * [0]

        pref[0] = suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i - 1] * pref[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            res[i] = suff[i] * pref[i]
        return res