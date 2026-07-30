class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                value, index = stack.pop()
                res[index] = i - index

            stack.append((v, i))
        return res

