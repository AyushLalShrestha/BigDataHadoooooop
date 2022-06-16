


import heapq
import math
from typing import List


def get_valid_siblings(x_coord, y_coord, len_x, len_y):
	valid_siblings = []
	if 0 <= y_coord-1 < len_y:
		valid_siblings.append([x_coord, y_coord-1])
	if 0 <= y_coord+1 < len_y:
		valid_siblings.append([x_coord, y_coord+1])
	if 0 <= x_coord-1 < len_x:
		valid_siblings.append([x_coord-1, y_coord])
	if 0 <= x_coord+1 < len_x:
		valid_siblings.append([x_coord+1, y_coord])
	return valid_siblings



class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		len_x = len(heights)
		len_y = len(heights[0])
		if len_x * len_y == 1:
			return 0

		dijkstraGraph = []
		for row in heights:
			graphRow = []
			for _ in row:
				graphRow.append(math.inf)
			dijkstraGraph.append(graphRow)

		# List of traversed_nodes
		traversed = []
		
		dijkstraGraph[0][0] = 0
		priority_queue = []
		heapq.heappush(priority_queue, [dijkstraGraph[0][0], 0, 0])

		while priority_queue:
			_, i, j = heapq.heappop(priority_queue)
			to_traverse = [i, j]
			to_traverse_max_jump = dijkstraGraph[i][j]
			to_traverse_value = heights[i][j]
			traversed.append(to_traverse)
			if i == len_x - 1 and j == len_y - 1:
				return dijkstraGraph[-1][-1]

			for sibling_x, sibling_y in get_valid_siblings(i, j, len_x, len_y):
				sibling_max_jump = dijkstraGraph[sibling_x][sibling_y]
				sibling_value = heights[sibling_x][sibling_y]
				jump_value = abs(to_traverse_value - sibling_value)

				if jump_value < sibling_max_jump:
					if jump_value < to_traverse_max_jump:
						dijkstraGraph[sibling_x][sibling_y] = to_traverse_max_jump
					else:
						dijkstraGraph[sibling_x][sibling_y] = jump_value

				if [sibling_x, sibling_y] not in traversed :
					heapq.heappush(priority_queue, [dijkstraGraph[sibling_x][sibling_y], sibling_x, sibling_y])

		return dijkstraGraph[-1][-1]


if __name__ == "__main__":
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    # heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    # heights = [[1,10,6,7,9,10,4,9]]
    solution = Solution()
    print(solution.minimumEffortPath(heights))
	