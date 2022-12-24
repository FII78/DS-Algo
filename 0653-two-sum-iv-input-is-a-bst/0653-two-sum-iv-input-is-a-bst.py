# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        pairs = set()
        
        def search(root):
            # if there was a valid pair it wud've been returned by now
            if not root: 
                return False
            
            if root.val in pairs:
                return True
            
            pairs.add(k - root.val)
            return search(root.left) or search(root.right)
        
        return search(root)