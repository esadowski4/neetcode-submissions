class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i] 
            if res[diff]:
                return [res[diff], i + 1]
            res[numbers[i]] = i + 1
        return []
