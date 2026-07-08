class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
        for i in range(k):
            key = max(seen, key=seen.get)
            res.append(key)
            seen.pop(key)
        return res