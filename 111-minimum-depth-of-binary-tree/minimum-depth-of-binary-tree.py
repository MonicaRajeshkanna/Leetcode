class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # If no left child, go right
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If no right child, go left
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
