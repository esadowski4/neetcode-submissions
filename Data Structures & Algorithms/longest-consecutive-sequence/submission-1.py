class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #remove dups
        sett = set(nums)
        max_len = 0
        # find start of sequence
        for num in sett:
            if num - 1 not in sett:
                curr_len = 1
                while num + curr_len in sett:
                    curr_len += 1
                max_len = max(curr_len, max_len)
        
        return max_len