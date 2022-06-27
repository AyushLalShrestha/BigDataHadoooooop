class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP = [[0 for i in range(len(text2))] for j in range(len(text1))]

        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c2 == c1:
                    if i == 0 or j == 0:
                        DP[i][j] = 1
                    else:
                        DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    if i == 0 and j == 0:
                        DP[i][j] = 0
                    elif i == 0:
                        DP[i][j] = DP[i][j - 1]
                    elif j == 0:
                        DP[i][j] = DP[i - 1][j]
                    else:
                        DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

        print(DP)
        return DP[-1][-1]


if __name__ == "__main__":
    text1 = "abc"
    text2 = "abc"
    text1 = "abc"
    text2 = "def"
    text1 = "abcde"
    text2 = "ace"
    text1 = "aabcaa"
    text2 = "abca"
    solution = Solution()
    res = solution.longestCommonSubsequence(text1, text2)
    print(f"The longest common subsequence is of length: {res}")
