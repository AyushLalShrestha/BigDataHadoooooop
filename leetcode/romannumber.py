
ROMAN_TO_DIGIT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

ROMAN_COMBO_TO_DIGIT = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        while s:
            if s[0] in ROMAN_TO_DIGIT:
                if len(s) >= 2 and s[:2] in ROMAN_COMBO_TO_DIGIT:
                    total += ROMAN_COMBO_TO_DIGIT[s[:2]]
                    s = s[2:]
                else:
                    total += ROMAN_TO_DIGIT[s[0]]
                    s = s[1:]
        return total


if __name__ == "__main__":
    roman_num = "MCMXCIV"
    roman_num = "LVIII"
    roman_num = "III"
    solution = Solution()
    res = solution.romanToInt(roman_num)
    print(res)
