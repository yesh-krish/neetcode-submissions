"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""[(1,40), (2,5), (6,10),(40,45), (45, 90)]
1 -> [(1, 40) (40,45),]
2 -> [(2,4), (6,10)}

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        daysMap = {1: [intervals[0]]}
        days = 1
        

        for i in range(1, len(intervals)):
            curInterval = intervals[i]

            for j in range(1, days + 1):
                
                if daysMap[j][-1].end <= curInterval.start:
                    daysMap[j].append(curInterval)
                    break
                else:
                    if j == days:
                        days += 1
                        daysMap[days] = [curInterval]
        return days
                        

