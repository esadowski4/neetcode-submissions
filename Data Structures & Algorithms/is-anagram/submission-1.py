class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ress = [0] * 26
        rest = [0] * 26
        for c in s:
            pos = 26 - (122 - ord(c) + 1)
            ress[pos] += 1
        for c in t:
            pos = 26 - (122 - ord(c) + 1)
            rest[pos] += 1
        return ress == rest