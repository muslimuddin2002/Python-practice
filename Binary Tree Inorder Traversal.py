# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        current = root

        while True:
            while current:
                stack.append(current)
                current = current.left      
            if stack:
                node = stack.pop()
                result.append(node.val)     
                current = node.right
            else:
                break
        return result
           
