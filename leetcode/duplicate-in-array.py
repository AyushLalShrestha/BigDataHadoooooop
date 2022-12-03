from collections import defaultdict
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > 1:
                duplicates.append(n)

        return duplicates


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(solution.findDuplicates(nums))
