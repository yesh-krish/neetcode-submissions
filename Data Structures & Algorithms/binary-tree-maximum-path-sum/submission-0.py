class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')  # Initialize to negative infinity

        def dfs(node):
            if not node:
                return 0
            left_max = max(0, dfs(node.left))   # Ignore negative paths
            right_max = max(0, dfs(node.right)) # Ignore negative paths

            # Update the global max path sum
            self.res = max(self.res, left_max + right_max + node.val)

            # Return max path sum including current node and one subtree
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.res
