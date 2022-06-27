from typing import List


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.leftNode = left
        self.rightNode = right
        self.invalid = False

    def __str__(self,):
        str_repr = f"{self.value}"
        if self.leftNode:
            str_repr += f", left={self.leftNode.value}"
        if self.rightNode:
            str_repr += f", right={self.rightNode.value}"
        return str_repr


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        len_x = len(heights)
        len_y = len(heights[0])
        if len_x * len_y == 1:
            return 0

        max_jump = 0
        binary_tree_map = [[None for i in row] for row in heights]
        for i in range(len(heights) - 1, -1, -1):
            for j in range(len(heights[0]) - 1, -1, -1):
                elem_value = heights[i][j]

                right_node = None
                if 0 <= j + 1 < len_y and binary_tree_map[i][j + 1] != None:
                    right_node = binary_tree_map[i][j + 1]
                    if abs(right_node.value - elem_value) > max_jump:
                        max_jump = abs(right_node.value - elem_value)
                down_node = None
                if 0 <= i + 1 < len_x and binary_tree_map[i + 1][j] != None:
                    down_node = binary_tree_map[i + 1][j]
                    if abs(down_node.value - elem_value) > max_jump:
                        max_jump = abs(down_node.value - elem_value)

                binary_tree_map[i][j] = Node(
                    elem_value, left=down_node, right=right_node
                )

        traverse_again = True

        while traverse_again:
            max_jump -= 1
            traverse = False
            next_nodes = [
                binary_tree_map[0][0],
            ]
            while next_nodes:
                node = next_nodes.pop(0)
                if node.leftNode and not node.leftNode.invalid:
                    if abs(node.leftNode.value - node.value) <= max_jump:
                        next_nodes.append(node.leftNode)
                        if (
                            node.leftNode.leftNode == None
                            and node.leftNode.rightNode == None
                        ):
                            print(f"a")
                            traverse = True
                    else:
                        node.leftNode.invalid = True
                if node.rightNode and not node.rightNode.invalid:
                    if abs(node.rightNode.value - node.value) <= max_jump:
                        next_nodes.append(node.rightNode)
                        if (
                            node.rightNode.leftNode == None
                            and node.rightNode.rightNode == None
                        ):
                            print(f"a")
                            traverse = True
                    else:
                        node.rightNode.invalid = True
            traverse_again = traverse

            if not traverse_again:
                max_jump += 1
        return max_jump


solution = Solution()

# heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]  # 1

# heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]  # 2

# heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]] #0

# heights = [[1,10,6,7,9,10,4,9]] #9

lowest = solution.minimumEffortPath(heights)
print(lowest)
