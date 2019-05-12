class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
      length = len(nums)
      for i in range(length):
        _target = target - nums.pop(0)
        if _target in nums:
          return [i, nums.index(_target)+i+1]

assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([2, 0, 11, 7], 11) == [1, 2]
assert Solution().twoSum([1, 3, 4, 2], 6) == [2, 3]