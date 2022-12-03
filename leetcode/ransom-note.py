

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        reserved = []
        magazine = list(magazine)
        for s in ransomNote:
            if s not in magazine:
                return False
            magazine.remove(s)
        return True


if __name__ == "__main__":
    solution = Solution()
    ransomNote = "a"
    magazine = "b"
    print(solution.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "aab"

    print(solution.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "ab"
    print(solution.canConstruct(ransomNote, magazine))

