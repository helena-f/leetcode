
# Binary Tree Level Order Traversal
# Solved 
# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        q = deque([root])
        level_counter = 0
        while q:
            curr_level = []
            for i in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr_level)
        print(level_counter)
        return res