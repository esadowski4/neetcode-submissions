# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            qLen = len(queue)
            level = []
            for i in range(qLen):
                node = queue.popleft()
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                level.append(node.val)
            if level:
                res.append(level)
        
        return res
