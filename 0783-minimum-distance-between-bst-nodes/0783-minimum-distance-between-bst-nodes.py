# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)
        
        minim = float("inf")
        inorder(root)
        
        for i in range(len(self.arr)-1):
            if self.arr[i+1] - self.arr[i] > 0:
                minim = min(self.arr[i+1] - self.arr[i],minim)
                
        return minim
        