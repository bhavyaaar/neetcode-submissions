class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #edge cases to consider: what if there is no interval, or 1 value in an interval 
        # need to sort the intervals by their starting time 
        # have a running merged array that i can work with 

    
        if not intervals:
            return False 
       #sorting by the start date helps us traverse and compare easier  
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged






