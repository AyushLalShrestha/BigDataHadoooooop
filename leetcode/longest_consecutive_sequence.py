

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hp = {}
        max_length = 1
        if not nums:
            return 0
        for num in nums:
            if num in hp:
                continue
            if num-1 in hp and num+1 in hp:
                hp[num] = [hp[num-1][0], hp[num+1][1], hp[num-1][2] + hp[num+1][2] + 1]
                hp[hp[num][0]] = hp[num]
                hp[hp[num][1]] = hp[num]
            elif num-1 in hp:
                hp[num] = [hp[num-1][0], num, hp[num-1][2] + 1]
                # hp[num-1] = hp[num]
                hp[hp[num][0]]=hp[num]
            elif num+1 in hp:
                hp[num] = [num, hp[num+1][1], hp[num+1][2] + 1]
                # hp[num+1] = hp[num]
                hp[hp[num][1]]=hp[num]
            else:
                hp[num] = [num, num, 1]

            if hp[num][2] > max_length:
                max_length = hp[num][2]

        return max_length


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 6, 7, 8, 9, 5]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # nums = [100, 4, 200, 1, 3, 2]
    # nums = [1,2,0,1]
    res = solution.longestConsecutive(nums)
    print(res)
