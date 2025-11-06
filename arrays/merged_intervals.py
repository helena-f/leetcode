class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0])
        merged = [intervals[0]]
        for start_i, end_i in intervals:
            if start_i <= merged[-1][1]:
                merged[-1][1] = max(end_i, merged[-1][1])
            else:
                merged.append([start_i, end_i])
        return merged

        
        
            