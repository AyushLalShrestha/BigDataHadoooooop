vowels = ["a", "e", "i", "o", "u"]


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_in_string = []

        string_array = []
        for letter in s:
            if letter.lower() in vowels:
                vowels_in_string.append(letter)
            string_array.append(letter)

        final_string = ""
        for letter in string_array:
            if letter.lower() in vowels:
                final_string += vowels_in_string.pop()
            else:
                final_string += letter
        return final_string
