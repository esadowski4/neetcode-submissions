class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            res = max(res, len(sett))
        return res
