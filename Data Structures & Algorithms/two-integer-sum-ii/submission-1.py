class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in res:
                return [res[diff], i + 1]
            res[numbers[i]] = i + 1
        return []
