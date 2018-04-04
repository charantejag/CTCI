# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""
        string = ""
        string += str(t.val)
        if t.left:
            string += "("
            string += self.tree2str(t.left)
            string += ")"
        elif t.right:
            string += "()"
        if t.right:
            string += "("
            string += self.tree2str(t.right)
            string += ")"
        return string
        
       