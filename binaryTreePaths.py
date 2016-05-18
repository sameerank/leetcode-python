# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            left_path = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
            right_path = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
            return left_path + right_path
