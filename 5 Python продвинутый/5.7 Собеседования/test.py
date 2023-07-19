# https://leetcode.com/problems/two-sum/description/


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, num1 in enumerate(nums):
#             for j, num2 in enumerate(nums):
#                 if i+j == target and i != j:
#                     return [i, j]
                
List = [2, 11, 4, 7, 15]
target = 9
# return [0, 3]


class Solution:
    def twoSum(nums, target):
        pairs = dict()
        for i, num in enumerate(nums):
            key = target - num
            if key in pairs:
                return [pairs[key], i]
            pairs[num] = i


print(Solution.twoSum(nums=List, target=9))

# nums = 2, 11, 4, 7, 15
# target = 9
# return [0, 3]
#