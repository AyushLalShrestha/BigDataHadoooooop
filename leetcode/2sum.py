

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req_map = dict()
        result = list()
        for i, num in enumerate(nums):
            if num in req_map:
                # result.append([req_map[num], num])
                return [req_map[num], i]
            else:
                req = target - num
                req_map[req] = i
        return result
    

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [3,2,4]
    # target = 6
    result  = solution.twoSum(nums, target)
    print(result)
                
        
        