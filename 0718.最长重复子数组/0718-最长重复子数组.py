class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)

        dp = [[0] * len1 for _ in range(len2)]
        max_len = 0
        for i in range(len2):
            for j in range(len1):
                if nums1[j] == nums2[i]:
                    dp[i][j] = 1
                    if i>0 and j>0 and dp[i-1][j-1] > 0:
                        dp[i][j] = 1+dp[i-1][j-1]
                    max_len = max(max_len, dp[i][j])
        # print(dp)
        return max_len