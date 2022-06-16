
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        total_houses = len(nums)
        if total_houses <= 2:
            return max(nums)

        best_robs = [0]*total_houses
        best_robs[0] = nums[0]
        best_robs[1] = max(nums[:2])
        for i in range(2, total_houses):
            best_robs[i] = max(best_robs[i-1], nums[i]+best_robs[i-2])
        
        return best_robs[-1]

          
if __name__ == "__main__":
    # nums = [1, 9, 3, 8, 11, 40, 12]
    nums = [1, 2, 3, 1]
    nums = [2,7,9,3,1]
    nums = [2,1,1,2]
    # nums = [1,3,1,3,100]
    # nums = [8, 2, 8, 9, 2]
    # nums = [8, 9, 9, 4, 10, 5, 6, 9, 7, 9]
    solution = Solution()    
    res = solution.rob(nums)
    print(res)
