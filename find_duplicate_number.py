from typing import List


class Solution:
    def findDuplicate_Hash(self, nums: List[int]) -> int:
        n_arr = [True] * len(nums)

        for i in nums:
            if n_arr[i]:
                n_arr[i] = False
            else:
                return i
            
    
    def findDuplicate(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return nums[0]

        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        



nums = [1,3,4,2,2]

sol = Solution()
print(sol.findDuplicate(nums))
