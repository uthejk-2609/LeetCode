# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def post_order_traverse(root):
            if root == None:
                return res
                
            post_order_traverse(root.left)
            post_order_traverse(root.right)
            res.append(root.val)

        post_order_traverse(root)
        return res
