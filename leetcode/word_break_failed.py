from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_buffer = ""
        for char in s:
            str_buffer += char
            print(f"Buffer: {str_buffer}")
            if str_buffer in wordDict:
                str_buffer = ""
        return False if str_buffer else True


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]

    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    solution = Solution()
    res = solution.wordBreak(s, wordDict)
    print(res)
