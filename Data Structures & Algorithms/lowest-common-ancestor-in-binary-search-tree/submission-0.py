# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not q or not p:
            return None
        if min(q.val, p.val) > root.val: # if both nodes are greater, move to right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        elif max(q.val, p.val) < root.val: # if both nodes are lower, move to left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        

        