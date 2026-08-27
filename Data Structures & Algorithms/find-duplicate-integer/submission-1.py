class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        fast = nums[nums[0]]
        slow = nums[0]
        while True:
            if fast == slow:
                slow = 0
                while True: 
                    fast = nums[fast]
                    slow = nums[slow]
                    if fast == slow:
                        return slow 
            fast = nums[nums[fast]]
            slow = nums[slow]
