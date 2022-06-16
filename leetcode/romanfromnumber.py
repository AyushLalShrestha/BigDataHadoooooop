
DIGIT_TO_ROMAN = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC",
    400: "CD",
    900:  "CM"
}
valid_entries = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        while num:
            for entry in valid_entries:
                if num/entry >= 1:
                    roman += DIGIT_TO_ROMAN[entry]
                    num = num - entry
                    break
                    
        return roman
    

if __name__ == "__main__":
    num =  58
    # num = 3
    # num = 1994
    # num = 20
    solution = Solution()
    res = solution.intToRoman(num)    
    print(res)