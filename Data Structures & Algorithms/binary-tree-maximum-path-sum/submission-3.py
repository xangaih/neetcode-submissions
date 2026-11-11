# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 10

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float("-infinity")

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(left, 0)                        # ← new: negative child → 0
            right = max(right, 0)

            
            res = max(res, left + right + node.val)

            return max(left, right) + node.val
        
        dfs(root)
        return res
            

        