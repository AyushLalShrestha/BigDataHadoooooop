

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        to_traverse = [root, ]
        traversed_nodes = []
        min_distance = None

        while to_traverse:
            pointer_node = to_traverse.pop()

            for traversed in traversed_nodes:
                diff = abs(traversed.val - pointer_node.val)
                if not min_distance or diff < min_distance:
                    min_distance = diff

            traversed_nodes.append(pointer_node)
            if pointer_node.left:
                to_traverse.append(pointer_node.left)
            if pointer_node.right:
                to_traverse.append(pointer_node.right)

        return min_distance
