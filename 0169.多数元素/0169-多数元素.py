class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = []
        for x in nums:
            if not stack:
                stack.append(x)
            else:
                if stack[-1] != x:
                    stack.pop()
                else:
                    stack.append(x)
        if stack:
            return stack[0]
        else:
            return 0