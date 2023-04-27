"""
# Problem 1

Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages.
Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.

Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed
in following fashion :
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113.

https://stackoverflow.com/questions/35517051/split-a-list-of-numbers-into-n-chunks-such-that-the-chunks-have-close-to-equal

https://stackoverflow.com/questions/61648065/split-list-into-n-sublists-with-approximately-equal-sums

Final understanding of the question -

"Split a list in n sublists such that the sum of values differ by a minimum"

My attempts
--------------

pages = [12, 34, 67, 90]
m = 2

def func(pages, m):
    # end = len(pages)
    # i = 0
    # arr = []
    # while i < end:
    #     sum1 = sum(pages[0:i])
    #     sum2 = sum(pages[i:end])
    #
    #     arr.append([sum1, sum2])
    #     i += 1
    #
    # total = min(map(max, arr))
    # print(total)
    #

    div = len(pages)//m
    arr2 = [0]*m

    for i in range(0, m):
        arr2[i] = pages[i:i+div]

    total = min(arr2)
    print(arr2)





    return total

"""
if __name__ == "__main__":
    pass
