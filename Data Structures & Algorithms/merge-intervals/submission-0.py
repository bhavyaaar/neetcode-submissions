class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #for an interval to merge the ending time must be greater than the starting time of another interval, this creates overlapping intervals 
        #for example [1,3 ] and [1,5] would be considered overlapping, and 
        #3 > 1

        # always sort by the start times ascedending order
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            #check if the merged intervals list is empty
            #comapred the end time of the last itnerval in merged with the start time of the current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                #if they overlap we only need to chnage the end time and to do this we compare the interval that is already in merge and the current intervals end times and see which one is larger and set that 
        return merged




        