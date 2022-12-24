# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        pairs = defaultdict(int)
        nodes = set()
        
        def bst(root):
            if not root:
                return 
            
            if k - root.val != root.val:
                pairs[k - root.val] = root.val 
                
            nodes.add(root.val)
            bst(root.left)
            bst(root.right)
        
        bst(root)
        
        for keys in pairs:
            if keys in nodes:
                return True
        return False
            
        
        
        
        