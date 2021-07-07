class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        N = len(nums)
        sum_distance = 0
        d = [0]*32

        for num in nums:
            s = bin(num)
            s = s[::-1][:-2]
            for i in range(len(s)):
                if s[i] == '1':
                    d[i] +=1
        
        for j in range(32):
            sum_distance += d[j] * (N-d[j])

        # def cnt_one(num: int):
        #     cnt = 0
        #     while num > 0:
        #         num = num & (num-1)
        #         cnt += 1
        #     return cnt

        # for i in range(N):
        #     for j in range(i+1,N):
        #         xor = nums[i]^nums[j]

        #         if xor in d:
        #             sum_distance += d[xor]
        #         else:
        #             distance = cnt_one(xor)
        #             d[xor] = distance
        #             sum_distance += distance
        
        # while N > 1:
        #     _nums = []
        #     for i in range(N-1):
        #         xor = nums[i]^nums[i+1]
                
        #         if xor in d:
        #             sum_distance += d[xor]
        #         else:
        #             distance = cnt_one(xor)
        #             d[xor] = distance
        #             sum_distance += distance
                
        #         _nums.append(xor)
        #     nums = _nums
        #     N = len(nums)
        
        return sum_distance