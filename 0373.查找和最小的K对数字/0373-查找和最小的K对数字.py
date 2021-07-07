class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        items = []
        for num1 in nums1[:k]:
            for num2 in nums2[:k]:
                if len(items) < k:
                    heapq.heappush(items,((num1+num2)*-1, [num1,num2]))
                else:
                    if items[0][0] * -1 > (num1+num2):
                        heapq.heappushpop(items, ((num1+num2)*-1, [num1,num2]))
        
        res = []
        for _ in range(k):
            if not items:
                break
            item = heapq.heappop(items)
            res.append(item[1])
        res.reverse()
        return res


            

