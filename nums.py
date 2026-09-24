from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums

# outside the class
nums = [0,0,1]
sol = Solution()
print(sol.moveZeroes(nums))