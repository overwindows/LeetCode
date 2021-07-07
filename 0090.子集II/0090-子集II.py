class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        N = len(nums)

        subsets_num = 2**N 
        # print(subsets_num)
        for i in range(subsets_num):
            cand = []
            pos = list(bin(i))[2:]
            pos.reverse()
            # print(pos)
            for i in range(len(pos)):
                if pos[i] == '1':
                    cand.append(nums[i])
            cand.sort()
            if cand not in subsets:
                subsets.append(cand)
        subsets.sort()
        return subsets
