import random

class Solution:

    def __init__(self, nums: List[int]):
        self.d = {}
        self.nums = nums
        for num in nums:
            if num in self.d:
                self.d[num] += 1
            else:
                self.d[num] = 1

    def pick(self, target: int) -> int:
        ix = random.randint(0,self.d[target]-1)
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if ix == 0:
                    return i
                else:
                    ix -= 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)