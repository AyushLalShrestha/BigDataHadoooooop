class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        sequence = []

        for letter in s:
            if letter in sequence:
                idx = sequence.index(letter)
                sequence = sequence[idx + 1 :]
            sequence.append(letter)
            if len(sequence) > max_length:
                max_length = len(sequence)
        return max_length


if __name__ == "__main__":
    solution = Solution()
    input_str = "abcdad"
    print(input_str, solution.lengthOfLongestSubstring(input_str))

    input_str = " a b c de"
    print(input_str, solution.lengthOfLongestSubstring(input_str))

    input_str = "pwwkew"
    print(input_str, solution.lengthOfLongestSubstring(input_str))
