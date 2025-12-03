# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        del_set = set(to_delete)

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in del_set:
                del_set.remove(node.val)
                if node.left:
                    res.append(node.left) 
                if node.right:
                    res.append(node.right)
                
                return None
            
            return node

        newnode = dfs(root)
        if newnode:
            res.append(newnode)
        return res