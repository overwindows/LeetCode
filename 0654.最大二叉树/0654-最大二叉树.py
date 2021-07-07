# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
    
        max_num = max(nums)
        max_idx = nums.index(max_num)
        
        root = TreeNode(max_num)
        left = self.constructMaximumBinaryTree(nums[:max_idx])
        right = self.constructMaximumBinaryTree(nums[(max_idx+1):])
        
        root.left = left
        root.right = right

        return root
        