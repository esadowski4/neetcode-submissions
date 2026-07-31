class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        hashmap = {}
        for i in range(len(position)):
            hashmap[position[i]] = (target - position[i]) / speed[i]
        
        for pos in sorted(hashmap.keys(), reverse=True):
            time = hashmap[pos]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)