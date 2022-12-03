
from typing import List
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        sequence_count_map = defaultdict(int)
        max_palindrome_len = 0

        for word in words:
            print(f"word is {word}, map is {dict(sequence_count_map)}")
            if sequence_count_map[word[::-1]] > 0:
                max_palindrome_len += 4
                sequence_count_map[word[::-1]] -= 1
            else:
                sequence_count_map[word] += 1

        for word, count in sequence_count_map.items():
            if max_palindrome_len % 4 != 0:
                break
            if count > 0 and word == word[::-1]:
                max_palindrome_len += 2
                break
        return max_palindrome_len


a = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]

# a = ["lc","cl","gg"]

# a = ["cc","ll","xx"]

# a = ["bb", "bb"]

ans = Solution().longestPalindrome(a)
print(ans)
