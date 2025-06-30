# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# NOTE DOESN'T RUN IN LEETCODE DUE TO NONLOCAL
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = root.val
        
        def inorder(node):
            nonlocal counter, res
            if not node:
                return

            inorder(node.left)
            counter -= 1
            if counter == 0:
                res = node.val
                return
            inorder(node.right)
        inorder(root)
        return res