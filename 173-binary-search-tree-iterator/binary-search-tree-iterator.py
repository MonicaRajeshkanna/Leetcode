# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # Push all left children onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        # Pop the top node and process its right subtree
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self):
        # There is a next element if stack is not empty
        return len(self.stack) > 0