class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        intervals.append(newInterval)
        intervals.sort()
        
        # print(intervals)

        for interval in intervals:
            if output:
                if interval[0] > output[-1][1]:
                    output.append(interval)
                else:
                    output[-1][1] = max(interval[1],output[-1][1])
            else:
                output.append(interval)
        
        return output

'''
[[1,3],[6,9]]
[2,5]
'''