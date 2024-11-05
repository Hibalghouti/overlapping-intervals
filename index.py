def merge_intervals(intervals):
   
    merged = [] 
    
    for interval in intervals:
        #This checks if the end of the last interval in the merged list
        # is less than the start of the current interval 
        #merge[start][end]
        if not merged or merged[0][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap so merge the intervals
            merged[0][1] = max(merged[0][1], interval[1])

    return merged


intervals = [[1, 3], [2, 4], [6, 8]]
print(merge_intervals(intervals)) 
