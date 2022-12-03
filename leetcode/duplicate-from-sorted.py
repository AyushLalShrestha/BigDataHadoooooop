from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        pointer = 0
        for i in range(len(nums)):
            if i == 0:
                count += 1
                pointer = 1
                continue

            if nums[i] != nums[pointer - 1]:
                nums[pointer] = nums[i]
                pointer += 1
                count += 1

        return count


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(Solution().removeDuplicates(arr))
