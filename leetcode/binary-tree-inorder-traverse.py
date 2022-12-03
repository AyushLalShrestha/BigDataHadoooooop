

from typing import Optional


class Solution:
    def traverse(self, node, ):
        if node.left:
            self.traverse(node.left)
        self.asc_order.append(node.val)
        if node.right:
            self.traverse(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.asc_order = []
        if not root:
            return self.asc_order
        self.traverse(root)
        return self.asc_order