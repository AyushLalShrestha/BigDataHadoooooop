
from typing import List

VALID_LETTERS = ["A", "C", "G", "T"]

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        mismatched_indexes = []
        for i, letter in enumerate(startGene):
            if letter != endGene[i]:
                mismatched_indexes.append(i)

        # print(mismatched_indexes)
        steps = 0
        loop_count = 0
        while mismatched_indexes:
            if loop_count > len(bank):
                return -1
            for index in mismatched_indexes:
                val = startGene[index]
                for letter in VALID_LETTERS:
                    tempStartGene = startGene
                    if letter == val:
                        continue
                    tempStartGene = tempStartGene[0:index] + letter + tempStartGene[index+1:]
                    if tempStartGene in bank:
                        startGene = tempStartGene
                        mismatched_indexes.remove(index)
                        steps += 1
                        break
            # loop_count += 1
        return steps

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]


# startGene = "AACCGGTT"
# endGene = "AACCGGTA"
# bank = ["AACCGGTA"]

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]

print(Solution().minMutation(startGene, endGene, bank))
