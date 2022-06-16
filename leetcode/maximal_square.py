from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memoized_matrix = [[0 for _ in row] for row in matrix]
        max_val = 0
        for i, row in enumerate(matrix):
            for j, bit in enumerate(row):
                if bit != "1":
                    continue
                memoized_matrix[i][j] = 1
                if max_val == 0:
                    max_val = 1

                if i <= 0 or j <= 0:
                    continue

                # check if all siblings are 1
                if (
                    matrix[i - 1][j] == "0"
                    or matrix[i][j - 1] == "0"
                    or matrix[i - 1][j - 1] == "0"
                ):
                    continue

                minimum_val = min(
                    memoized_matrix[i - 1][j],
                    memoized_matrix[i][j - 1],
                    memoized_matrix[i - 1][j - 1],
                )
                # val = int((minimum_val ** (1 / 2) + 1) ** 2)
                val = minimum_val + 1
                memoized_matrix[i][j] = val
                if val > max_val:
                    max_val = val

        return max_val ** 2


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    # matrix = [["0"], ["0"], ["0"]]
    # matrix = [
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    # ]

    solution = Solution()
    res = solution.maximalSquare(matrix)
    print(res)
