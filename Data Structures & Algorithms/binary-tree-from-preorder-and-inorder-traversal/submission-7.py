# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # phone book: value -> its index in inorder (built once)
        indexOf = {}
        for i, val in enumerate(inorder):
            indexOf[val] = i

        self.pre = 0  # points at the next boss in preorder

        def helper(l, r):
            # empty range: no node here
            if l > r:
                return None

            # next boss comes straight from preorder
            boss = preorder[self.pre]
            self.pre += 1
            node = TreeNode(boss)

            # where the boss sits in inorder
            mid = indexOf[boss]

            # build left first (that's preorder's order), then right
            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)
            return node

        return helper(0, len(inorder) - 1)

