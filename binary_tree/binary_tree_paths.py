# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        # traverse tree with DFS
        # 1 -> 2 -> 5
        # 5 <- 2 <- 1 -> 3
        
        def traverse_paths(node, curr_path):
            if not node:
                return

            curr_path.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(curr_path))
            else:
                traverse_paths(node.left, curr_path[:])
                traverse_paths(node.right, curr_path[:])



        traverse_paths(root, [])
        # add to result array if get to leaf node
        # keep track of current path in a list
        # at each node, append the node to the path
        # traverse to the left and right subtrees
        # join list with "->" 

        return paths