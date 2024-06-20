def merge_intervals(intervals):
    # Sort the intervals based on the starting time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the list of merged intervals is empty or the current interval does not overlap with the previous one, append it
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, so merge the current and previous intervals
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

# Function to get input intervals from the user
def get_intervals_from_user():
    intervals = []
    n = int(input("Enter the number of intervals: "))
    for i in range(n):
        start = int(input(f"Enter the start of interval {i+1}: "))
        end = int(input(f"Enter the end of interval {i+1}: "))
        intervals.append((start, end))
    return intervals

# Get intervals from the user
intervals = get_intervals_from_user()

# Merge intervals and print the result
merged_intervals = merge_intervals(intervals)
print(f"Merged intervals: {merged_intervals}")
