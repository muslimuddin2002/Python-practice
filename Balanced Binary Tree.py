class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = [True]

        def find_depth(node):
            if node is None:
                return 0
            left_depth = find_depth(node.left) + 1
            right_depth = find_depth(node.right) + 1
            is_balanced[0] = is_balanced[0] and (abs(left_depth - right_depth) <= 1)
            return max(left_depth, right_depth)

        find_depth(root)
        return is_balanced[0]
