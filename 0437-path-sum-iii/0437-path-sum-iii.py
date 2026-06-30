# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        d = {0: 1}

        def dfs(root, s):
            if not root:
                return 0

            s += root.val
            ans = d.get(s - targetSum, 0)

            d[s] = d.get(s, 0) + 1
            ans += dfs(root.left, s)
            ans += dfs(root.right, s)
            d[s] -= 1

            return ans

        return dfs(root, 0)