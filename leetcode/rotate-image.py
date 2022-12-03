from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_len = len(matrix[0])

        matrix_copy = []
        for i in range(matrix_len):
            row = []
            for j in range(matrix_len - 1, -1, -1):
                row.append(matrix[j][i])
            matrix_copy.append(row)

        for i, row in enumerate(matrix_copy):
            for j, elem in enumerate(row):
                matrix[i][j] = elem


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)
    print(matrix)
