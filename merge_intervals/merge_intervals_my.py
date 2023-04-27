class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print('[' + str(self.start) + ',' + str(self.end) + ']', end="")


def merge(intervals):

    mergedIntervals = []
    intervals.sort(key=lambda i: i.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    mergedIntervals.append(Interval(start,end))
    return mergedIntervals

"""
As we are iterating through both the lists once, the time complexity of the above algorithm is O(N + M)O(N+M), where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.

Space complexity ##
Ignoring the space needed for the result list, the algorithm runs in constant space O(1)O(1).

    
"""


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()
    #
    # print("Merged intervals: ", end='')
    # for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    #     i.print_interval()
    # print()
    #
    # print("Merged intervals: ", end='')
    # for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    #     i.print_interval()
    # print()


main()