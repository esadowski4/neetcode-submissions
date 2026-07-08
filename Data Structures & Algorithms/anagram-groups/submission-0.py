class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #count of occurences -> List of anagrams
        for word in strs:
            count = 26 * [0]
            for c in word:
                count[(ord(c) - ord('a'))] += 1
            if tuple(count) not in res:
                res[tuple(count)] = []
            res[tuple(count)].append(word)
        return list(res.values());