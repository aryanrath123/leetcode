# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(root, mx):
            if not root:
                return 0
            c = 0
            if root.val >= mx:
                c = 1
            mx = max(mx, root.val)
            return c + dfs(root.left, mx) + dfs(root.right, mx)

        return dfs(root, float("-inf"))