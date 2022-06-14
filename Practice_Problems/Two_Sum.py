from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]

    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))