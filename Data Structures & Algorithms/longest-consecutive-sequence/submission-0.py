class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # remove dups
        longest = 0

        for num in numSet:
            if num - 1 not in numSet: #beginning of sequence
                curr_len = 1
                while (num + curr_len) in numSet:
                    curr_len += 1
                longest = max(longest, curr_len)
        return longest;