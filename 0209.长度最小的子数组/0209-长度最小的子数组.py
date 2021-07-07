class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        q = []
        sum_q = 0
        cur_len = 0
        min_len = len(nums)+1
        for num in nums:
            q.append(num)
            sum_q += num
            cur_len += 1

            while sum_q >= s:
                if cur_len < min_len:
                    min_len = cur_len
                sum_q -= q.pop(0)
                cur_len -= 1
        
        if min_len == len(nums)+1:
            return 0
        return min_len