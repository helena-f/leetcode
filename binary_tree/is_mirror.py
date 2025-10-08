# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self, node_left, node_right):
    # if leaf node we got through the tree and found 
        # symmetry, return true
        if not node_left and not node_right:
            return True
        elif not node_left or not node_right:
            return False

        # if left and rightmost are the same value
        # compare the next node; 
        if node_left.val != node_right.val:
            return False
        # right of left and left of right
        # left of left, right of right
        return self.isMirror(node_left.left, node_right.right) and self.isMirror(node_left.right, node_right.left) 

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        return self.isMirror(root.left, root.right)