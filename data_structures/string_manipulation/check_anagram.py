
#User function Template for python3


class Solution:

    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        dict1 = {}

        for i in a:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[1] = 1

        for i in b:
            if i in dict1:
                dict1[i] -= 1
            if dict1[i] == 0:
                dict1.pop(i)

        return len(dict1) == 0




# #{
# #  Driver Code Starts
# #Initial Template for Python 3
#
# import atexit
# import io
# import sys
#
# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER
#
# @atexit.register
#
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    # t = int(input())
    # for i in range(t):
    # a,b=map(str,input().strip().split())
    a = 'act'
    b = 'tac'
    if(Solution().isAnagram(a,b)):
        print("YES")
    else:
        print("NO")
            # } Driver Code Ends