
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def traverse(self, current_node, p, q):
        self.priority_queue.append(current_node)
        if current_node == p:
            self.p_ancestors.extend(self.priority_queue)
        if current_node == q:
            self.q_ancestors.extend(self.priority_queue)
        if current_node.left:
            self.traverse(current_node.left, p, q)
        if current_node.right:
            self.traverse(current_node.right, p, q)

        self.priority_queue.pop()

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.priority_queue = []
        self.p_ancestors = []
        self.q_ancestors = []
        self.traverse(root, p, q)

        for p_ans in self.p_ancestors[::-1]:
            if p_ans in self.q_ancestors:
                return p_ans
