
from typing import List


class Solution:
    def isValidPoint(self, len_x, len_y, traversed, x, y):
        return 0 <= x < len_x and 0 <= y < len_y and [x, y] not in traversed

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        columns = len(matrix[0])
        rows = len(matrix)
        point = [0, 0]
        direction = None
        if columns > 1:
            direction = "right"
        elif rows > 1:
            direction = "down"
        else:
            return [matrix[0][0], ]

        while point:
            path.append(point)

            next_point = None
            # If next point in the given direction is not valid
            # or already traversed, change direction
            if direction == "right":
                right_point = [point[0], point[1] + 1]
                if self.isValidPoint(rows, columns, path, *right_point):
                    next_point = right_point
                else:
                    down_point = [point[0]+1, point[1]]
                    if self.isValidPoint(rows, columns, path, *down_point):
                        direction = "down"
                        next_point = down_point
            elif direction == "down":
                down_point = [point[0] + 1, point[1]]
                if self.isValidPoint(rows, columns, path, *down_point):
                    next_point = down_point
                else:
                    left_point = [point[0], point[1] - 1]
                    if self.isValidPoint(rows, columns, path, *left_point):
                        direction = "left"
                        next_point = left_point
            elif direction == "left":
                left_point = [point[0], point[1] - 1]
                if self.isValidPoint(rows, columns, path, *left_point):
                    next_point = left_point
                else:
                    up_point = [point[0]-1, point[1]]
                    if self.isValidPoint(rows, columns, path, *up_point):
                        direction = "up"
                        next_point = up_point
            elif direction == "up":
                up_point = [point[0] - 1, point[1]]
                if self.isValidPoint(rows, columns, path, *up_point):
                    next_point = up_point
                else:
                    right_point = [point[0], point[1] + 1]
                    if self.isValidPoint(rows, columns, path, *right_point):
                        next_point = right_point
                        direction = "right"

            if next_point is None or next_point in path:
                break

            point = next_point

        final = []
        for i, j in path:
            final.append(matrix[i][j])
        return final
       

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    matrix = [[1]]
    matrix = [[3],[2]]
    matrix = [[1,2,3,4,5]]
    res = solution.spiralOrder(matrix)
    print(res)


