# Python3 program to count cumlative
# frequencies of elements in an unsorted array.
def countFreq(a, n):

    # Insert elements and their
    # frequencies in hash map.
    hm = {}
    for i in range(0, n):
        hm[a[i]] = hm.get(a[i], 0) + 1

    # Declare a set
    st = set()

    # Insert the element and
    # its frequency in a set
    for x in hm:
        st.add((x, hm[x]))

    cumul = 0

    # Iterate the set and print
    # the cumulative frequency
    for x in sorted(st):
        cumul += x[1]
        print(x[0], cumul)

    # Driver Code
if __name__ == "__main__":

    a = [1, 3, 2, 4, 2, 1]
    n = len(a)
    countFreq(a, n)

# This code is contributed by Rituraj Jain
